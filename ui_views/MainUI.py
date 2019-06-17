from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog as Qfd
from ui_views.Views import toolbox, Menubar

# from numpy import unique
# from ui_views.vector_edit import Ui_vector_widget


class MainUI(QtWidgets.QMainWindow):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self, control, graphicsys):
        super().__init__()
        self.icon = "ui_views/icons/strucpy_icon.png"
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(self.icon)))
        self.setWindowTitle("Strucpy Alpha v0.1")
        self.control = control(self)
        self.graphicsys = graphicsys(self)
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
        #toolbar
        self.tools_groupbox.vectors_groupbox.edit_btn_vectors.clicked.connect(self.control.edit_vector)
        self.tools_groupbox.vectors_groupbox.del_btn_vectors.clicked.connect(self.control.del_selection)
        self.tools_groupbox.vectors_groupbox.add_btn_vectors.clicked.connect(self.control.add_vector)
        self.tools_groupbox.nodes_groupbox.edit_btn_nodes.clicked.connect(self.control.edit_node)
        self.tools_groupbox.elements_groupbox.loads_btn_elements.clicked.connect(self.control.edit_loads)
        self.tools_groupbox.elements_groupbox.edit_btn_elements.clicked.connect(self.control.edit_section_type)
        self.tools_groupbox.run_btn_tools.clicked.connect(self.control.run)
        self.tools_groupbox.deact_btn_tools.clicked.connect(self.control.view_results_all)

        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.keyPressed.connect(self.on_key)
        self.show()

    def keyPressEvent(self, event):
        super(MainUI, self).keyPressEvent(event)
        self.keyPressed.emit(event)

    def on_key(self, event):
        if event.key() in [QtCore.Qt.Key_Up, QtCore.Qt.Key_Down, QtCore.Qt.Key_Left, QtCore.Qt.Key_Right]:
            self.graphicsys.rotation(event.key())
        elif event.key() == QtCore.Qt.Key_Escape:
            self.control.clear_selection()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.control.del_selection()
        else:
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
