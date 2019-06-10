# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Type_material_editor_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from ui_views.concrete_widget import Ui_Form as ConcEditor
from ui_views.Or_widget import Ui_Form as OrEditor
from ui_views.Ir_widget import Ui_Form as IrEditor
from ui_views.Oc_widget import Ui_Form as OcEditor
from ui_views.Custom_widget import Ui_Form as CustomEditor


class TypeEditor(QtWidgets.QWidget):
    def __init__(self, element):
        super().__init__()
        self.element = element
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(340, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.element_group = QtWidgets.QGroupBox(self)
        self.element_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.element_group.setObjectName("element_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.element_group)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.type = QtWidgets.QComboBox(self.element_group)
        self.type.setMinimumSize(QtCore.QSize(0, 40))
        self.type.setMaximumSize(QtCore.QSize(100, 16777215))
        self.type.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.gridLayout_2.addWidget(self.type, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.element_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.element_group)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # self.scroll_content = QtWidgets.QWidget()
        # self.scroll_content.setGeometry(QtCore.QRect(0, 0, 316, 92))
        # self.scroll_content.setObjectName("scroll_content")

        # self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scroll_content)
        # self.verticalLayout_3.setObjectName("verticalLayout_3")

        # self.fill_this = QtWidgets.QVBoxLayout()
        # self.fill_this.setObjectName("fill_this")
        # self.message = QtWidgets.QLabel(self.scroll_content)
        # self.message.setObjectName("message")
        # self.fill_this.addWidget(self.message)
        # self.verticalLayout_3.addLayout(self.fill_this)

        # self.scrollArea.setWidget(self.scroll_content)
        self.verticalLayout.addWidget(self.scrollArea)
        self.ok_btn = QtWidgets.QPushButton(self)
        # self.ok_btn.setMinimumSize(QtCore.QSize(80, 40))
        # self.ok_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.ok_btn.setFixedSize(QtCore.QSize(80, 40))
        # self.ok_btn.setSizeIncrement(QtCore.QSize(80, 40))
        self.ok_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.type.currentIndexChanged.connect(self.filler)
        self.ok_btn.clicked.connect(self.save_type)


    def filler(self):
        index = self.type.currentIndex()
        if index == 0:
            return
        elif index == 1:
            # self.element.set_type(index)
            ui = ConcEditor(self,self.element)
            self.scrollArea.setWidget(ui)
        elif index == 2:
            # self.element.set_type(index)
            ui = OrEditor(self,self.element)
            self.scrollArea.setWidget(ui)
        elif index == 3:
            # self.element.set_type(index)
            ui = IrEditor(self,self.element)
            self.scrollArea.setWidget(ui)
        elif index == 4:
            # self.element.set_type(index)
            ui = OcEditor(self,self.element)
            self.scrollArea.setWidget(ui)
        elif index == 5:
            # self.element.set_type(index)
            ui = CustomEditor(self,self.element)
            self.scrollArea.setWidget(ui)

    def save_type(self):
        print("saved")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.element_group.setTitle(_translate("Dialog", "Element id"))
        self.type.setItemText(0, _translate("Dialog", "Empty"))
        self.type.setItemText(1, _translate("Dialog", "Concreto"))
        self.type.setItemText(2, _translate("Dialog", "Or: Acero"))
        self.type.setItemText(3, _translate("Dialog", "Ir: Acero"))
        self.type.setItemText(4, _translate("Dialog", "Oc: Acero"))
        self.type.setItemText(5, _translate("Dialog", "Custom"))
        self.label_4.setText(_translate("Dialog", "Tipo"))
        # self.message.setText(_translate("Dialog", "Hola"))
        self.ok_btn.setText(_translate("Dialog", "OK"))




# if __name__ == "__main__":
#     import sys
#     from classes.element_types import Element
#     from classes.geometry import Vector
#     app = QtWidgets.QApplication(sys.argv)
#     # Dialog = QtWidgets.QDialog()
#     element = Element(Vector((0,0,0), (1,1,1)))
#     ui = TypeEditor(element)
#     # ui.setupUi(Dialog)
#     ui.show()
#     sys.exit(app.exec_())
