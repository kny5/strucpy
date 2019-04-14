import pyqtgraph as pg
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog as Qfd
from Model.classes.view import toolbox, Menubar
from Model.classes.control import Controller
from Model.functions.points_distance import dist
from Model.classes.geometry import Vector
from numpy import unique


class MainUI(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super().__init__()
        self.control = Controller(self)
        self.graphicsys = GraphicSystem(self)
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.tools_groupbox = toolbox(self.centralwidget)
        self.horizontalLayout.addWidget(self.tools_groupbox)
        self.horizontalLayout.addWidget(self.graphicsys.view_layout)
        self.setCentralWidget(self.centralwidget)
        # menu bar
        self.menubar = Menubar(self)
        self.menubar.actionAbrir_DXF.triggered.connect(self.control.open_file)
        self.menubar.actionGuardar_DXF.triggered.connect(self.control.save_file)
        # self.menubar.actionBorrar_Todo.triggered.connect(self.control.close_file)
        self.tools_groupbox.elements_groupbox.set_btn_elements.clicked.connect(self.control.program.assemble_elements)
        self.tools_groupbox.run_btn_tools.clicked.connect(self.control.program.run)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.keyPressed.connect(self.on_key)
        self.show()

    def keyPressEvent(self, event):
        super(MainUI, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def on_key(self, event):
        self.graphicsys.rotation(event.key())

    def set_filename(self):
        try:
            file = Qfd.getOpenFileName(self, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.control.filename = file[0]
        except:
            return


class GraphicSystem:
    def __init__(self, parent):
        self.select_vectors = True
        self.parent = parent
        self.view_layout = pg.GraphicsLayoutWidget()

        self.vLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 255, 255, 100), width=1),
                                     angle=90,
                                     movable=False)
        self.hLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 255, 255, 100), width=1),
                                     angle=0,
                                     movable=False)

        self.plot = pg.PlotCurveItem(
            pen=pg.mkPen(color=(7, 185, 252, 255), width=2),
            antialias=True)

        self.plot_selection = pg.PlotCurveItem(
            antialias=True)

        self.plot_dots = pg.ScatterPlotItem(
            pen=pg.mkPen(color=QtGui.QColor(253, 95, 0, 100)),
            brush=pg.mkBrush(color=QtGui.QColor(253, 95, 0, 100)),
            antialias=True,
            size=10, symbol='o')

        self.plot_dots_selection = pg.ScatterPlotItem(
            pen=pg.mkPen(color=QtGui.QColor(253, 95, 0, 200)),
            brush=pg.mkBrush(color=QtGui.QColor(253, 95, 0, 200)),
            antialias=True,
            size=14, symbol='s')

        self.graphics = self.view_layout.addViewBox(lockAspect=1, enableMenu=False)
        self.graphics.addItem(self.plot)
        self.graphics.addItem(self.plot_selection)
        self.graphics.addItem(self.plot_dots)
        self.graphics.addItem(self.plot_dots_selection)
        self.graphics.addItem(self.vLine, ignoreBounds=True)
        self.graphics.addItem(self.hLine, ignoreBounds=True)
        self.graphics.setBackgroundColor((39, 40, 34, 255))

        self.view_layout.scene().sigMouseMoved.connect(self.cursor_pos)
        self.view_layout.scene().sigMouseClicked.connect(self.check_if_point)
        self.vectors_selected_by_click = set([])
        self.elements_select_by_click = set([])
        self.results_layout = None

    def cursor_pos(self, cursor):
        maped_pos = self.plot.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)

    def check_if_point(self, cursor):

        if cursor.button() == 1:
            try:
                _maped_pos = self.plot.mapFromScene(cursor.pos())
                _x_ = _maped_pos.x()
                _y_ = _maped_pos.y()
                pixelsize = self.graphics.viewPixelSize()
            except AttributeError:
                return
            group = self.parent.control.program.vectors
            selection = self.vectors_selected_by_click
            for vector in group:
                start = vector.start_2d
                end = vector.end_2d
                perpendicular_distance_from_point = dist(start[0], start[1], end[0], end[1], _x_, _y_)
                if perpendicular_distance_from_point < pixelsize[0] * 15:
                    if vector not in selection:
                        if self.parent.control.select_vectors:
                            selection.add(vector)
                        else:
                            selection.add(vector)
                            self.parent.control.selected_elements.add(vector.parent)
                    else:
                        if self.parent.control.select_vectors:
                            selection.remove(vector)
                        else:
                            selection.remove(vector)
                            self.parent.control.selected_elements.remove(vector.parent)
                    print(selection)
                    print(self.parent.control.selected_elements)
                    self.show_vector_selection()
                else:
                    pass
        else:
            print("right click")

    def show_results(self):
        self.results_layout = self.view_layout.addLayout()
        self.results_layout.addPlot(row=0, col=0, rowspan=1, colspan=1)
        self.results_layout.addPlot(row=1, col=0, rowspan=1, colspan=1)
        self.results_layout.addPlot(row=2, col=0, rowspan=1, colspan=1)
        self.results_layout.addPlot(row=3, col=0, rowspan=1, colspan=1)

    def show_vectors(self):
        Vector.iso_projection()
        matrix = Vector.process_to_matrix(self.parent.control.program.vectors)
        self.plot.updateData(matrix[:, 0], matrix[:, 1], connect="pairs")
        # plotting dots for node representation, but we need to do this separately
        dots = unique(matrix, axis=0)
        self.plot_dots.setData(dots[:, 0], dots[:, 1])

    def show_vector_selection(self):
        if self.vectors_selected_by_click.__len__() > 0:
            matrix = Vector.process_to_matrix(self.vectors_selected_by_click, selection=True)
            self.plot_selection.updateData(matrix[:, 0], matrix[:, 1], connect="pairs",
                                           pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5,
                                                        # style=QtCore.Qt.DashLine
                                                        ),
                                           shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 50), width=15))
        else:
            self.plot_selection.setData([], [])

    def show_dots(self):
        pass

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
        # print((Vector.alpha, Vector.beta))


if not __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = MainUI()
        sys.exit(app.exec_())
