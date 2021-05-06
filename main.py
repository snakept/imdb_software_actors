import os
import sys
from PyQt6.QtWidgets import QApplication

from landing.MainWindow import MainWindow

DEFAULT_API_KEY = "k_vhvsnz5j"

if __name__ == "__main__":
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)

    app = QApplication(sys.argv)

    apiKey = DEFAULT_API_KEY
    if len(sys.argv) > 1:
        apiKey = sys.argv[1]

    window = MainWindow(path, apiKey)
    window.show()
    sys.exit(app.exec())
