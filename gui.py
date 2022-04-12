from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys


form_class = uic.loadUiType("PyAutoAli.ui")[0]  # Load the UI


class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def SaveToClicked(self):
        pass

    def OpenFileClicked(self):
        pass

app = QApplication(sys.argv)
Window = WindowClass(None)
Window.show()
app.exec_()
