from PyQt5 import QtWidgets, QtCore
from ui_views.MainUI import MainUI
from classes.control import Controller
from classes.PyQtGraph import GraphicSystem


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtWidgets.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        ui = MainUI(Controller, GraphicSystem)
        app.mainwindow = ui
        inspect = ui.control
        app.exec_()
        # sys.exit(app.exec_())
