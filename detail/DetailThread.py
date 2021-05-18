import ssl
import json
import requests as req
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal


class DetailThread(QThread):

    moviesListFinished = pyqtSignal(bool)

    def __init__(self, moviesDf, about, actressUrl):
        super().__init__()
        self.moviesDf = moviesDf
        self.about = about
        self.actressUrl = actressUrl

    def run(self):

        self.fetchActressDataFromUrl()
        self.moviesListFinished.emit(True)

    def fetchActressDataFromUrl(self):
        ssl._create_default_https_context = ssl._create_unverified_context

        jsonData = req.get(self.actressUrl).json()
        self.moviesDf = pd.DataFrame(jsonData['knownFor'])
        self.about = jsonData['summary']

        try:
            pass
        except:
            print("Couldn't read data from " + self.actressUrl)
