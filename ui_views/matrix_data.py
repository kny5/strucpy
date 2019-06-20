from PyQt5 import QtCore, QtWidgets
from numpy import nditer

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, program):
        super().__init__()
        self.kest = program.kest
        self.pcur = program.pcur_sum
        self.setupUi()

    def createTable(self, data, tablewidget):
        shape = data.shape
        print(shape)
        if len(shape) == 2:
            tablewidget.setColumnCount(shape[0])
            tablewidget.setRowCount(shape[1])
            it = nditer(data, flags=['multi_index'])
            while not it.finished:
                index = it.multi_index
                tablewidget.setItem(index[0], index[1], QtWidgets.QTableWidgetItem(str(it[0])))
                it.iternext()
        else:
            tablewidget.setColumnCount(shape[0])
            tablewidget.setRowCount(1)
            it = nditer(data, flags=['multi_index'])
            while not it.finished:
                index = it.multi_index
                tablewidget.setItem(0, index[0], QtWidgets.QTableWidgetItem(str(it[0])))
                it.iternext()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableWidget(self.tab)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.createTable(self.kest, self.tableView)
        self.createTable(self.pcur, self.tableView_2)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Vector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Data"))
