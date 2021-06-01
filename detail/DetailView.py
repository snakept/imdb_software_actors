import os
from PyQt6.QtWidgets import QTableWidgetItem, QWidget
from PyQt6.uic import loadUi

from detail.ActressDetail import ActressDetail
from detail.DetailThread import DetailThread

API_URL = "https://imdb-api.com/API/Name/"


class DetailView(QWidget):

    def __init__(self, apiKey, path):
        super().__init__()
        self.apiKey = apiKey
        self.path = path

    def initContent(self, pixmap, name, id):
        self.actressUrl = API_URL + self.apiKey + "/" + id
        self.actressDetail = ActressDetail(id, name, pixmap)

        self.initUi()

        self.initThread()

    def initUi(self):
        # ImageLabel
        pixmap = self.actressDetail.pixmap.scaledToHeight(150)
        self.imageLabel.setPixmap(pixmap)

        # NameLabel
        self.nameLabel.setText(self.actressDetail.name)

    def setUiContent(self):
        # GenresLabel
        self.genresLabel.setText(self.actressDetail.id)

        # About Text
        self.aboutText.setPlainText(self.actressDetail.about)

        # All Movies
        header = ["Title", "Year", "Awards", "Genre"]
        self.moviesTableView.setColumnCount(4)
        self.moviesTableView.setHorizontalHeaderLabels(header)
        self.moviesTableView.verticalHeader().setVisible(False)
        movies = self.actressDetail.moviesDf

        for i, movie in movies.iterrows():
            title = movie['title']
            year = movie['year']

            self.moviesTableView.insertRow(i)
            self.moviesTableView.setItem(
                i, 0, QTableWidgetItem(title))
            self.moviesTableView.setItem(
                i, 1, QTableWidgetItem(year))

        self.moviesTableView.resizeColumnsToContents()

    def initThread(self):
        self.detailThread = DetailThread(self.actressUrl, self.actressDetail)
        self.detailThread.moviesListFinished.connect(self.setUiContent)

    def runThread(self):
        self.detailThread.run()
