# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'column_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 234)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.accept_btn = QtWidgets.QPushButton(self.centralwidget)
        self.accept_btn.setGeometry(QtCore.QRect(0, 10, 80, 23))
        self.accept_btn.setObjectName("accept_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(0, 40, 80, 23))
        self.back_btn.setObjectName("back_btn")
        self.listView = QtWidgets.QTableWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(90, 10, 256, 192))
        self.listView.setObjectName("listView")
        self.listView.setColumnCount(0)
        self.listView.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.accept_btn.setText(_translate("MainWindow", "Accept"))
        self.back_btn.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

