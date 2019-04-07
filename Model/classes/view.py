from PyQt5 import QtWidgets, QtCore


translate = QtCore.QCoreApplication.translate


class vectors_tools(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.vectors_layout = QtWidgets.QGridLayout(self)
        self.edit_btn_vectors = QtWidgets.QPushButton(self)
        self.vectors_layout.addWidget(self.edit_btn_vectors, 0, 1, 1, 1)
        self.set_btn_vectors = QtWidgets.QPushButton(self)
        self.vectors_layout.addWidget(self.set_btn_vectors, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.vectors_layout.addItem(spacerItem, 1, 3, 1, 1)
        self.add_btn_vectors = QtWidgets.QPushButton(self)
        self.vectors_layout.addWidget(self.add_btn_vectors, 0, 3, 1, 1)
        self.del_btn_vectors = QtWidgets.QPushButton(self)
        self.vectors_layout.addWidget(self.del_btn_vectors, 1, 1, 1, 1)
        self.retranslate_ui()

    def retranslate_ui(self):
        global translate
        self.setTitle(translate("MainWindow", "Vectors, draw"))
        self.edit_btn_vectors.setText(translate("MainWindow", "Edit"))
        self.set_btn_vectors.setText(translate("MainWindow", "SET"))
        self.add_btn_vectors.setText(translate("MainWindow", "Add"))
        self.del_btn_vectors.setText(translate("MainWindow", "Del"))


class nodes_tools(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.gridLayout_7 = QtWidgets.QGridLayout(self)
        self.edit_btn_nodes = QtWidgets.QPushButton(self)
        self.gridLayout_7.addWidget(self.edit_btn_nodes, 0, 0, 1, 1)
        self.set_btn_nodes = QtWidgets.QPushButton(self)
        self.gridLayout_7.addWidget(self.set_btn_nodes, 0, 1, 1, 1)
        #spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout_7.addItem(spacerItem1, 1, 0, 1, 1)
        self.retranslate_ui()

    def retranslate_ui(self):
        global translate
        self.setTitle(translate("MainWindow", "Nodes, forces and DoF"))
        self.edit_btn_nodes.setText(translate("MainWindow", "Edit"))
        self.set_btn_nodes.setText(translate("MainWindow", "SET"))


class elements_tools(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.edit_btn_elements = QtWidgets.QPushButton(self)
        self.gridLayout_2.addWidget(self.edit_btn_elements, 0, 0, 1, 1)
        self.set_btn_elements = QtWidgets.QPushButton(self)
        self.gridLayout_2.addWidget(self.set_btn_elements, 1, 1, 1, 1)
        self.conf_btn_elements = QtWidgets.QPushButton(self)
        self.gridLayout_2.addWidget(self.conf_btn_elements, 0, 1, 1, 1)
        self.retranslate_ui()

    def retranslate_ui(self):
        global translate
        self.setTitle(translate("MainWindow", "Elements, section and types"))
        self.edit_btn_elements.setText(translate("MainWindow", "EDIT"))
        self.set_btn_elements.setText(translate("MainWindow", "SET"))
        self.conf_btn_elements.setText(translate("MainWindow", "CONF"))


class analysis_tools(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.gridLayout_3 = QtWidgets.QGridLayout(self)

        self.analytic_bool_analysis = QtWidgets.QRadioButton(self)
        self.analytic_bool_analysis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_3.addWidget(self.analytic_bool_analysis, 0, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.baprox_bool_analysis = QtWidgets.QRadioButton(self)
        self.baprox_bool_analysis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_3.addWidget(self.baprox_bool_analysis, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.label_2, 1, 3, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_3.addWidget(self.lineEdit, 2, 2, 1, 1)

        self.montecarlo_bool_analysis = QtWidgets.QRadioButton(self)
        self.montecarlo_bool_analysis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_3.addWidget(self.montecarlo_bool_analysis, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.label, 2, 3, 1, 1)

        self.standard_bool_analysis = QtWidgets.QRadioButton(self)
        self.standard_bool_analysis.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_3.addWidget(self.standard_bool_analysis, 3, 0, 1, 1)

        self.retranslate()

    def retranslate(self):
        global translate
        self.setTitle(translate("MainWindow", "Analysis"))
        self.analytic_bool_analysis.setText(translate("MainWindow", "Analytic"))
        self.baprox_bool_analysis.setText(translate("MainWindow", "B Aprox"))
        self.label_2.setText(translate("MainWindow", "MAX B"))
        self.montecarlo_bool_analysis.setText(translate("MainWindow", "MonteCarlo"))
        self.label.setText(translate("MainWindow", "Iterations"))
        self.standard_bool_analysis.setText(translate("MainWindow", "Standard"))


class toolbox(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.max_width = 250
        self.max_height = 16777215
        self.min_width = 250
        self.min_height = 600
        self.setMaximumSize(QtCore.QSize(self.max_width, self.max_height))
        self.setMinimumSize(QtCore.QSize(self.min_width, self.min_height))
        self.tools_layout = QtWidgets.QVBoxLayout(self)

        self.vectors_groupbox = vectors_tools(self)
        self.tools_layout.addWidget(self.vectors_groupbox)

        self.nodes_groupbox = nodes_tools(self)
        self.tools_layout.addWidget(self.nodes_groupbox)

        self.elements_groupbox = elements_tools(self)
        self.tools_layout.addWidget(self.elements_groupbox)

        self.analysis_groupbox = analysis_tools(self)
        self.tools_layout.addWidget(self.analysis_groupbox)
        self.run_btn_tools = QtWidgets.QPushButton(self)
        self.tools_layout.addWidget(self.run_btn_tools)
        self.retranslate_ui()

    def retranslate_ui(self):
        global translate
        self.setTitle(translate("MainWindow", "Tools"))
        self.run_btn_tools.setText(translate("MainWindow", "Run"))


class Menubar(QtWidgets.QMenuBar):
    def __init__(self, parent, abrir, guardar, borrar):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menuArchivo = QtWidgets.QMenu(self)

        self.actionAbrir_DXF = QtWidgets.QAction(self)
        self.actionAbrir_DXF.setShortcut("Ctrl+O")
        self.actionGuardar_DXF = QtWidgets.QAction(self)
        self.actionGuardar_DXF.setShortcut("Ctrl+S")
        self.actionBorrar_Todo = QtWidgets.QAction(self)

        self.menuArchivo.addAction(self.actionAbrir_DXF)
        self.menuArchivo.addAction(self.actionGuardar_DXF)
        self.menuArchivo.addAction(self.actionBorrar_Todo)
        self.addAction(self.menuArchivo.menuAction())

        self.actionAbrir_DXF.triggered.connect(abrir)
        self.actionGuardar_DXF.triggered.connect(guardar)
        self.actionBorrar_Todo.triggered.connect(borrar)

        self.retranslate()

    def retranslate(self):
        global translate
        self.menuArchivo.setTitle(translate("MainWindow", "File"))
        self.actionAbrir_DXF.setText(translate("MainWindow", "Open DXF"))
        self.actionGuardar_DXF.setText(translate("MainWindow", "Save as DXF"))
        self.actionBorrar_Todo.setText(translate("MainWindow", "Clear All"))



