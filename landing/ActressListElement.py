from PyQt6.QtGui import QIcon, QPixmap


class ActressListElement():
    def __init__(self, name, id, thumbnailData):
        self.pixmap = QPixmap(60, 60)
        QPixmap.loadFromData(self.pixmap, thumbnailData, "JPG")
        self.name = name
        self.id = id
        self.icon = QIcon(self.pixmap)
