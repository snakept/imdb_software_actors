from PyQt6 import QtGui
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QListWidgetItem, QVBoxLayout, QWidget
from io import BytesIO


class ActressListElement():
    def __init__(self, name, thumbnailData):
        self.pixmap = QPixmap(60, 60)
        QPixmap.loadFromData(self.pixmap, thumbnailData, "JPG")
        self.name = name
        self.icon = QIcon(self.pixmap)
