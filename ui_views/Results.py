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
        # self.show()
        # self.table()

    def changeEvent(self, event):
        if self.isActiveWindow():
            try:
                self.prints()
            except Exception:
                pass

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(300, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 400))
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
        self._dict = self.results.__dict__
        for c, key in enumerate(self._dict, 0):
            if key not in ['dry', 'drz', 'desp_imp_antes_y']:
                a = pg.PlotItem() # enableMenu=False)
                x_l = a.getAxis('left')
                x_l.setWidth(50)
                # x_r = a.getAxis('right')
                # x_r.setWidth(50)
                # a.showGrid(x=True, y=True)
                # a.setFixedWidth(600)
                a.hideAxis('bottom')
                a.showGrid(x=True, alpha=0.5)
                # a.hideAxis('left')
                # a.showAxis('right', True)
                scatter = pg.ScatterPlotItem(x=asarray([x for x in range(0, Element.sections + 1)]), y=self._dict[key], pxMode=True, symbol='o', size=4)
                scatter.setBrush(pg.mkBrush('#303030'))
                scatter.setPen(pg.mkPen(None))
                a.addItem(scatter)

                line = pg.PlotCurveItem(x=asarray([x for x in range(0, Element.sections + 1)]), y=self._dict[key], pxMode=True, symbolSize=5)
                line.setPen(pg.mkPen('#808080', width=1))
                # line.setData(symbol='o', symbolPen=None, symbolBrush=pg.mkBrush('#404040'), pxMode=True, symbolSize=5)
                a.addItem(line)
                a.setLabel('left', text=key)
                self.pg_widget.addItem(a, row=c, col=0)
     #            print('*' * 30)
     #            print(key)
     #            print(self._dict[key])
     #    print('#' * 50)
     #    print('Elemento: ' + str(self.id))
        # print(*self._dict, sep='\n')
        # print(*self._dict.values(), sep='\n')
    def prints(self):
        print('#' * 50)
        print('Elemento: ' + str(self.id))
        for key in self._dict:
            print('*' * 30)
            print(key)
            print(self._dict[key])

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

