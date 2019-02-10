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

        # self.filename = filename
        self.all_vectors = []
        self.vector_set = set([])
        # self.quit_on_last_window_closed(False)


        self.centralwidget = QtWidgets.QWidget(self)
        self.view = pg.GraphicsLayoutWidget(parent=self.centralwidget)
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)

        self.groupbox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupbox.setMinimumSize(QtCore.QSize(250, 0))
        self.horizontalLayout.addWidget(self.groupbox)
        self.horizontalLayout.addWidget(self.view)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        # menubar

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.actionAbrir_DXF = QtWidgets.QAction(self)
        self.actionAbrir_DXF.setShortcut("Ctrl+O")
        # self.actionAbrir_DXF.triggered.connect(self.open_dxf)
        self.actionGuardar_DXF = QtWidgets.QAction(self)
        self.actionBorrar_Todo = QtWidgets.QAction(self)
        self.menuArchivo.addAction(self.actionAbrir_DXF)
        self.menuArchivo.addAction(self.actionGuardar_DXF)
        self.menuArchivo.addAction(self.actionBorrar_Todo)
        self.menubar.addAction(self.menuArchivo.menuAction())

        #set actions to buttons
        self.actionAbrir_DXF.setShortcut("Ctrl+O")
        self.actionAbrir_DXF.triggered.connect(self.open_dxf)
        self.actionGuardar_DXF.setShortcut("Ctrl+S")
        self.actionGuardar_DXF.triggered.connect(self.save_dxf)
        self.actionBorrar_Todo.triggered.connect(self.clear_all)

        #toolbar
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_7, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_8)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.gridLayout_7.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_8)
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle("")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_4.addWidget(self.radioButton, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setTitle("")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_6.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.gridLayout_6.addWidget(self.label_2, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setTitle("")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_5.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_5.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupbox)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout.addWidget(self.groupbox)
        # self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        # self.horizontalLayout.addWidget(self.openGLWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        # items
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
        self.viewbox = self.view.addViewBox(lockAspect=1,
                                            enableMenu=False)
        self.set_up()
        self.retranslate_ui()

    def open_dxf(self):
        try:
            file = qfd.getOpenFileName(self, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.all_vectors = read_dxf(file[0])
            self.matrix_plot = np.array(reduce(add, [[vector.start, vector.end] for vector in self.all_vectors]))
            Vector.iso_projection()
            self.plot()

        except:
            self.all_vectors = []
            self.matrix_plot = []
            self.plot()

    def save_dxf(self):
        try:
            file = qfd.getSaveFileName(self, "Save DXF", "c:\\", "dxf files (*.dxf)")
            save_dxf(self.all_vectors, file[0])
        except:
            return False


    def clear_all(self):
        self.all_vectors = []
        Vector.alpha = 35
        Vector.beta = 50.3
        Vector.iso_projection()
        self.plot()
        self.plot_select()
        return True

    def set_up(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Strucpy')

        self.keyPressed.connect(self.on_key)
        self.view.scene().sigMouseMoved.connect(self._cursor)
        self.view.scene().sigMouseClicked.connect(self.check_point)

        self.show()
        self.set_viewbox()
        Vector.iso_projection()
        self.plot()

    def xy_vectors_toplot(self, vectors):
        # # return np.array(reduce(add, [[vector.start_2d, vector.end_2d] for vector in vectors]))
        if vectors != self.all_vectors:
            matrix = np.array(reduce(add, [[vector.start, vector.end] for vector in vectors]))
            # print(matrix.shape)
            projection = matrix.dot(Vector.last_iso_projection)
            return projection.dot(Vector.project_plane_matrix)
        else:
            # matrix = Vector.last_iso_projection.dot(self.matrix_plot)
            matrix = self.matrix_plot.dot(Vector.last_iso_projection)
            return matrix.dot(Vector.project_plane_matrix)

    def set_viewbox(self):
        self.viewbox.setBackgroundColor((33, 33, 33, 255))
        # self.viewbox.enableAutoRange(True)
        self.viewbox.addItem(self.plot_dxf)
        self.viewbox.addItem(self.plot_selected)
        # self.viewbox.addItem(self.plot_points)
        self.viewbox.addItem(self.vLine, ignoreBounds=True)
        self.viewbox.addItem(self.hLine, ignoreBounds=True)

    def plot(self):
        if self.vector_set.__len__() < self.all_vectors.__len__() != 0:
            not_selected = self.xy_vectors_toplot(self.all_vectors)
            self.plot_dxf.updateData(
                not_selected[:, 0],
                not_selected[:, 1],
                connect="pairs")
        else:
            self.plot_dxf.setData([], [])
        return

    def plot_select(self):
        # selection = xy_vectors_toplot([vector for vector in self.all_vectors if vector.selected is True])
        if self.vector_set.__len__() > 0:
            selection = self.xy_vectors_toplot(list(self.vector_set))
            self.plot_selected.updateData(
                selection[:, 0],
                selection[:, 1],
                pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5),
                connect="pairs")
        else:
            self.plot_selected.setData([], [])
        # return

    def check_point(self, cursor):
        if cursor.button() == 1:
            try:
                _maped_pos = self.plot_dxf.mapFromScene(cursor.pos())
                _x_ = _maped_pos.x()
                _y_ = _maped_pos.y()
                pixelsize = self.viewbox.viewPixelSize()
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
            self.deleteLater()  # a test I implemented to see if pressing 'Q' would close the window
        return

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupbox.setTitle(_translate("MainWindow", "Tools"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vectors, draw"))
        self.pushButton.setText(_translate("MainWindow", "Edit"))
        self.pushButton_7.setText(_translate("MainWindow", "SET"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Del"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Nodes, forces and DoF"))
        self.pushButton_8.setText(_translate("MainWindow", "Edit"))
        self.pushButton_9.setText(_translate("MainWindow", "SET"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Elements, section and types"))
        self.pushButton_3.setText(_translate("MainWindow", "EDIT"))
        self.pushButton_10.setText(_translate("MainWindow", "SET"))
        self.pushButton_4.setText(_translate("MainWindow", "CONF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Analysis"))
        self.radioButton.setText(_translate("MainWindow", "Analytic"))
        self.radioButton_3.setText(_translate("MainWindow", "B Aprox"))
        self.label_2.setText(_translate("MainWindow", "MAX B"))
        self.radioButton_2.setText(_translate("MainWindow", "MonteCarlo"))
        self.label.setText(_translate("MainWindow", "Iterations"))
        self.pushButton_5.setText(_translate("MainWindow", "Run"))
        self.menuArchivo.setTitle(_translate("MainWindow", "File"))
        self.actionAbrir_DXF.setText(_translate("MainWindow", "Open DXF"))
        self.actionGuardar_DXF.setText(_translate("MainWindow", "Save as DXF"))
        self.actionBorrar_Todo.setText(_translate("MainWindow", "Clear All"))

    # @staticmethod
    # def proceed(direction):
    #     # print("Moviendo a " + str(direction))
    #     atm_rot(direction)


class app(QtGui.QApplication):
    def __init__(self):
        super().__init__([])
        self.setOverrideCursor(QtCore.Qt.CrossCursor)
        self.setQuitOnLastWindowClosed(False)
        self.mainwindow = mainwin()
        # self.exec_()


if not __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app = app()

        app.exec_()
        # sys.exit(app.exec_())
