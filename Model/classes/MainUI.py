import pyqtgraph as pg
from PyQt5 import QtWidgets, QtGui, QtCore
from Model.classes.view import toolbox, Menubar
from Model.classes.control import Controller
from Model.functions.points_distance import dist


class MainUI(QtWidgets.QMainWindow):
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
        self.menubar.actionAbrir_DXF.triggered.connect(self.control.opening_dxf)
        self.menubar.actionGuardar_DXF.triggered.connect(self.control.saving_dxf)
        self.menubar.actionBorrar_Todo.triggered.connect(self.control.deleting_all)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.show()


class GraphicSystem:
    def __init__(self, parent):
        self.parent = parent
        self.view_layout = pg.GraphicsLayoutWidget()

        self.vLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 100), width=1),
                                     angle=90,
                                     movable=False)
        self.hLine = pg.InfiniteLine(pen=pg.mkPen(color=QtGui.QColor(255, 33, 83, 100), width=1),
                                     angle=0,
                                     movable=False)

        self.plot = pg.PlotCurveItem(pen=pg.mkPen(color=(7, 185, 252, 200), width=1),
                                     antialias=True)
        self.plot_selected = pg.PlotCurveItem(shadowPen=pg.mkPen(color=QtGui.QColor(180, 185, 252, 20), width=15),
                                              pen=pg.mkPen(color=QtGui.QColor(100, 185, 252, 50), width=2),
                                              antialias=True)

        self.graphics = self.view_layout.addViewBox(lockAspect=1, enableMenu=False)

        self.graphics.addItem(self.plot)
        self.graphics.addItem(self.vLine, ignoreBounds=True)
        self.graphics.addItem(self.hLine, ignoreBounds=True)

        self.view_layout.scene().sigMouseMoved.connect(self._cursor)

        self.vector_set = set([])

    def _cursor(self, cursor):
        maped_pos = self.plot.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)

    def check_point(self, cursor):

        if cursor.button() == 1:
            try:
                _maped_pos = self.plot.mapFromScene(cursor.pos())
                _x_ = _maped_pos.x()
                _y_ = _maped_pos.y()
                pixelsize = self.graphics.viewPixelSize()
            except AttributeError:
                return

            for vector in self.parent.control.vectors:
                start = vector.start_2d
                end = vector.end_2d
                point_toline_mindist = dist(start[0], start[1], end[0], end[1], _x_, _y_)

                if point_toline_mindist < pixelsize[0] * 15:
                    vector.clicked()
                    if vector.selected:
                        self.vector_set.add(vector)
                    else:
                        self.vector_set.remove(vector)
                    print(self.vector_set)

                else:
                    pass
        else:
            print("right click")


if not __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtGui.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = MainUI()
        # app.exec_()
        sys.exit(app.exec_())