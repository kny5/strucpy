# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Type_material_editor_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.element_group = QtWidgets.QGroupBox(Dialog)
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
        self.gridLayout_2.addWidget(self.type, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.element_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.element_group)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.fill_this = QtWidgets.QWidget()
        self.fill_this.setGeometry(QtCore.QRect(0, 0, 316, 92))
        self.fill_this.setObjectName("fill_this")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fill_this)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.fill_this)
        self.verticalLayout.addWidget(self.scrollArea)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.ok_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.ok_btn.setSizeIncrement(QtCore.QSize(80, 40))
        self.ok_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.element_group.setTitle(_translate("Dialog", "Element id"))
        self.type.setItemText(0, _translate("Dialog", "Concreto"))
        self.type.setItemText(1, _translate("Dialog", "Or: Acero"))
        self.type.setItemText(2, _translate("Dialog", "Ir: Acero"))
        self.type.setItemText(3, _translate("Dialog", "Oc: Acero"))
        self.type.setItemText(4, _translate("Dialog", "Custom"))
        self.label_4.setText(_translate("Dialog", "Tipo"))
        self.ok_btn.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
