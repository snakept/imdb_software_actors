import ssl
import json
import requests as req
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal


class DetailThread(QThread):

    moviesListFinished = pyqtSignal(bool)

    def __init__(self, movies, description, apiUrl):
        super().__init__()
        self.apiUrl = apiUrl
        self.movies = movies
        self.description = description

    def run(self):
        ssl._create_default_https_context = ssl._create_unverified_context

        jsonData = req.get(self.apiUrl).json()
        self.description = jsonData['summary']
        for movie in jsonData['castMovies']:
            self.movies.append(movie)
        self.moviesListFinished.emit(True)
