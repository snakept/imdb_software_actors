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

    # random choice of api key because only 100 calls are possible per day
    apiKey = random.choice(API_KEY_LIST)

    window = MainWindow(apiKey, path)
    window.show()
    sys.exit(app.exec())
