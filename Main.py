from PyQt5 import QtWidgets, QtCore
from ui_views.MainUI import MainUI

if __name__ == '__main__':
    import sys
    import os
    print(os.path.dirname(sys.argv[0]))
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtWidgets.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = MainUI()
        sys.exit(app.exec_())
