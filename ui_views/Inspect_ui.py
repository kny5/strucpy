from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import nditer, asarray
from pyqtgraph import GraphicsLayoutWidget, PlotItem, PlotCurveItem


class ValueInspector(QtWidgets.QWidget):
    def __init__(self, element):
        super().__init__()
        self.element = element
        self.setupUi()

    def filler(self):
        self._dict = self.element.results.__dict__
        for key in self._dict:
            if key not in ['dry', 'drz', 'desp_imp_antes_y']:
                self.createTab(str(key), self._dict[key])

    def createTab(self, name, data):
        tab = QtWidgets.QWidget()
        self.tabWidget.setTabText(self.tabWidget.indexOf(tab), name)
        layout = QtWidgets.QVBoxLayout(tab)
        graph = GraphicsLayoutWidget(tab)
        self.createGraph(data, graph)
        layout.addWidget(graph)
        table = QtWidgets.QTableWidget(tab)
        self.createTable(data, table)
        layout.addWidget(table)
        self.tabWidget.addTab(tab, name)

    def createGraph(self, data, graph):
        plot = PlotItem()
        line = PlotCurveItem(x=asarray([x for x in range(0, self.element.sections + 1)]), y=data, pxMode=True,
                                symbolSize=5)
        plot.addItem(line)
        graph.addItem(plot, row=0, col=0)


    def createTable(self, data, table):
        shape = data.shape
        if len(shape) == 2:
            table.setColumnCount(shape[0])
            table.setRowCount(shape[1])
            it = nditer(data, flags=['multi_index'])
            while not it.finished:
                index = it.multi_index
                table.setItem(index[0], index[1], QtWidgets.QTableWidgetItem(str(it[0])))
                it.iternext()
        else:
            table.setColumnCount(shape[0])
            table.setRowCount(1)
            it = nditer(data, flags=['multi_index'])
            while not it.finished:
                index = it.multi_index
                table.setItem(0, index[0], QtWidgets.QTableWidgetItem(str(it[0])))
                it.iternext()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(630, 298)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.filler()

        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        # self.graph = QtWidgets.QWidget(self.tab)
        # self.graph.setObjectName("graph")
        # self.verticalLayout_2.addWidget(self.graph)
        # self.tableView = QtWidgets.QTableView(self.tab)
        # self.tableView.setMaximumSize(QtCore.QSize(16777215, 100))
        # self.tableView.setObjectName("tableView")
        # self.verticalLayout_2.addWidget(self.tableView)
        # self.tabWidget.addTab(self.tab, "")
        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Resultados de elemento " + str(self.element.e_id)))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

