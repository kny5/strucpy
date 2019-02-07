import pyqtgraph as pg
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from Model.functions.read_dxf import read_dxf
import math
from operator import add
from functools import reduce
from Model.classes.geometry import Vector
# from ui_views.Vectoreditor import Ui_Form as vectoredit
from ui_views.addvector import edit_vector


def dist(x1, y1, x2, y2, x3, y3):  # x3,y3 is the point
    px = x2 - x1
    py = y2 - y1

    sqr_point = px * px + py * py

    u = ((x3 - x1) * px + (y3 - y1) * py) / float(sqr_point)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def xy_vectors_toplot(vectors):
    if vectors.__len__() > 0:
        return np.array(reduce(add, [[vector.start_2d, vector.end_2d] for vector in vectors]))
    elif vectors.__len__() == 1:
        return np.array([vector.start, vector.end] for vector in vectors)
    else:
        return []


def points_to_plot(vectors):
    return list(set([vector.start_2d for vector in vectors] + [vector.end_2d for vector in vectors]))


class mainwin(QtGui.QMainWindow):

    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self, filename):
        # global view
        super().__init__()

        self.filename = filename
        self.dxf = read_dxf(self.filename)
        self.setGeometry(300, 300, 800, 600)
        self.keyPressed.connect(self.on_key)
        # self.resize(1024, 768)
        self.vector_set = set([])
        Vector.iso_projection()
        self.view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
        self.view.scene().sigMouseMoved.connect(self._cursor)
        self.view.scene().sigMouseClicked.connect(self.check_point)
        self.setCentralWidget(self.view)
        # self
        # self.setWindowOpacity(0.95)
        self.setContentsMargins(-20,-20,-20,-20)
        self.setWindowTitle('Strucpy')
        self.show()
        self.create_items()
        self.set_viewbox()
        self.plot()
        # self.menubar = self.menuBar()
        # self.menubar.addMenu('&DRAW')
        # self.menubar.addAction('&Open DXF')
        # self.toolbox = QtWidgets.QToolBox(self)
        # self.addmenu_entry()

    def addmenu_entry(self):
        self.menubar.addMenu('&admin')

    def create_items(self):
        self.vLine = pg.InfiniteLine(angle=90, movable=False,
                                     pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
        self.hLine = pg.InfiniteLine(angle=0, movable=False,
                                     pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 255), width=1))
        self.plot_dxf = pg.PlotCurveItem(antialias=True, pen=pg.mkPen(color=(7, 185, 252, 255), width=2))
        self.plot_selected = pg.PlotCurveItem(shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 20), width=15),
                                              pen=pg.mkPen(color=QtGui.QColor(100, 185, 252, 50), width=2), antialias=True)
        self.plot_points = pg.ScatterPlotItem(pen=pg.mkPen(color=QtGui.QColor(57, 255, 20, 200), width=2),
                                              brush=None, size=10, antialias=True)

    def set_viewbox(self):
        self.viewbox = self.view.addViewBox(invertY=False, lockAspect=1, enableMouse=True, border=pg.mkPen('k'),
                                            enableMenu=False)
        self.viewbox.setBackgroundColor((33, 33, 33, 255))
        self.viewbox.enableAutoRange(True)
        self.viewbox.addItem(self.plot_dxf)
        self.viewbox.addItem(self.plot_selected)
        self.viewbox.addItem(self.plot_points)
        self.viewbox.addItem(self.vLine, ignoreBounds=True)
        self.viewbox.addItem(self.hLine, ignoreBounds=True)

    def plot(self):
        not_selected = xy_vectors_toplot(self.dxf)
        if not_selected.__len__() > 0:
            self.plot_dxf.updateData(
                not_selected[:, 0],
                not_selected[:, 1],
                connect="pairs")
        else:
            self.plot_dxf.setData([], [])
        # self.plot_points.setData(pos=points_to_plot(self.dxf))
        # return

    def plot_select(self):
        # selection = xy_vectors_toplot([vector for vector in self.dxf if vector.selected is True])
        selection = xy_vectors_toplot(list(self.vector_set))
        if selection.__len__() > 0:
            self.plot_selected.updateData(
                selection[:, 0],
                selection[:, 1],
                pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5),
                connect="pairs",
                antialias=True)
        else:
            self.plot_selected.setData([], [])
        # self.plot_points.setData(pos=points_to_plot(self.dxf))
        # return

    def check_point(self, cursor):
        _maped_pos = self.plot_dxf.mapFromScene(cursor.pos())
        _x_ = _maped_pos.x()
        _y_ = _maped_pos.y()
        pixelsize = self.viewbox.viewPixelSize()
        for vector in self.dxf:
            start = vector.start_2d
            end = vector.end_2d
            point_toline_mindist = dist(start[0], start[1], end[0], end[1], _x_, _y_)

            if point_toline_mindist < pixelsize[0] * 15:
                vector.clicked()
                if vector.selected:
                    self.vector_set.add(vector)
                else:
                    self.vector_set.remove(vector)

                self.plot()
                self.plot_select()

                break
            else:
                pass

    def atm_rot(self, direction):

        if direction == QtCore.Qt.Key_Up:
            Vector.alpha += 0.1
        elif direction == QtCore.Qt.Key_Down:
            Vector.alpha -= 0.1
        elif direction == QtCore.Qt.Key_Left:
            Vector.beta -= 0.1
        elif direction == QtCore.Qt.Key_Right:
            Vector.beta += 0.1

        Vector.iso_projection()
        self.plot()
        self.plot_select()

    def _cursor(self, cursor):
        maped_pos = self.plot_dxf.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)
        # return

    def keyPressEvent(self, event):
        super(mainwin, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def vector_widget(self, vector):
        self.form = QtWidgets.QWidget()
        self.ui = edit_vector(vector)
        self.ui.setupUi(self.form)
        self.form.show()

    def on_key(self, event):
        # if event.key() == QtCore.Qt.Key_Up:
        #     self.atm_rot("up")
        # elif event.key() == QtCore.Qt.Key_Down:
        #     self.atm_rot("down")
        # elif event.key() == QtCore.Qt.Key_Left:
        #     self.atm_rot("left")
        # elif event.key() == QtCore.Qt.Key_Right:
        #     self.atm_rot("right")

        self.atm_rot(event.key())

        if event.key() == QtCore.Qt.Key_Enter:
            if self.vector_set.__len__() == 1:
                self.vector_widget(list(self.vector_set)[0])

            elif self.vector_set.__len__() == 0:
                self.vector_widget(Vector((0,0,0), (1,1,1)))
                print("Sin seleccion")
            else:
                print("Seleccione sólo un vector")

            # print("hello")  # this is called whenever the continue button is presse
        elif event.key() == QtCore.Qt.Key_Q:
            print("Killing")
            self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window
        return
    # @staticmethod
    # def proceed(direction):
    #     # print("Moviendo a " + str(direction))
    #     atm_rot(direction)


class app(QtGui.QApplication):
    def __init__(self, filename):
        super().__init__([])
        self.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.mainwindow = mainwin(filename)
        self.exec_()

# if not __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         app = app()
#         app.exec_()
