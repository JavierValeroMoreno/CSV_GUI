# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 200))
        self.centralwidget.setMaximumSize(QtCore.QSize(350, 200))
        self.centralwidget.setObjectName("centralwidget")
        self.Selected_Files = QtWidgets.QListView(self.centralwidget)
        self.Selected_Files.setGeometry(QtCore.QRect(90, 10, 256, 192))
        self.Selected_Files.setObjectName("Selected_Files")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(5, 10, 80, 23))
        self.load_btn.setObjectName("load_btn")
        self.accept_btn = QtWidgets.QPushButton(self.centralwidget)
        #!/usr/bin
        self.accept_btn.setGeometry(QtCore.QRect(5, 40, 80, 23))
        self.accept_btn.setMouseTracking(False)
        self.accept_btn.setObjectName("accept_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(5, 70, 80, 23))
        self.reset_btn.setObjectName("reset_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_btn.setText(_translate("MainWindow", "Load"))
        self.accept_btn.setText(_translate("MainWindow", "Accept"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

