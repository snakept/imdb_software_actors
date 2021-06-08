import ssl
import re

import pandas as pd
import requests as req

from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QTableWidgetItem, QWidget
from PyQt6.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QCloseEvent

from detail.ActressDetail import ActressDetail

API_URL = "https://imdb-api.com/API/Name/"


class MoviesDataWorker(QObject):

    fetchedData = pyqtSignal(float, str, str, int)
    finished = pyqtSignal()

    def __init__(self, moviesDf):
        super().__init__()
        self.moviesDf = moviesDf

    @pyqtSlot()
    def fetchMovieData(self):

        for i, _ in self.moviesDf.iterrows():

            url = "https://www.imdb.com/title/" + \
                self.moviesDf.at[i, 'id']
            page = req.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Rating
            ratingSpan = soup.select_one(
                'span[class*="AggregateRatingButton__RatingScore"]')
            rating = -1.0
            if ratingSpan:
                ratingString = ratingSpan.text
                rating = float(ratingString)

            # Awards
            awardsText = ""
            awardsContainer = soup.find(
                'div', attrs={'data-testid': "tmd_awards"})
            if awardsContainer:
                awards = awardsContainer.find(
                    'span', class_='ipc-metadata-list-item__list-content-item')
                awardsText = awards.text

            # For genre select storyline div
            genreA = soup.select_one('a[href*="genres"]')

            genre = "----"
            if genreA:
                genre = genreA.text

            self.fetchedData.emit(rating, awardsText, genre, i)

        self.finished.emit()


class ActressAwardsDataWorker(QObject):

    fetchedData = pyqtSignal(dict)

    def __init__(self, actressId):
        super().__init__()
        self.actressId = actressId

    @pyqtSlot()
    def fetchAwardsData(self):

        url = "https://www.imdb.com/name/" + self.actressId + "/awards"

        page = req.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        awardsSoup = soup.find_all('table', attrs={'class': 'awards'})
        awards = {"title": [], "outcome": [], "year": []}
        for award in awardsSoup:

            # award title
            awardTitle = award.find(class_="award_category").text.strip()
            awards['title'].append(awardTitle)

            # outcome
            outcomeWrapper = award.find(class_="award_outcome")
            outcome = outcomeWrapper.findChildren()[0].text.strip()
            awards['outcome'].append(outcome)

            # year
            yearWrapper = award.find(class_="award_year")
            year = yearWrapper.findChildren()[0].text.strip()
            awards['year'].append(year)

        self.fetchedData.emit(awards)


