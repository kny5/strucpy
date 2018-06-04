import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QHBoxLayout, QLineEdit, QPushButton, QDialogButtonBox
from PyQt5 import QtCore
sys.path.append('../')
from Model.dataClasses import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.form_layout = QFormLayout()
        self.init_ui()

    def init_ui(self):
        self.setLayout(self.form_layout)
        self.setWindowTitle("Editor de elementos")
        self.setGeometry(300,300,400,0)
        self.form_layout.addRow(QLabel("Propiedad"), QLabel("Valor"))
        self.show()


app = QApplication(sys.argv)
window = MainWindow()


y = Or()


for key, value in y.__dict__.items():
    if type(value) != list:
        window.form_layout.addRow(QLabel(key), QLineEdit(str(value)))
    else:
        for item in value:
            window.form_layout.addRow(QLabel(key), QLineEdit(str(item)))

window.form_layout.addRow(QLabel("hola"), QPushButton("Guardar"))

sys.exit(app.exec_())

