from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class Column_Model(QtCore.QAbstractTableModel):
    def __init__(self, load=None):
        super(Column_Model, self).__init__()
        self.load = load or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._load[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.load)