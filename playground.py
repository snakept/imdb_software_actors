from PyQt5.QtGui import QStandardItem, QStandardItemModel, QTextList
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListView, QMainWindow
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

response = requests.get(url)

json_data = response.json() if response and response.status_code == 200 else None

actors = json_data['items']

actors_list = []
for actor in actors:
    actors_list.append(actor['title'])


window(actors_list, 800, 600)
