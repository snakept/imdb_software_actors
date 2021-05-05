import sys
from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow

API_URL = "https://imdb-api.com/en/API/IMDbList/k_vhvsnz5j/ls053501318"

if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow(API_URL)
    window.show()
    sys.exit(app.exec())
