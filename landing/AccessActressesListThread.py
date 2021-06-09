from PyQt6.QtCore import QThread, pyqtSignal
import pandas as pd
import requests as req
from landing.ActressListElement import ActressListElement


class AccessActressesListThread(QThread):

    actressAddedSignal = pyqtSignal(bool)
    started = pyqtSignal(bool)
    finished = pyqtSignal(bool)

    def __init__(self, actressesUrl, actressesListData):
        QThread.__init__(self)
        self.actressesUrl = actressesUrl
        self.actressesListData = actressesListData
        self.actressesDf = []

    def fetchActressesDataFromUrl(self):
        self.actressesListData.clear()
        # so button can be disabled
        self.started.emit(True)
        actressesRequest = req.get(self.actressesUrl)

        # when status is ok read actresses into dataframe
        if actressesRequest.status_code == 200:
            actressesData = pd.read_json(actressesRequest.content)
            self.actressesDf = actressesData['items']

            if len(self.actressesDf) == 0:
                ("No data provided for the link " + self.actressesUrl)
                return
        else:
            print("Error occured fetch didn't succeed. Error code: " +
                  str(actressesRequest.status_code))

    def fetchActress(self, actress):

        imageBin = req.get(actress['image']).content
        actressListItem = ActressListElement(
            actress['fullTitle'], actress['id'], imageBin)
        self.actressesListData.append(actressListItem)

        # to handle layout adaption
        self.actressAddedSignal.emit(True)

    def run(self):
        self.fetchActressesDataFromUrl()

        for actress in self.actressesDf:
            self.fetchActress(actress)

        # to enable fetch button again
        self.finished.emit(True)
