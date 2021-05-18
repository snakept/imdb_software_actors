from PyQt6.QtCore import QThread, pyqtSignal
import pandas as pd
import requests as req
from ActressListElement import ActressListElement


class AccessActressesListThread(QThread):

    actressSignal = pyqtSignal(bool)
    started = pyqtSignal(bool)
    finished = pyqtSignal(bool)

    def __init__(self, actressesUrl, actressesListData):
        QThread.__init__(self)
        self.actressesUrl = actressesUrl
        self.actressesListData = actressesListData
        self.actressesDf = []

    def fetchActressesDataFromUrl(self):
        self.actressesListData.clear()
        self.started.emit(True)
        actressesRequest = req.get(self.actressesUrl)
        if actressesRequest.status_code == 200:
            actressesData = pd.read_json(actressesRequest.content)
            self.actressesDf = actressesData['items']

            if len(self.actressesDf) == 0:
                print("No data provided for the link " + self.actressesUrl)
                return
        else:
            print("Error occured fetch didn't succeed. Error code: " +
                  actressesRequest.status_code)

    def loadFromFile(self):
        self.actressesListData.clear()
        self.started.emit(True)

        try:
            df = pd.read_json_normalize(self.actressesUrl)
            self.actressesDf = df['items']

        except:
            print("Couldn't read data from " + self.actressesUrl)

    def fetchActress(self, actress):

        imageBin = req.get(actress['image']).content
        actressListItem = ActressListElement(
            actress['fullTitle'], actress['id'], imageBin)
        self.actressesListData.append(actressListItem)
        self.actressSignal.emit(True)

    def run(self):
        if self.actressesUrl.find("http") != -1:
            self.fetchActressesDataFromUrl()
        else:
            self.loadFromFile()

        for actress in self.actressesDf:
            self.fetchActress(actress)

        self.finished.emit(True)