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


def array_vectors_to_plot(vectors):
    return np.array(reduce(add, [[vector.start_2d, vector.end_2d] for vector in vectors]))


def array_points_to_plot(vectors):
    return list(set([vector.start_2d for vector in vectors] + [vector.end_2d for vector in vectors]))


class mainwin(QtGui.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        # global view
        super(mainwin, self).__init__()
        self.setGeometry(300, 300, 800, 600)
        self.keyPressed.connect(self.on_key)
        # self.resize(1024, 768)
        self.vector_set = set([])
        Vector.iso_projection()
        self.view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
        self.view.scene().sigMouseMoved.connect(self._cursor)
        self.view.scene().sigMouseClicked.connect(self.check_point)
        self.setCentralWidget(self.view)
        # self.setWindowOpacity(0.95)
        self.setContentsMargins(-20, -20, -20, -20)
        self.setWindowTitle('Strucpy')
        self.show()
        self.create_plots()
        self.set_viewbox()
        self.plot()

    def create_plots(self):
        self.vLine = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
        self.hLine = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
        self.plot_dxf = pg.PlotCurveItem(antialias=True, pen=pg.mkPen(color=(7, 185, 252, 255), width=2))
        self.plot_selected = pg.PlotCurveItem(shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 20), width=15),
                                         pen=pg.mkPen(color=QtGui.QColor(100, 185, 252, 50), width=2))
        self.plot_points = pg.ScatterPlotItem(pen=pg.mkPen(color=QtGui.QColor(57, 255, 20, 200), width=2),
                                         brush=None, size=10, antialias=True)

    def set_viewbox(self):
        # global plot_dxf, plot_selected, plot_points, vLine, hLine
        self.viewbox = self.view.addViewBox(invertY=False, lockAspect=1, enableMouse=True, border=pg.mkPen('k'), enableMenu=False)
        self.viewbox.setBackgroundColor((33, 33, 33, 255))
        self.viewbox.enableAutoRange(True)
        self.viewbox.addItem(self.plot_dxf)
        self.viewbox.addItem(self.plot_selected)
        self.viewbox.addItem(self.plot_points)
        self.viewbox.addItem(self.vLine, ignoreBounds=True)
        self.viewbox.addItem(self.hLine, ignoreBounds=True)

    def plot(self):
        filename = 'lienzo.dxf'
        self.dxf = read_dxf('c:/repos/strucpy/dev_files/dxf/' + filename)
        dxf_mapped = array_vectors_to_plot(self.dxf)
        self.plot_dxf.setData(
            dxf_mapped[:, 0],
            dxf_mapped[:, 1],
            connect="pairs")

        self.plot_points.setData(pos=array_points_to_plot(self.dxf))

    def check_point(self, cursor):
        _maped_pos = self.plot_dxf.mapFromScene(cursor.pos())
        _x_ = _maped_pos.x()
        _y_ = _maped_pos.y()
        pixelsize = self.viewbox.viewPixelSize()
        for vector in self.dxf:
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
                    self.vector_set.add(vector)
                else:
                    self.vector_set.remove(vector)
                # print("setted")
                # print('Eureka!', _x_, _y_)
                # print("listed", vector_list)
                if self.vector_set.__len__() > 0:
                    selected_vector_list = array_vectors_to_plot(self.vector_set)
                    self.plot_selected.setData(selected_vector_list[:, 0], selected_vector_list[:, 1],
                                          pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5), connect="pairs",
                                          antialias=True)
                else:
                    self.plot_selected.updateData([], [])
                return True

    def atm_rot(self, direction):

        if direction == "up":
            Vector.alpha += 0.1
        elif direction == "down":
            Vector.alpha -= 0.1
        elif direction == "left":
            Vector.beta -= 0.1
        elif direction == "right":
            Vector.beta += 0.1

        Vector.iso_projection()
        dxf_mapped = array_vectors_to_plot(self.dxf)

        self.plot_dxf.updateData(
            dxf_mapped[:, 0],
            dxf_mapped[:, 1],
            connect="pairs")

        self.plot_points.setData(pos=array_points_to_plot(self.dxf))

        if self.vector_set.__len__() > 0:
            selected_vectors = array_vectors_to_plot(self.vector_set)

            self.plot_selected.updateData(
                selected_vectors[:, 0],
                selected_vectors[:, 1],
                connect="pairs")

    def _cursor(self, cursor):
        maped_pos = self.plot_dxf.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)

    def keyPressEvent(self, event):
        super(mainwin, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def on_key(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.atm_rot("up")
        elif event.key() == QtCore.Qt.Key_Down:
            self.atm_rot("down")
        elif event.key() == QtCore.Qt.Key_Left:
            self.atm_rot("left")
        elif event.key() == QtCore.Qt.Key_Right:
            self.atm_rot("right")
        if event.key() == QtCore.Qt.Key_Enter:
            self.atm_rot("up")
            print("hello")# this is called whenever the continue button is presse
        elif event.key() == QtCore.Qt.Key_Q:
            print("Killing")
            self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window

    # @staticmethod
    # def proceed(direction):
    #     # print("Moviendo a " + str(direction))
    #     atm_rot(direction)
# app = QtGui.QApplication([])
# app.setOverrideCursor(QtCore.Qt.CrossCursor)
# mw = mainwin()
# pg.setConfigOptions(antialias=True, useOpenGL=True)
# Vector.iso_projection()


class app(QtGui.QApplication):
    def __init__(self):
        super().__init__([])
        self.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.mainwindow = mainwin()


if not __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = app()
        app.exec_()
