import typing
from PyQt6 import QtCore
import PyQt6
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant
from PyQt6.QtWidgets import QLabel

from ActressListElement import ActressListElement


class ActressesListModel(QAbstractListModel):

    def __init__(self, listData):
        super().__init__()
        self.listData = listData

    def rowCount(self, parent):
        return len(self.listData)

    def data(self, index: QModelIndex, role: int):

        if role == Qt.ItemDataRole.DisplayRole:
            return self.listData[index.row()].name

        if role == Qt.ItemDataRole.DecorationRole:
            return self.listData[index.row()].icon