import pyqtgraph as pg
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog as Qfd
from Model.classes.Views import toolbox, Menubar
from Model.classes.control import Controller
from Model.functions.points_distance import dist_point_line
from Model.classes.geometry import Vector
# from numpy import unique
# from ui_views.vector_edit import Ui_vector_widget


class MainUI(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super().__init__()
        self.uis_vector = set()
        self.uis_element = set()
        self.uis_node = set()
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
        self.menubar.actionClear_select.triggered.connect(self.control.clear_selection)
        self.menubar.actionClose_file.triggered.connect(self.control.close_file)
        # self.tools_groupbox.elements_groupbox.set_btn_elements.clicked.connect(self.control.program.assemble_elements)
        # self.tools_groupbox.vectors_groupbox.edit_btn_vectors.clicked.connect(lambda event: self.control.multiple_views(Ui_vector_widget, self.control.select_vectors))
        self.tools_groupbox.vectors_groupbox.edit_btn_vectors.clicked.connect(self.control.edit_vector)
        self.tools_groupbox.vectors_groupbox.del_btn_vectors.clicked.connect(self.control.del_selection)
        self.tools_groupbox.vectors_groupbox.add_btn_vectors.clicked.connect(self.control.add_vector)
        self.tools_groupbox.nodes_groupbox.set_btn_nodes.clicked.connect(self.control.set_nodes)
        self.tools_groupbox.nodes_groupbox.edit_btn_nodes.clicked.connect(self.control.edit_node)
        # self.tools_groupbox.vectors_groupbox.set_btn_vectors.setDisabled(True)
        self.tools_groupbox.vectors_groupbox.set_btn_vectors.clicked.connect(self.control.set_vectors)
        self.tools_groupbox.elements_groupbox.edit_btn_elements.clicked.connect(self.control.edit_element)


        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.keyPressed.connect(self.on_key)
        self.show()

    def keyPressEvent(self, event):
        super(MainUI, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def on_key(self, event):
        try:
            self.graphicsys.rotation(event.key())
        except:
            pass

    def set_filename(self):
        try:
            file = Qfd.getOpenFileName(self, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.control.filename = file[0]
            return True
        except:
            return False

    def notificator(self, title, message):
        QtWidgets.QMessageBox.about(self, title, message)

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
            pen=pg.mkPen(color=(7, 185, 252, 255), width=2),
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
        else:
            print("right click")

    def show_vectors(self):
        Vector.iso_projection()
        matrix = Vector.process_to_matrix(self.parent.control.program.vectors)
        self.plot.updateData(matrix[:, 0], matrix[:, 1], connect="pairs")
        # plotting dots for node representation, but we need to do this separately
        # dots = unique(matrix, axis=0)
        # self.plot_dots.setData(dots[:, 0], dots[:, 1])

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


if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = QtWidgets.QApplication([])
        app.setOverrideCursor(QtCore.Qt.CrossCursor)
        app.mainwindow = MainUI()
        sys.exit(app.exec_())
