from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys


<<<<<<< HEAD
form_class = uic.loadUiType("PyAutoAli.ui")[0]  # Load the UI


class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
=======
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.OpenFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileBtn.setObjectName("OpenFileBtn")
        self.gridLayout.addWidget(self.OpenFileBtn, 0, 0, 1, 1)
        self.OpenFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.OpenFilePath.setObjectName("OpenFilePath")
        self.gridLayout.addWidget(self.OpenFilePath, 0, 1, 1, 1)
        self.SaveFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SaveFileBtn.setObjectName("SaveFileBtn")
        self.gridLayout.addWidget(self.SaveFileBtn, 1, 0, 1, 1)
        self.SaveFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.SaveFilePath.setInputMask("")
        self.SaveFilePath.setText("")
        self.SaveFilePath.setObjectName("SaveFilePath")
        self.gridLayout.addWidget(self.SaveFilePath, 1, 1, 1, 1)
        self.AutoOpenCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.AutoOpenCheck.setObjectName("AutoOpenCheck")
        self.gridLayout.addWidget(self.AutoOpenCheck, 2, 0, 1, 1)
        self.LinksTxtEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LinksTxtEdit.setObjectName("LinksTxtEdit")
        self.gridLayout.addWidget(self.LinksTxtEdit, 3, 0, 1, 2)
        self.StartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartBtn.setObjectName("StartBtn")
        self.gridLayout.addWidget(self.StartBtn, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.OpenFileBtn.clicked.connect(self.OpenFileClicked()) # type: ignore
        self.SaveFileBtn.clicked.connect(self.SaveToClicked()) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def OpenFileClicked(self):
        pass
>>>>>>> 97429d446adfd24fa3f0214a213f2a06184a3a40

    def SaveToClicked(self):
        pass

    def OpenFileClicked(self):
        pass

app = QApplication(sys.argv)
Window = WindowClass(None)
Window.show()
app.exec_()
