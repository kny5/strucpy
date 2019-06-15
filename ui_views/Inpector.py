import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from numpy import nditer

class App(QWidget):

    def __init__(self, element):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 100
        self.top = 100
        self.top = 100
        self.width = 300
        self.height = 200
        self.data = [data for data in element.data.__dict__.values()]
        self.tableWidgets = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        for data in self.data:
            try:
                for ui in self.tableWidgets:
                    self.layout.addWidget(ui)
                self.createTable(data)
            except:
                pass
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

    def createTable(self, data):
        table = QTableWidget()
        self.tableWidgets.append(table)
        shape = data.shape
        table.setColumnCount(shape[1])
        table.setRowCount(shape[0])
        it = nditer(data, flags=['multi_index'])
        while not it.finished:
            index = it.multi_index
            table.setItem(index[0], index[1], QTableWidgetItem(str(it[0])))
            it.iternext()
        table.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())