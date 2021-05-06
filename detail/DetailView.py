from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap

from detail.DetailViewModel import DetailViewModel


class DetailView(QWidget):

    def __init__(self):
        super().__init__()

    def initUI(self, pixmap, name):
        # ImageLabel
        pixmap = pixmap.scaledToHeight(150)
        self.imageLabel.setPixmap(pixmap)

        # NameLabel
        self.nameLabel.setText(name)

        # GenresLabel
        self.genresLabel.setText("bla, bla, blaaa")

        # All Movies
        self.moviesTableView
