from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextList
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListView, QMainWindow
import pandas as pd
import sys


def window(actors, width, height):
    app = QApplication(sys.argv)
    list = QListView()
    list.setWindowTitle("Hello")
    list.setMinimumSize(width, height)

    model = QStandardItemModel(list)

    for actor in actors:
        item = QStandardItem(actor)
        model.appendRow(item)

    list.setModel(model)
    list.show()
    sys.exit(app.exec_())


url = "https://imdb-api.com/en/API/IMDbList/k_vhvsnz5j/ls053501318"
df = pd.read_json(url)

actors = df['items']

actors_list = []
for actor in actors:
    actors_list.append(actor['title'])


window(actors_list, 800, 600)
