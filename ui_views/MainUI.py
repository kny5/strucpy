from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog as Qfd
from ui_views.Views import toolbox, Menubar
from classes.control import Controller
from classes.PyQtGraph import GraphicSystem
# from numpy import unique
# from ui_views.vector_edit import Ui_vector_widget


class MainUI(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("strucpy_icon.png")))
        self.setWindowTitle("Strucpy Alpha v0.1")
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
        # self.tools_groupbox.vectors_groupbox.set_btn_vectors.clicked.connect(self.control.set_vectors)
        # self.tools_groupbox.nodes_groupbox.set_btn_nodes.clicked.connect(self.control.set_nodes)
        self.tools_groupbox.nodes_groupbox.edit_btn_nodes.clicked.connect(self.control.edit_node)
        self.tools_groupbox.elements_groupbox.loads_btn_elements.clicked.connect(self.control.edit_loads)

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
