import sys
from PyQt6.QtGui import QImage, QStandardItemModel

import pandas as pd
import requests as req
from PyQt6.QtWidgets import QListWidgetItem, QMainWindow, QApplication, QLabel, QListWidget
from PyQt6.uic import loadUi

from ActressesListModel import ActressesListModel
from ActressListElement import ActressListElement
from AccessActressesListThread import AccessActressesListThread
from PyQt6.QtWidgets import QItemDelegate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Layouts/main_view.ui", self)

        self.actressesUrl = "https://imdb-api.com/en/API/IMDbList/k_vhvsnz5j/ls053501318"

        self.actressesList = []
        self.model = ActressesListModel(self.actressesList)
        self.actressesListView.setModel(self.model)

        self.fetchButton.clicked.connect(self.fetchButtonClicked)

    def fetchButtonClicked(self):
        if self.fetchButton.isEnabled:
            self.fetchButton.setEnabled(False)
            self.startFetchingActresses()

    def setFetchButtonEnabled(self):
        self.fetchButton.setEnabled(True)

    def startFetchingActresses(self):
        self.fetchThread = AccessActressesListThread(
            self.actressesUrl, self.actressesList)
        self.fetchThread.started.connect(self.model.layoutChanged.emit)
        self.fetchThread.actressSignal.connect(self.model.layoutChanged.emit)
        self.fetchThread.finished.connect(self.setFetchButtonEnabled)
        self.fetchThread.start()


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
