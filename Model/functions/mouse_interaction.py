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


def isometric_projection_var_angle(point, _alpha, _beta):
    calpha = math.cos(_alpha)
    salpha = math.sin(_alpha)
    cbeta = math.cos(_beta)
    sbeta = math.sin(_beta)
    _tranform_a = np.array([[1, 0, 0],
                            [0, calpha, salpha],
                            [0, -salpha, calpha]])
    _tranform_b = np.array([[cbeta, 0, -sbeta],
                            [0, 1, 0],
                            [sbeta, 0, cbeta]])
    _tranform_c = _tranform_a.dot(_tranform_b)
    _x_y = np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 0]])
    _isoproject_a = _tranform_c.dot(point)
    _isoproject_b = _isoproject_a.dot(_x_y)
    return np.array([_isoproject_b[0], _isoproject_b[1]])


def yaxis_reflector(point):
    mat_reflex = np.array([[1, 0], [0, -1]])
    reflection = np.array([point[0], point[1]]).dot(mat_reflex)
    return reflection


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

    # print("#"*10, pixelsize)
    # print(_x_, _y_)
    # print("True")

    for vector in dxf[1]:
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

            vector_list = list(vector_set)
            # print("listed", vector_list)
            # print(vector.start_2d[0])
            if vector_list.__len__() > 0:
                x_vector_list = reduce(add, [[vector.start_2d[0], vector.end_2d[0]] for vector in vector_list])
                y_vector_list = reduce(add, [[vector.start_2d[1], vector.end_2d[1]] for vector in vector_list])
                plot_selected.updateData(np.array(x_vector_list), np.array(y_vector_list),
                                         pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5), connect="pairs")
            else:
                plot_selected.updateData([], [])
            return True
        # if _counter % 2 == 0:
        #     _p2_ = dxf_mapped[_counter + 1]
        #     x1, y1 = _p1_[0], _p1_[1]
        #     x2, y2 = _p2_[0], _p2_[1]
        #
        #     point_toline_mindist = dist(x1, y1, x2, y2, _x_, _y_)
        #
        #     if point_toline_mindist < pixelsize[0] * 15:
        #         print('Eureka!', _x_, _y_)
        #
        #         x_selected_vectors += [x1, x2]
        #         y_selected_vectors += [y1, y2]
        #
        #         plot_selected.updateData(np.array(x_selected_vectors), np.array(y_selected_vectors),
        #                                  pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5), connect="pairs")
        #
        #         return True


def atm_rot(direction):
    global dxf_mapped, x_selected_vectors, y_selected_vectors
    if direction == "up":
        Vector.alpha += 0.1
    elif direction == "down":
        Vector.alpha -= 0.1
    elif direction == "left":
        Vector.beta -= 0.1
    elif direction == "right":
        Vector.beta += 0.1
    # dxf_mapped = np.array([isometric_projection_var_angle(_point, alpha, beta) for _point in dxf[0]])
    dxf_mapped = plot_array_from_vectors(dxf[1])
    plot_dxf.updateData(dxf_mapped[:, 0], dxf_mapped[:, 1], connect="pairs")

    vector_list = list(vector_set)
    x_vector_list = reduce(add, [[vector.start_2d[0], vector.end_2d[0]] for vector in vector_list])
    y_vector_list = reduce(add, [[vector.start_2d[1], vector.end_2d[1]] for vector in vector_list])

    plot_selected.updateData(
        np.array(x_vector_list),
        np.array(y_vector_list),
        pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5),
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

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.proceed("up")
        elif event.key() == QtCore.Qt.Key_Down:
            self.proceed("down")
        elif event.key() == QtCore.Qt.Key_Left:
            self.proceed("left")
        elif event.key() == QtCore.Qt.Key_Right:
            self.proceed("right")
        # if event.key() == QtCore.Qt.Key_Enter and self.ui.continueButton.isEnabled():
        #     self.proceed()  # this is called whenever the continue button is pressed

        # elif event.key() == QtCore.Qt.Key_Q:
        #     print("Killing")
        #     self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window
    @staticmethod
    def proceed(direction):
        # print("Moviendo a " + str(direction))
        atm_rot(direction)


app = QtGui.QApplication([])
# app.setOverrideCursor(QtCore.Qt.BlankCursor)
app.setOverrideCursor(QtCore.Qt.CrossCursor)
mw = mainwin()
mw.resize(800, 800)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('Strucpy')
pg.setConfigOptions(antialias=True, useOpenGL=True)
w1 = view.addViewBox(invertY=False, lockAspect=1, enableMouse=True, border=pg.mkPen('k'), enableMenu=False)
w1.setBackgroundColor((33, 33, 33, 255))
w1.enableAutoRange(True)
filename = 'lienzo.dxf'
dxf = read_dxf('c:/repos/strucpy/dev_files/dxf/' + filename)
# alpha = 35
# beta = 45

# dxf_mapped_old = np.array([isometric_projection_var_angle(_point, alpha, beta) for _point in dxf[0]])
# dxf_vectors = dxf[1]


def plot_array_from_vectors(vectors):
    return np.array(reduce(add, [vector.iso_projection for vector in vectors]))


dxf_mapped = plot_array_from_vectors(dxf[1])

plot_dxf = pg.PlotCurveItem()
plot_dxf.setData(
    dxf_mapped[:, 0],
    dxf_mapped[:, 1],
    connect="pairs",
    antialias=True,
    # setCompositionMode=3,
    pen=pg.mkPen(color=(7, 185, 252, 255), width=2),
    brush=pg.mkBrush(7, 185, 252, 100))
w1.addItem(plot_dxf)

x_selected_vectors = []
y_selected_vectors = []
vector_set = set([])

plot_selected = pg.PlotCurveItem()
w1.addItem(plot_selected)

location = view.addLabel(filename, 1, 0.1)  # check position arguments or any other argument to avoid overlapping
vLine = pg.InfiniteLine(angle=90, movable=False, pen='y')
hLine = pg.InfiniteLine(angle=0, movable=False, pen='y')
w1.addItem(vLine, ignoreBounds=True)
w1.addItem(hLine, ignoreBounds=True)

view.scene().sigMouseMoved.connect(_cursor)
view.scene().sigMouseClicked.connect(check_point)


if not __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
