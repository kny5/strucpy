import pyqtgraph as pg
from functions.points_distance import dist_point_line
from classes.geometry import Vector
from PyQt5 import QtGui, QtCore

class GraphicSystem:
    def __init__(self, parent):
        self.selection_ratio = 15
        self.parent = parent
        self.view_layout = pg.GraphicsLayoutWidget()

        self.vLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 255, 255, 100), width=1),
                                     angle=90,
                                     movable=False)
        self.hLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 255, 255, 100), width=1),
                                     angle=0,
                                     movable=False)

        self.plot = pg.PlotCurveItem(
            pen=pg.mkPen(color=(7, 185, 252, 255), width=1),
            antialias=True)

        self.plot_selection = pg.PlotCurveItem(
            antialias=True)

        # self.plot_dots = pg.ScatterPlotItem(
        #     pen=pg.mkPen(color=QtGui.QColor(7, 185, 252, 255)),
        #     brush=pg.mkBrush(color=QtGui.QColor(253, 95, 0, 0)),
        #     antialias=True,
        #     size=10, symbol='o')

        self.graphics = self.view_layout.addViewBox(lockAspect=1, enableMenu=False)
        self.graphics.addItem(self.plot)
        self.graphics.addItem(self.plot_selection)
        # self.graphics.addItem(self.plot_dots)
        # self.graphics.addItem(self.plot_dots_selection)
        self.graphics.addItem(self.vLine, ignoreBounds=True)
        self.graphics.addItem(self.hLine, ignoreBounds=True)
        self.graphics.setBackgroundColor((39, 40, 34, 255))
        self.view_layout.scene().sigMouseMoved.connect(self.cursor_pos)
        self.view_layout.scene().sigMouseClicked.connect(self.check_if_point)

    def cursor_pos(self, cursor):
        maped_pos = self.plot.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)

    def check_if_point(self, cursor):
        if self.parent.control.program.vectors.__len__() > 0:
            if cursor.button() == 1:
                try:
                    _maped_pos = self.plot.mapFromScene(cursor.pos())
                    cursor_pos = (_maped_pos.x(), _maped_pos.y())
                    pixelsize = self.graphics.viewPixelSize()
                except AttributeError:
                    return False
                group = self.parent.control.program.vectors
                selection = self.parent.control.selection
                for vector in group:
                    perpendicular_distance_from_point = dist_point_line(vector.start_2d, vector.end_2d, cursor_pos)
                    if perpendicular_distance_from_point < pixelsize[0] * self.selection_ratio:
                        if vector not in selection:
                            selection.add(vector)
                        else:
                            selection.remove(vector)
                self.show_vector_selection()
            # else:
            #     pass
                # print("right click")

    def show_vectors(self):
        if self.parent.control.program.vectors.__len__() > 0:
            Vector.iso_projection()
            matrix = Vector.process_to_matrix(self.parent.control.program.vectors)
            self.plot.updateData(matrix[:, 0], matrix[:, 1], connect="pairs")
            # plotting dots for node representation, but we need to do this separately
            # dots = unique(matrix, axis=0)
            # self.plot_dots.setData(dots[:, 0], dots[:, 1])
        else:
            self.plot.setData([], [])

    def show_vector_selection(self):
        if self.parent.control.selection.__len__() > 0:
            matrix = Vector.process_to_matrix(self.parent.control.selection, selection=True)
            self.plot_selection.updateData(matrix[:, 0], matrix[:, 1], connect="pairs",
                                           pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5,
                                                        # style=QtCore.Qt.DashLine
                                                        ),
                                           shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 50), width=15))
        else:
            self.plot_selection.setData([], [])

    def rotation(self, direction):
        if direction == QtCore.Qt.Key_Up:
            Vector.alpha += 0.1
        elif direction == QtCore.Qt.Key_Down:
            Vector.alpha -= 0.1
        elif direction == QtCore.Qt.Key_Left:
            Vector.beta -= 0.1
        elif direction == QtCore.Qt.Key_Right:
            Vector.beta += 0.1
        Vector.iso_projection()
        self.show_vectors()
        self.show_vector_selection()
        self.graphics.autoRange(items=[self.plot])