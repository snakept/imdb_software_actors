import ssl
import requests as req
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal


class DetailThread(QThread):

    moviesListFinished = pyqtSignal(bool)

    def __init__(self, actressUrl, actressDetail):
        super().__init__()
        self.actressUrl = actressUrl
        self.actressDetail = actressDetail

    def run(self):

        self.fetchActressDataFromUrl()
        self.moviesListFinished.emit(True)

    def fetchActressDataFromUrl(self):
        ssl._create_default_https_context = ssl._create_unverified_context

        jsonData = req.get(self.actressUrl).json()
        df = pd.DataFrame(jsonData['castMovies'])
        self.actressDetail.moviesDf = df[df['role'] == 'Actor']
        self.actressDetail.about = jsonData['summary']
