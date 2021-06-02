from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtGui import QCloseEvent

from detail.DetailView import DetailView
from landing.ActressesListModel import ActressesListModel
from landing.AccessActressesListThread import AccessActressesListThread


class MainWindow(QMainWindow):
    def __init__(self, apiKey, path):
        super().__init__()
        self.apiKey = apiKey
        self.path = path

        loadUi(self.path + "/Layouts/main_view.ui", self)

        self.actressesUrl = self.actressesUrl = "https://imdb-api.com/en/API/IMDbList/" + \
            apiKey + "/ls053501318"

        self.actressesList = []
        self.model = ActressesListModel(self.actressesList)
        self.actressesListView.setModel(self.model)
        self.actressesListView.clicked.connect(self.actressClicked)

        self.fetchButton.clicked.connect(self.fetchButtonClicked)

    def actressClicked(self, index):
        self.detailView = DetailView(self.apiKey, self.path)
        loadUi(self.path + "/Layouts/detail.ui", self.detailView)

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
            self.actressesUrl, self.actressesList)

        # when the list changes update listview
        self.fetchThread.actressAddedSignal.connect(
            self.model.layoutChanged.emit)

        # Reset the fetch button only when everything is fetched
        self.fetchThread.finished.connect(self.setFetchButtonEnabled)
        self.fetchThread.start()
