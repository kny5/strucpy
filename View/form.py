import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton
sys.path.append('../')
from Model.dataClasses import *

workspace = workspace(100, 100, 100)

node0 = Nodo(20, 30, 14, workspace)
node1 = Nodo(67, 56, 34, workspace)

node0.set_ve(34,34,34,56,56,56)
node1.set_ve(78,78,78,12,12,12)

e1 = Concreto()
e1.set_nodos(node0,node1)

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
    window.setWindowTitle(type(y).__name__ + " " + y.id)
    sys.exit(app.exec_())


windower(workspace)
windower(node0)
windower(node1)
windower(e1)