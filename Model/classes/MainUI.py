import pyqtgraph as pg
from PyQt5 import QtWidgets, QtGui, QtCore
from Model.classes.view import toolbox, Menubar
from Model.classes.control import Controller


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.control = Controller()
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.tools_groupbox = toolbox(self.centralwidget)
        self.horizontalLayout.addWidget(self.tools_groupbox)
        self.view = pg.GraphicsLayoutWidget()
        self.horizontalLayout.addWidget(self.view)
        self.setCentralWidget(self.centralwidget)
        # menu bar
        self.menubar = Menubar(self)
        self.menubar.actionAbrir_DXF.triggered.connect(self.open_dxf)
        self.menubar.actionGuardar_DXF.triggered.connect(self.save_dxf)
        self.menubar.actionBorrar_Todo.triggered.connect(self.clear_all)
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.show()


if not __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = MainUI()
        # app.exec_()
        sys.exit(app.exec_())