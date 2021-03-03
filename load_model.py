from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

class Load_Model(QtCore.QAbstractListModel):
    def __init__(self, *args, load=None, **kwargs):
        super(Load_Model, self).__init__(*args, **kwargs)
        self.load = load or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.load[index.row()]
            return text

    def rowCount(self, index):
        return len(self.load)