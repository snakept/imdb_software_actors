import os
import sys
from PyQt6.QtWidgets import QApplication

from landing.MainWindow import MainWindow

API_URL = "https://imdb-api.com/en/API/IMDbList/k_vhvsnz5j/ls053501318"

if __name__ == "__main__":
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)

    app = QApplication([])
    window = MainWindow(path, API_URL)
    window.show()
    sys.exit(app.exec())
