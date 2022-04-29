import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5 import uic, QtGui
from PyAutoAli import *

form_class = uic.loadUiType("PyAutoAli.ui")[0]  # Load the UI

class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.sleepspinBox.setValue(pyAuto.timesleep)
        self.imagesspinBox.setValue(pyAuto.maximages)
        self.openfile=""
        self.savefile=""

    def start_clicked(self):
        if ((self.openfile != ""
            or self.LinksTxtEdit.toPlainText()!="Here will be your links")
            and self.savefile != ""):
            try:
                file = self.LinksTxtEdit.toPlainText()
                lines = file.split('\n')
                self.progressBar.setValue(0)
                self.progressBar.setMaximum(len(lines))
                for url in lines:
                    pyAuto.check_url(url)
                    self.progressBar.setValue(self.progressBar.value()+1)
                pyAuto.save_file(self.savefile)
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

    def save_to_clicked(self):
        try:
            if self.openfile=="":
                self.openfile="file.txt"
            self.savefile, _ = QFileDialog.getSaveFileName(self,
                                                           'Save to',
                                                           self.openfile[:-3]+"csv",
                                                           "CSV files (*.csv)")
            self.SaveFilePath.setText(self.savefile)
        except Exception as e:
            raise

    def open_file_clicked(self):
        try:
            self.openfile, _ = QFileDialog.getOpenFileName(self,
                                                           'Links',
                                                           r"",
                                                           "Text files (*.txt)")
            self.OpenFilePath.setText(self.openfile)
            self.LinksTxtEdit.setPlainText("")
            if self.openfile != "":
                with open(self.openfile) as file:
                    for url in file:
                        self.LinksTxtEdit.appendPlainText(url)
        except Exception as e:
            raise

    def sleep_changed(self, value):
        pyAuto.set_settings("timesleep", value)

    def images_changed(self, value):
        pyAuto.set_settings("maximages", value)

pyAuto = PyAutoAli()
app = QApplication(sys.argv)
Window = WindowClass(None)
Window.show()
app.exec_()
