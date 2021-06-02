import os
import sys
from PyQt6.QtWidgets import QApplication

from landing.MainWindow import MainWindow

DEFAULT_API_KEY = "k_vhvsnz5j"
OTHER_API_KEY = "k_66k35hbm"
ANOTHER_API_KEY = "k_1dlps7sm"

if __name__ == "__main__":
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)

    app = QApplication(sys.argv)

    apiKey = ANOTHER_API_KEY
    if len(sys.argv) > 1:
        apiKey = sys.argv[1]

    window = MainWindow(apiKey, path)
    window.show()
    sys.exit(app.exec())
