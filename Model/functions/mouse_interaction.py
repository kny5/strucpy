import pyqtgraph as pg
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from Model.functions.read_dxf import read_dxf, save_dxf
import math
from operator import add
from functools import reduce
from Model.classes.geometry import Vector
# from ui_views.Vectoreditor import Ui_Form as vectoredit
from ui_views.addvector import edit_vector
from PyQt5.QtWidgets import QFileDialog as qfd
from Model.classes.view import toolbox, menubar


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


def points_to_plot(vectors):
    return list(set([vector.start_2d for vector in vectors] + [vector.end_2d for vector in vectors]))


class mainwin(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super().__init__()

        self.all_vectors = []
        self.vector_set = set([])

        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.tools_groupbox = toolbox(self.centralwidget)
        self.horizontalLayout.addWidget(self.tools_groupbox)
        self.view = pg.GraphicsLayoutWidget()
        self.horizontalLayout.addWidget(self.view)
        self.setCentralWidget(self.centralwidget)
        # menu bar
        self.menubar = menubar(self)
        self.menubar.actionAbrir_DXF.triggered.connect(self.open_dxf)
        self.menubar.actionGuardar_DXF.triggered.connect(self.save_dxf)
        self.menubar.actionBorrar_Todo.triggered.connect(self.clear_all)
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.vLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 100), width=1),
                                     angle=90,
                                     movable=False)
        self.hLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 100), width=1),
                                     angle=0,
                                     movable=False)
        self.plot_dxf = pg.PlotCurveItem(pen=pg.mkPen(color=(7, 185, 252, 200), width=1),
                                         antialias=True)
        self.plot_selected = pg.PlotCurveItem(shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 20), width=15),
                                              pen=pg.mkPen(color=QtGui.QColor(100, 185, 252, 50), width=2),
                                              antialias=True)
        # self.plot_points = pg.ScatterPlotItem(pen=pg.mkPen(color=QtGui.QColor(57, 255, 20, 200), width=2),
        #                                       brush=None,
        #                                       size=10,
        #                                       antialias=True)
        # self.view_layout = self.view.addLayout(row=2, col=2, rowspan=1)
        self.graphics = self.view.addViewBox(lockAspect=1, enableMenu=False)
        # self.graphics = self.view_layout.addViewBox(lockAspect=1, enableMenu=False)
        # self.props_text = self.view_layout.addPlot()
        # text = "Lorem Ipsum is sim "
        # self.viewbox_info = self.view_layout.addLabel(text, row=1, col=0)

        self.set_up()
        self.retranslate_ui()

    def open_dxf(self):
        try:
            file = qfd.getOpenFileName(self, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.all_vectors = read_dxf(file[0])
            self.matrix_plot = np.array(reduce(add, [[vector.start, vector.end] for vector in self.all_vectors]))
            Vector.alpha = 35
            Vector.beta = 50.3
            Vector.iso_projection()
            self.plot()
        except:
            return

    def save_dxf(self):
        try:
            file = qfd.getSaveFileName(self, "Save DXF", "c:\\", "dxf files (*.dxf)")
            save_dxf(self.all_vectors, file[0])
        except:
            return

    def clear_all(self):
        self.all_vectors = []
        self.vector_set = set([])
        Vector.iso_projection()
        self.plot()
        self.plot_select()
        return

    def set_up(self):
        self.setGeometry(300, 300, 800, 600)
        self.keyPressed.connect(self.on_key)
        self.view.scene().sigMouseMoved.connect(self._cursor)
        self.view.scene().sigMouseClicked.connect(self.check_point)

        self.show()
        self.set_viewbox()
        Vector.iso_projection()
        self.plot()

    def xy_vectors_toplot(self, vectors):
        if vectors != self.all_vectors:
            matrix = np.array(reduce(add, [[vector.start, vector.end] for vector in vectors]))
            projection = matrix.dot(Vector.last_iso_projection)
            return projection.dot(Vector.project_plane_matrix)
        else:
            matrix = self.matrix_plot.dot(Vector.last_iso_projection)
            return matrix.dot(Vector.project_plane_matrix)

    def set_viewbox(self):
        self.graphics.setBackgroundColor((33, 33, 33, 255))
        # self.graphics.enableAutoRange(True)
        self.graphics.addItem(self.plot_dxf)
        self.graphics.addItem(self.plot_selected)
        # self.graphics.addItem(self.plot_points)
        self.graphics.addItem(self.vLine, ignoreBounds=True)
        self.graphics.addItem(self.hLine, ignoreBounds=True)

    def plot(self):
        if self.vector_set.__len__() < self.all_vectors.__len__() != 0:
            __vectors = self.xy_vectors_toplot(self.all_vectors)
            self.plot_dxf.updateData(
                __vectors[:, 0],
                __vectors[:, 1],
                connect="pairs")
        else:
            self.plot_dxf.setData([], [])
        return

    def plot_it(self):
        return

    def plot_select(self):
        if self.vector_set.__len__() > 0:
            selection = self.xy_vectors_toplot(list(self.vector_set))
            self.plot_selected.updateData(
                selection[:, 0],
                selection[:, 1],
                pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5),
                connect="pairs")
        else:
            self.plot_selected.setData([], [])
        return

    def check_point(self, cursor):
        if cursor.button() == 1:
            try:
                _maped_pos = self.plot_dxf.mapFromScene(cursor.pos())
                _x_ = _maped_pos.x()
                _y_ = _maped_pos.y()
                pixelsize = self.graphics.viewPixelSize()
            except AttributeError:
                return

            for vector in self.all_vectors:
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
                    return
                else:
                    pass
        else:
            print("right click")

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
        return

    def keyPressEvent(self, event):
        super(mainwin, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def vector_widget(self, vector):
        self.form = QtWidgets.QWidget()
        self.ui = edit_vector(vector)
        self.ui.setupUi(self.form)
        self.form.show()

    def on_key(self, event):
        self.atm_rot(event.key())

        if event.key() == QtCore.Qt.Key_Enter:
            if self.vector_set.__len__() == 1:
                self.vector_widget(list(self.vector_set)[0])

            elif self.vector_set.__len__() == 0:
                self.vector_widget(Vector((0,0,0), (1,1,1)))
                print("Sin seleccion")
            else:
                print("Seleccione sólo un vector")

        elif event.key() == QtCore.Qt.Key_Q:
            print("Killing")
            self.deleteLater()
        return

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", 'Strucpy   v0.1    [alpha]'))

    # @staticmethod
    # def proceed(direction):
    #     # print("Moviendo a " + str(direction))
    #     atm_rot(direction)


if not __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = mainwin()
        # app.exec_()
        sys.exit(app.exec_())
