import pyqtgraph as pg
import numpy as np
from PyQt5 import QtGui, QtCore


app = QtGui.QApplication([])
app.setOverrideCursor(QtCore.Qt.CrossCursor)
mw = QtGui.QMainWindow()
mw.resize(800, 800)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Strucpy')
pg.setConfigOptions(antialias=True, useOpenGL=True)
# pg.setConfigOption('useOpenGL', True)
# pg.setConfigOption('antialias', True)
w1 = view.addViewBox(invertY=False, lockAspect=1, enableMouse=True, border=pg.mkPen(None))
w1.setAspectLocked(True)
# mw.setContentsMargins(-50,-50,-50,-50)
# mw.unsetCursor()

s4 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 20))
w1.addItem(s4)
# w1.addItem(pg.GraphicsItem())

view.nextColumn()
location = view.addLabel("3D Grphics", 1, 0.1)  # check position arguments or any other argument to avoid overlapping
# view.nextColumn()
# objects_selector = view.addLabel(0, 2)
# txt = pg.TextItem("[0,0,0,2,2,2]",anchor=(1,1,1))
# w1.addItem(txt)
# s5 = pg.CrosshairROI(movable=False, scaleSnap=False, rotateSnap=False, snapSize=None)
# s6 = pg.ArrowItem()

# a = np.array([[1, 0], [0, -1]])
# b = lambda cursor_: np.array([cursor_.x(), cursor_.y() - 800]).dot(a)
# d = lambda dot: s4.addPoints(x=np.array([dot.x()]), y=np.array([dot.y()]))

# vLine = pg.InfiniteLine(angle=90, movable=False, label="Seleccione Elemento:")
# hLine = pg.InfiniteLine(angle=0, movable=False)
# w1.addItem(vLine, ignoreBounds=True)
# w1.addItem(hLine, ignoreBounds=True)


def cursor_reflector(cursor):
    mat_reflex = np.array([[1, 0], [0, -1]])
    reflection = np.array([cursor.x(), cursor.y()]).dot(mat_reflex)
    return reflection


def roi_cursor(cursor):
    # pos = cursor.pos()
    # maped_pos = w1.mapFromViewToItem(s4, cursor)
    maped_pos = s4.mapFromScene(cursor)
    # reflex = cursor_reflector(maped_pos)
    # reflex = (maped_pos.x(), maped_pos.y())
    # local_ = w1.mapFromViewToItem(w1.cursor, s4)
    # print(local_)
    x_ = maped_pos.x()
    y_ = maped_pos.y()
    # print(x_, y_)  # test
    # maped_pos = w1.mapFromViewToItem(s4, w1.cursor().pos())
    # print("maped", maped_pos.x(), maped_pos.y()) # test
    # vLine.setPos(x_)
    # hLine.setPos(y_)
    # s5.setPos((x_, y_))
    s4.addPoints(x=np.array([x_]), y=np.array([y_]))
    # location.setText(str((x_, y_)))
    # objects_selector.setText("Seleccionado: " )
    # txt.setAnchor(s4.mapFromView(view.cursor().pos()))
    # view.cursor().setPos(x_, y_)
    # return s4.addPoints(x=np.array([cursor[0]], y=np.array([cursor[1]])))


# pg.SignalProxy(w1.scene().sigMouseMoved, rateLimit=60, slot=d)
# w1.addItem(s5)

view.scene().sigMouseMoved.connect(roi_cursor)

# w1.setLeftButtonAction()
# w1.scene().sigMouseMoved.connect(roi_cursor)

# Start Qt event loop unless running in interactive mode or using pyside.

if not __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
