import sys
from PyQt6.QtGui import QImage, QStandardItemModel

from PyQt6.QtWidgets import QListWidgetItem, QMainWindow, QLabel, QListWidget
from PyQt6.uic import loadUi

from ActressListElement import ActressListElement
from detail.DetailView import DetailView
from landing.ActressesListModel import ActressesListModel
from landing.AccessActressesListThread import AccessActressesListThread
from PyQt6.QtWidgets import QItemDelegate


class MainWindow(QMainWindow):
    def __init__(self, path, apiKey):
        super().__init__()
        self.detailView = DetailView(apiKey)
        loadUi(path + "/Layouts/main_view.ui", self)
        loadUi(path + "/Layouts/detail.ui", self.detailView)

        self.actressesApiUrl = "https://imdb-api.com/en/API/IMDbList/" + apiKey + "/ls053501318"

        self.actressesList = []
        self.model = ActressesListModel(self.actressesList)
        self.actressesListView.setModel(self.model)
        self.actressesListView.clicked.connect(self.actressClicked)

        self.fetchButton.clicked.connect(self.fetchButtonClicked)

    def actressClicked(self, index):
        i = index.row()
        actressPixmap = self.actressesList[i].pixmap
        actressName = self.actressesList[i].name
        actressId = self.actressesList[i].id
        self.detailView.initContent(actressPixmap, actressName, actressId)
        self.detailView.show()

    def fetchButtonClicked(self):
        if self.fetchButton.isEnabled:
            self.fetchButton.setEnabled(False)
            self.startFetchingActresses()

    def setFetchButtonEnabled(self):
        self.fetchButton.setEnabled(True)

    def startFetchingActresses(self):
        self.fetchThread = AccessActressesListThread(
            self.actressesApiUrl, self.actressesList)
        self.fetchThread.started.connect(self.model.layoutChanged.emit)
        self.fetchThread.actressSignal.connect(self.model.layoutChanged.emit)
        self.fetchThread.finished.connect(self.setFetchButtonEnabled)
        self.fetchThread.start()