class DetailView(QWidget):

    # signals for MovieDataWorker
    requestedMovieRatingFetch = pyqtSignal()
    requestToQuitThread = pyqtSignal()

    # signal for ActressAwardsDataWorker
    requestActressAwards = pyqtSignal()

    sumRating = 0.0
    ratingCount = 0
    averageRating = 0.0

    def __init__(self, apiKey, path):
        super().__init__()
        self.apiKey = apiKey
        self.path = path

    def closeEvent(self, a0: QCloseEvent):
        self.workerMoviesThread.terminate()
        self.workerActressAwardsThread.terminate()
        self.workerMoviesThread.wait(600)

        return super().closeEvent(a0)

    def initContent(self, pixmap, name, id):
        self.actressUrl = API_URL + self.apiKey + "/" + id
        self.actressDetail = ActressDetail(id, name, pixmap)

        ssl._create_default_https_context = ssl._create_unverified_context

        jsonData = req.get(self.actressUrl).json()
        df = pd.DataFrame(jsonData['castMovies'])
        df['awards'] = "none"
        df['genre'] = "default"
        df['rating'] = 0.0
        df['position'] = -1
        self.actressDetail.moviesDf = df
        self.actressDetail.about = jsonData['summary']

        # ImageLabel
        pixmap = self.actressDetail.pixmap.scaledToHeight(150)
        self.imageLabel.setPixmap(pixmap)

        # NameLabel
        self.nameLabel.setText(name)

        # Genres
        self.genresString = ""
        self.genresLabel.setText("Genres: ")

        # Average Rating
        self.avRatingLabel.setText(
            "Average Movie Rating: " + str(self.averageRating))

        # About Text
        self.aboutText.setPlainText(self.actressDetail.about)

        # Awards Table
        self.awardsTable.setColumnCount(3)
        headerAwards = ["Title", "Outcome", "Year"]
        self.awardsTable.setHorizontalHeaderLabels(headerAwards)
        self.awardsTable.verticalHeader().setVisible(False)

        # movies table
        self.moviesTableView.setColumnCount(5)
        headerMovies = ["Title", "Year", "Awards", "Genre", "Rating"]
        self.moviesTableView.setHorizontalHeaderLabels(headerMovies)
        self.moviesTableView.verticalHeader().setVisible(False)

        # top movies table
        self.topMoviesTable.setColumnCount(3)
        headerTopMovies = ["Title", "Year", "Genre"]
        self.topMoviesTable.setHorizontalHeaderLabels(headerTopMovies)
        self.topMoviesTable.verticalHeader().setVisible(False)

        # MoviesWorker
        self.workerMovies = MoviesDataWorker(self.actressDetail.moviesDf)
        self.workerMoviesThread = QThread()

        self.workerMovies.fetchedData.connect(self.useMovieDataAt)
        self.workerMovies.finished.connect(self.setTop5Movies)
        self.requestedMovieRatingFetch.connect(
            self.workerMovies.fetchMovieData)
        self.workerMovies.moveToThread(self.workerMoviesThread)

        self.workerMoviesThread.start()

        self.setMoviesTableContent()

        # ActressAwardsWorker
        self.workerActressAwards = ActressAwardsDataWorker(
            self.actressDetail.id)
        self.workerActressAwardsThread = QThread()

        self.workerActressAwards.fetchedData.connect(self.setActressAwards)
        self.requestActressAwards.connect(
            self.workerActressAwards.fetchAwardsData)
        self.workerActressAwards.moveToThread(self.workerActressAwardsThread)

        self.workerActressAwardsThread.start()
        self.requestActressAwards.emit()

    def useMovieDataAt(self, rating, awards, genre, index):

        # Awards
        self.actressDetail.moviesDf.at[index, 'awards'] = awards
        self.moviesTableView.setItem(
            index, 2, QTableWidgetItem(awards))

        # add data to genre list
        if genre not in self.actressDetail.genres and genre.__contains__("-") == False:
            self.actressDetail.genres.append(genre)

            # only append comma when at least a genre exists
            if len(self.genresString) > 0:
                self.genresString = self.genresString + ", " + genre
            else:
                self.genresString = "Genres: " + genre

            self.genresLabel.setText(self.genresString)

        # add genre to movie
        self.actressDetail.moviesDf.at[index, 'genre'] = genre
        self.moviesTableView.setItem(
            index, 3, QTableWidgetItem(genre))

        # add rating to movie if available
        if rating > 0.0:
            self.actressDetail.moviesDf.at[index, 'rating'] = rating
            self.moviesTableView.setItem(
                index, 4, QTableWidgetItem(str(rating)))

            # set average data
            self.ratingCount += 1
            self.sumRating += rating
            self.averageRating = self.sumRating / float(self.ratingCount)
            self.avRatingLabel.setText(
                "Average Rating: " + str(round(self.averageRating, 2)))

        else:
            self.moviesTableView.setItem(index, 4, QTableWidgetItem("-.-"))

        self.moviesTableView.resizeColumnsToContents()

    def setTop5Movies(self):
        top5moviesDf = self.actressDetail.moviesDf.sort_values(
            by=["rating"], ascending=False).head(5)
        i = 0
        for _, movie in top5moviesDf.iterrows():
            self.topMoviesTable.insertRow(i)
            self.topMoviesTable.setItem(i, 0, QTableWidgetItem(movie['title']))
            self.topMoviesTable.setItem(i, 1, QTableWidgetItem(movie['year']))
            self.topMoviesTable.setItem(
                i, 2, QTableWidgetItem(str(movie['rating'])))
            i += 1

        self.topMoviesTable.resizeColumnsToContents()

    def setActressAwards(self, awards):
        awards = sortAwards(awards)
        self.actressDetail.awards = awards

        n = len(awards['year'])

        for i in range(0, n):
            self.awardsTable.insertRow(i)
            self.awardsTable.setItem(
                i, 0, QTableWidgetItem(awards['title'][i]))
            self.awardsTable.setItem(
                i, 1, QTableWidgetItem(awards['outcome'][i]))
            self.awardsTable.setItem(
                i, 2, QTableWidgetItem(awards['year'][i]))

        self.awardsTable.resizeColumnsToContents()

    def setMoviesTableContent(self):

        # Add Movies to table
        for i, movie in self.actressDetail.moviesDf.iterrows():
            title = movie['title']
            year = movie['year']

            self.moviesTableView.insertRow(i)
            self.moviesTableView.setItem(
                i, 0, QTableWidgetItem(title))
            self.moviesTableView.setItem(
                i, 1, QTableWidgetItem(year))

        self.requestedMovieRatingFetch.emit()
        self.moviesTableView.resizeColumnsToContents()


def getNumberBeforeSubString(string, subString) -> int:
    numString = re.findall("(\d+) *" + subString + "*", string)
    if len(numString) > 0:
        return int(numString[0])
    else:
        return 0


def sortAwards(awards) -> dict:
    n = len(awards['year'])

    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if awards['year'][j+1] < awards['year'][j]:
                swapYear = awards['year'][j]
                swapOutcome = awards['outcome'][j]
                swapTitle = awards['title'][j]
                awards['year'][j] = awards['year'][j+1]
                awards['outcome'][j] = awards['outcome'][j+1]
                awards['title'][j] = awards['title'][j+1]
                awards['year'][j+1] = swapYear
                awards['outcome'][j+1] = swapOutcome
                awards['title'][j+1] = swapTitle

    return awards
