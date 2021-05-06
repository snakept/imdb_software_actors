from PyQt6.QtWidgets import QWidget, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap

from detail.DetailViewModel import DetailViewModel
from detail.DetailThread import DetailThread

API_URL = "https://imdb-api.com/API/Name/"


class DetailView(QWidget):

    def __init__(self, apiKey):
        super().__init__()
        self.apiKey = apiKey

    def initContent(self, pixmap, name, id):
        self.id = id
        self.actressApiUrl = API_URL + self.apiKey + "/" + self.id
        self.initUi(pixmap, name)
        self.description = ""
        self.movies = []

        self.initThread()
        self.runThread()

    def initUi(self, pixmap, name):
        # ImageLabel
        pixmap = pixmap.scaledToHeight(150)
        self.imageLabel.setPixmap(pixmap)

        # NameLabel
        self.nameLabel.setText(name)

        # GenresLabel
        self.genresLabel.setText(self.id)

        # All Movies
        header = ["Title", "Year", "Awards", "Genre"]
        self.moviesTableView.setColumnCount(4)
        self.moviesTableView.setHorizontalHeaderLabels(header)

    def fillMoviesTableView(self):
        for i, movie in enumerate(self.movies):
            self.moviesTableView.setItem(
                i, 0, QTableWidgetItem(movie['title']))
            self.moviesTableView.setItem(
                i, 1, QTableWidgetItem(movie['year']))
            print(i)

    def initThread(self):
        self.detailThread = DetailThread(
            self.movies, self.description, self.actressApiUrl)
        self.detailThread.moviesListFinished.connect(self.fillMoviesTableView)

    def runThread(self):
        self.detailThread.run()
