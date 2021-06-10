import os
import sys
import random
from PyQt6.QtWidgets import QApplication

from landing.MainWindow import MainWindow

API_KEY_LIST = ["k_vhvsnz5j", "k_66k35hbm", "k_1dlps7sm"]

if __name__ == "__main__":
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)

    app = QApplication(sys.argv)

    # random choice for maximal api calls
    choice = int(3.0 * random.random())

    apiKey = API_KEY_LIST[choice]

    window = MainWindow(apiKey, path)
    window.show()
    sys.exit(app.exec())
