import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton
sys.path.append('../')
from Model.Classes import *

e1 = Concreto()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.form_layout = QFormLayout()

        self.init_ui()

    def init_ui(self):
        i = 0
        self.setLayout(self.form_layout)

        self.setGeometry(300, 300, 320, 0)

        self.show()


def windower(y):

    app = QApplication(sys.argv)
    window = MainWindow()

    window.form_layout.addRow(QLabel("Propiedad"), QLabel("Valor"))

    for key, value in y.__dict__.items():
        while type(value) != list and type(value) != str:
            try:
                window.form_layout.addRow(QLabel(key + "            "), QLineEdit(str(value)))
                break
            except:
                pass

    window.form_layout.addRow(QWidget(), QPushButton("Guardar"))
    window.setWindowTitle(type(y).__name__ + " " + y.e_id)
    sys.exit(app.exec_())

windower(e1)