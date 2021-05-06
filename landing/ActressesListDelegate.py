from PyQt6.QtWidgets import QItemDelegate
from PyQt6.QtCore import QSize


class ActressesListDelegate(QItemDelegate):

    def paint(self, painter, option, index):
        pass

    def sizeHint(self, option, index):
        return QSize(300, 100)
