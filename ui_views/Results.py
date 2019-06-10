# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from classes.element_types import Element
from classes.geometry import Vector
from numpy import asarray

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, element):
        super().__init__()
        self.id = element.e_id
        self.results = element.results
        self.setupUi()
        self.filler()
        self.show()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(400, 531)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 507))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pg_widget = pg.GraphicsLayoutWidget()
        self.pg_widget.setBackground('FFFFFF')

        # self.plot_item = pg.PlotItem(enableMenu=False)
        # self.pg_widget.addItem(self.plot_item, row=0, col=0)

        self.scrollArea.setWidget(self.pg_widget)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def filler(self):
        _dict = self.results.__dict__
        for c, key in enumerate(_dict, 0):
            if key not in ['dry', 'drz', 'desp_imp_antes_y']:
                a = pg.PlotItem(title=str(key), enableMenu=False)
                a.showGrid(x=True, y=True)
                # a.setFixedWidth(400)
                a.hideAxis('bottom')
                # a.showGrid(x=True, y=True, alpha=100)
                a.hideAxis('left')
                # a.showAxis('right', True)
                scatter = pg.PlotDataItem(x=asarray([x for x in range(0, Element.sections + 1)]), y=_dict[key])
                a.addItem(scatter)
                self.pg_widget.addItem(a, row=c, col=0)
                ax_r = a.getAxis('right')
                # ax_r.setFixedWidth(100)

            # try:
            #     if value.__len__() > 0:
            #         p_item = pg.PlotItem(value, enableMenu=False)
            #         self.values.append(p_item)
            #     else:
            #         pass
            # except TypeError:
            #     pass


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Element " + str(self.id)))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     # Form = QtWidgets.QWidget()
#     ui = Ui_Form(Element(Vector((0,0,0), (1,1,1))))
#     # ui.setupUi(Form)
#     ui.show()
#     sys.exit(app.exec_())

