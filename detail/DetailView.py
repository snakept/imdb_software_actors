import os
import ssl

import pandas as pd
import requests as req

from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QTableWidgetItem, QWidget
from PyQt6.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
from PyQt6.QtGui import QCloseEvent

from detail.ActressDetail import ActressDetail

API_URL = "https://imdb-api.com/API/Name/"


class MoviesDataWorker(QObject):

    fetchedData = pyqtSignal(float, str, int)

    @pyqtSlot(str, int)
    def fetchMovieData(self, url, index):
        page = req.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Rating
        ratingSpan = soup.select_one(
            'span[class*="AggregateRatingButton__RatingScore"]')
        rating = -1.0
        if ratingSpan:
            ratingString = ratingSpan.text
            rating = float(ratingString)

        # For genre select storyline div
        genreA = soup.select_one('a[href*="genres"]')

        genre = "----"
        if len(genreA) > 0:
            genre = genreA.text

        self.fetchedData.emit(rating, genre, index)


class DetailView(QWidget):

    requestedMovieRatingFetch = pyqtSignal(str, int)

    sumRating = 0.0
    ratingCount = 0
    averageRating = 0.0

    def __init__(self, apiKey, path):
        super().__init__()
        self.apiKey = apiKey
        self.path = path

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.workerThread.terminate()
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
        self.actressDetail.moviesDf = df[df['role'] == 'Actor']
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
            "Average Rating: " + str(self.averageRating))

        # About Text
        self.aboutText.setPlainText(self.actressDetail.about)

        # movies table
        self.moviesTableView.setColumnCount(5)
        header = ["Title", "Year", "Awards", "Genre", "Rating"]
        self.moviesTableView.setHorizontalHeaderLabels(header)
        self.moviesTableView.verticalHeader().setVisible(False)

        self.worker = MoviesDataWorker()
        self.workerThread = QThread()

        self.worker.fetchedData.connect(self.useMovieDataAt)
        self.requestedMovieRatingFetch.connect(self.worker.fetchMovieData)
        self.worker.moveToThread(self.workerThread)

        self.workerThread.start()
        self.setMoviesTableContent()

    def useMovieDataAt(self, rating, genre, index):

        # add data to genre list
        if genre not in self.actressDetail.genres:
            self.actressDetail.genres.append(genre)

            # only append comma when at least a genre exists
            if len(self.genresString) > 0:
                self.genresString = self.genresString + ", " + genre
            else:
                self.genresString = genre

            self.genresLabel.setText(self.genresString)

        # add genre to movie
        self.moviesTableView.setItem(
            index, 3, QTableWidgetItem(genre))

        # add rating to movie if available
        if rating > 0.0:
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

            url = "https://www.imdb.com/title/" + \
                self.actressDetail.moviesDf.at[i, 'id']
            self.requestedMovieRatingFetch.emit(url, i)

        self.moviesTableView.resizeColumnsToContents()
