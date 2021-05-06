import ssl
import json
import requests as req
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal


class DetailThread(QThread):

    moviesListFinished = pyqtSignal(bool)

    def __init__(self, actressDf, actressUrl):
        super().__init__()
        self.actressDf = actressDf
        self.actressUrl = actressUrl

    def run(self):

        self.fetchActressDataFromUrl()
        self.moviesListFinished.emit(True)

    def fetchActressDataFromUrl(self):
        ssl._create_default_https_context = ssl._create_unverified_context

        self.actressDf = pd.read_json(self.actressUrl)
        try:
            pass
        except:
            print("Couldn't read data from " + self.actressUrl)
