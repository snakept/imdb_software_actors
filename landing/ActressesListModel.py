from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


class ActressesListModel(QAbstractListModel):

    def __init__(self, listData):
        super().__init__()
        self.listData = listData

    def rowCount(self, parent):
        return len(self.listData)

    def data(self, index: QModelIndex, role: int):

        # when the item is for displaying text
        if role == Qt.ItemDataRole.DisplayRole:
            return self.listData[index.row()].name

        # when the item is for displaying icon
        if role == Qt.ItemDataRole.DecorationRole:
            return self.listData[index.row()].icon
