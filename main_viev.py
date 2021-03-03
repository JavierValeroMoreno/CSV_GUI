from load_gui import *
from load_gui import Ui_MainWindow as Load_Window

from make_csv import CSV_List

from column_gui import Ui_MainWindow as Column_Window

from load_model import Load_Model
from column_model import Column_Model

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

window = None
column_w = None
list_csv = None

class MainWindow(QtWidgets.QMainWindow, Load_Window):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.model = Load_Model()
        self.Selected_Files.setModel(self.model)
        self.load_btn.pressed.connect(self.load)
        self.reset_btn.pressed.connect(self.reset)
        self.accept_btn.pressed.connect(self.accept)

    def load(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Seleccione el archivo", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName and not ((False,fileName) in self.model.load):
            self.model.load.append((False,fileName))
            self.model.layoutChanged.emit()
            if not self.accept_btn.isEnabled():
                self.accept_btn.setEnabled(True)

    def reset(self):
        self.model.load.clear()
        self.model.layoutChanged.emit()
        self.accept_btn.setEnabled(False)

    def accept(self):
        global window, column_w, list_csv

        column_w = ColunmWindow(_load = list_csv)
        column_w.show()
        window.hide()

class ColunmWindow(QtWidgets.QMainWindow, Column_Window):
    def __init__(self, *args,_load=None, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.model = Column_Model(load=_load)
        self.back_btn.pressed.connect(self.back)
        self.accept_btn.pressed.connect(self.accept)

    def back(self):
        global window, column_w
        window.show()
        column_w.close()
    
    def accept(self):
        pass
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()