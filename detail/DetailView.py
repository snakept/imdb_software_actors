from PyQt6.QtWidgets import QWidget, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap

from detail.DetailViewModel import DetailViewModel
from detail.DetailThread import DetailThread

API_URL = "https://imdb-api.com/API/Name/"


class DetailView(QWidget):

    def __init__(self, apiKey, path):
        super().__init__()
        self.path = path
        self.apiKey = apiKey

    def initContent(self, pixmap, name, id):
        self.id = id
        self.actressUrl = ""
        if self.apiKey == "t":
            self.actressUrl = self.path + "/TestData_MelGibson.json"
        else:
            self.actressUrl = API_URL + self.apiKey + "/" + self.id

        self.actressDf = []
        self.initUi(pixmap, name)

        self.initThread()
        self.runThread()

    def initUi(self, pixmap, name):
        # ImageLabel
        pixmap = pixmap.scaledToHeight(150)
        self.imageLabel.setPixmap(pixmap)

        # NameLabel
        self.nameLabel.setText(name)

    def setUiContent(self):
        # GenresLabel
        self.genresLabel.setText(self.id)

        # About Text
        # self.aboutText.setText(self.actressDf['summary'])

        # All Movies
        header = ["Title", "Year", "Awards", "Genre"]
        self.moviesTableView.setColumnCount(4)
        self.moviesTableView.setHorizontalHeaderLabels(header)
        self.moviesTableView.verticalHeader().setVisible(False)
        # movies = self.actressDf['castMovies']
        # for i, movie in enumerate(movies):
        #     self.moviesTableView.insertRow(i)
        #     self.moviesTableView.setItem(
        #         i, 0, QTableWidgetItem(movie['title']))
        #     self.moviesTableView.setItem(
        #         i, 1, QTableWidgetItem(movie['year']))
        print(self.actressDf)

    def initThread(self):
        self.detailThread = DetailThread(
            self.actressDf, self.actressUrl)
        self.detailThread.moviesListFinished.connect(self.setUiContent)

    def runThread(self):
        self.detailThread.run()
