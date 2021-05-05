from PyQt6.QtCore import QAbstractItemModel, QModelIndex


class DetailViewModel(QAbstractItemModel):

    def __init__(self):
        super().__init__()

    def rowCount(self, parent):
        return 4

    def columnCount(self, parent):
        return 4

    def index(self, row, column, parent):
        return QModelIndex()
