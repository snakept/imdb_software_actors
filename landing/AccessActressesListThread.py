from PyQt6.QtCore import QThread, pyqtSignal
import pandas as pd
import requests as req
from ActressListElement import ActressListElement


class AccessActressesListThread(QThread):

    actressSignal = pyqtSignal(bool)
    started = pyqtSignal(bool)
    finished = pyqtSignal(bool)

    def __init__(self, imdbLink, actressesListData):
        QThread.__init__(self)
        self.imdbLink = imdbLink
        self.actressesListData = actressesListData
        self.actressesDf = []

    def fetchActressesData(self):
        self.actressesListData.clear()
        self.started.emit(True)
        actressesRequest = req.get(self.imdbLink).content
        actressesData = pd.read_json(actressesRequest)
        self.actressesDf = actressesData['items']

    def fetchActress(self, actress):

        imageBin = req.get(actress['image']).content
        actressListItem = ActressListElement(
            actress['fullTitle'], imageBin)
        self.actressesListData.append(actressListItem)
        self.actressSignal.emit(True)

    def run(self):
        self.fetchActressesData()

        for actress in self.actressesDf:
            self.fetchActress(actress)

        self.finished.emit(True)
