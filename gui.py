from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5 import uic
import sys
from PyAutoAli import *
import os

form_class = uic.loadUiType("PyAutoAli.ui")[0]  # Load the UI

class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.sleepspinBox.setValue(pyAuto.timesleep)
        self.imagesspinBox.setValue(pyAuto.maximages)
        self.openfile=""
        self.savefile=""

    def StartClicked(self):
        if (self.openfile != "" or self.LinksTxtEdit.toPlainText()!="Here will be your links") and self.savefile != "":
            try:
                file = self.LinksTxtEdit.toPlainText()
                lines = file.split('\n')
                print(lines)
                self.progressBar.setValue(0)
                self.progressBar.setMaximum(len(lines))
                for url in lines:
                    pyAuto.checkurl(url)
                    self.progressBar.setValue(self.progressBar.value()+1)
                pyAuto.savefile(self.savefile)
                if self.AutoOpenCheck.isChecked():
                    os.system(self.savefile)
            except Exception as e:
                raise
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Not open path or save path!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def SaveToClicked(self):
        try:
            if self.openfile=="":
                self.openfile="file.txt"
            self.savefile, _ = QFileDialog.getSaveFileName(self, 'Save to', self.openfile[:-3]+"csv", "CSV files (*.csv)")
            self.SaveFilePath.setText(self.savefile)
        except Exception as e:
            raise

    def OpenFileClicked(self):
        try:
            self.openfile, _ = QFileDialog.getOpenFileName(self, 'Links', r"", "Text files (*.txt)")
            self.OpenFilePath.setText(self.openfile)
            self.LinksTxtEdit.setPlainText("")
            if self.openfile != "":
                with open(self.openfile) as file:
                    for url in file:
                        self.LinksTxtEdit.appendPlainText(url)
        except Exception as e:
            raise

    def sleepChanged(self, value):
        pyAuto.setSettings("timesleep", value)

    def imagesChanged(self, value):
        pyAuto.setSettings("maximages", value)

pyAuto = PyAutoAli()
app = QApplication(sys.argv)
Window = WindowClass(None)
Window.show()
app.exec_()
