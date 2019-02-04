import pyqtgraph as pg
import numpy as np
from PyQt5 import QtGui, QtCore
from Model.functions.read_dxf import read_dxf
import math
from operator import add
from functools import reduce
from Model.classes.element_types import Vector


def dist(x1, y1, x2, y2, x3, y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1

    sqr_point = px*px + py*py

    u = ((x3 - x1) * px + (y3 - y1) * py) / float(sqr_point)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    distance = math.sqrt(dx*dx + dy*dy)

    return distance


def _cursor(cursor):
    maped_pos = plot_dxf.mapFromScene(cursor)
    x_ = maped_pos.x()
    y_ = maped_pos.y()
    vLine.setPos(x_)
    hLine.setPos(y_)


def check_point(cursor):
    global dxf, vector_set
    _maped_pos = plot_dxf.mapFromScene(cursor.pos())
    _x_ = _maped_pos.x()
    _y_ = _maped_pos.y()
    pixelsize = w1.viewPixelSize()

    for vector in dxf:
        # print("True")
        start = vector.start_2d
        end = vector.end_2d
        # print("False")
        point_toline_mindist = dist(start[0], start[1], end[0], end[1], _x_, _y_)
        # print("maybe")
        if point_toline_mindist < pixelsize[0] * 15:
            vector.clicked()
            # print("clicked ", vector.selected)
            if vector.selected:
                vector_set.add(vector)
            else:
                vector_set.remove(vector)
            # print("setted")
            # print('Eureka!', _x_, _y_)
            # print("listed", vector_list)
            if vector_set.__len__() > 0:
                selected_vector_list = array_vectors_to_plot(vector_set)
                plot_selected.updateData(selected_vector_list[:, 0], selected_vector_list[:, 1],
                                         pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5), connect="pairs")
            else:
                plot_selected.updateData([], [])
            return True


def array_vectors_to_plot(vectors):
    return np.array(reduce(add, [[vector.start_2d, vector.end_2d] for vector in vectors]))


def array_points_to_plot(vectors):
    return list(set([vector.start_2d for vector in vectors] + [vector.end_2d for vector in vectors]))


# def plot_array_from_vectors(vectors):
#    return np.array(list(map(lambda point: np.dot(Vector.last_iso_projection, point),
# reduce(add, [[vector.start, vector.end] for vector in vectors]))))

# def plot_array_from_vectors(vectors):
#     return np.array(list(map(Vector.to_2d, reduce(add, [[vector.start, vector.end] for vector in vectors]))))


def atm_rot(direction):
    global dxf_mapped
    if direction == "up":
        Vector.alpha += 0.1
    elif direction == "down":
        Vector.alpha -= 0.1
    elif direction == "left":
        Vector.beta -= 0.1
    elif direction == "right":
        Vector.beta += 0.1

    Vector.iso_projection()
    dxf_mapped = array_vectors_to_plot(dxf)

    plot_dxf.updateData(
        dxf_mapped[:, 0],
        dxf_mapped[:, 1],
        connect="pairs")

    plot_points.setData(pos=array_points_to_plot(dxf))

    if vector_set.__len__() > 0:
        selected_vectors = array_vectors_to_plot(vector_set)

        plot_selected.updateData(
            selected_vectors[:, 0],
            selected_vectors[:, 1],
            connect="pairs")


class mainwin(QtGui.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super(mainwin, self).__init__()
        # self.setGeometry(300, 300, 250, 150)
        self.show()
        self.keyPressed.connect(self.on_key)

    def keyPressEvent(self, event):
        super(mainwin, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    # def mousePressEvent(self, event):
    #     super(mainwin, self).mousePressEvent(event)
    #     self.keyPressed.emit(event)

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            atm_rot("up")
        elif event.key() == QtCore.Qt.Key_Down:
            atm_rot("down")
        elif event.key() == QtCore.Qt.Key_Left:
            atm_rot("left")
        elif event.key() == QtCore.Qt.Key_Right:
            atm_rot("right")
        if event.key() == QtCore.Qt.Key_Enter:
            atm_rot("up")
            print("hello")# this is called whenever the continue button is presse
        elif event.key() == QtCore.Qt.Key_Q:
            print("Killing")
            self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window

    # @staticmethod
    # def proceed(direction):
    #     # print("Moviendo a " + str(direction))
    #     atm_rot(direction)


app = QtGui.QApplication([])
# app.setOverrideCursor(QtCore.Qt.BlankCursor)
app.setOverrideCursor(QtCore.Qt.CrossCursor)
mw = mainwin()
mw.resize(1024, 768)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
# mw.setWindowOpacity(0.95)
mw.setContentsMargins(-20,-20,-20,-20)
mw.show()
mw.setWindowTitle('Strucpy')
pg.setConfigOptions(antialias=True, useOpenGL=True)
w1 = view.addViewBox(invertY=False, lockAspect=1, enableMouse=True, border=pg.mkPen('k'), enableMenu=False)
w1.setBackgroundColor((33, 33, 33, 255))
w1.enableAutoRange(True)
filename = 'lienzo.dxf'
dxf = read_dxf('c:/repos/strucpy/dev_files/dxf/' + filename)

Vector.iso_projection()
dxf_mapped = array_vectors_to_plot(dxf)

plot_dxf = pg.PlotCurveItem()
plot_dxf.setData(
    dxf_mapped[:, 0],
    dxf_mapped[:, 1],
    connect="pairs",
    antialias=True,
    # setCompositionMode=3,
    pen=pg.mkPen(color=(7, 185, 252, 255), width=2))
#   brush=pg.mkBrush(7, 185, 252, 100)
#   )
w1.addItem(plot_dxf)

vector_set = set([])

plot_selected = pg.PlotCurveItem(
    shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 20), width=15, setCompositionMode=QtGui.QPainter.CompositionMode(2)),
    pen=pg.mkPen(color=QtGui.QColor(100, 185, 252, 50), width=2, style=QtCore.Qt.DashLine))
w1.addItem(plot_selected)

plot_points = pg.ScatterPlotItem(
    pos=array_points_to_plot(dxf),
    pen=pg.mkPen(
        color=QtGui.QColor(57, 255, 20, 200),
        width=2),
    brush=None,
    size=10,
    antialias=True)
w1.addItem(plot_points)

# location = view.addLabel(filename, 1, 0.1)  # check position arguments or any other argument to avoid overlapping
vLine = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
hLine = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
w1.addItem(vLine, ignoreBounds=True)
w1.addItem(hLine, ignoreBounds=True)

view.scene().sigMouseMoved.connect(_cursor)
view.scene().sigMouseClicked.connect(check_point)
# mw.sigMouseClicked.connect(lambda x: print("hello"))


if not __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
