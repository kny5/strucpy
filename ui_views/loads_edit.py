# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Element_editor_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class LoadsEditor(QtWidgets.QWidget):
    def __init__(self, control, element):
        super().__init__()
        self.control = control
        self.element = element
        self.loads = element.loads
        self.setupUi()
        self.ok_btn.clicked.connect(self.save_values)

    def setupUi(self):
        # self.setObjectName("Dialog")
        self.resize(329, 557)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        # self.verticalLayout.setObjectName("verticalLayout")
        self.element_group = QtWidgets.QGroupBox(self)
        self.element_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        # self.element_group.setObjectName("element_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.element_group)
        self.gridLayout_2.setVerticalSpacing(20)
        # self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.element_group)
        # self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        # self.label_3 = QtWidgets.QLabel(self.element_group)
        # self.label_3.setObjectName("label_3")
        # self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        # self.label_4 = QtWidgets.QLabel(self.element_group)
        # # self.label_4.setObjectName("label_4")
        # self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)

        # self.type = QtWidgets.QComboBox(self.element_group)
        # self.type.setMinimumSize(QtCore.QSize(0, 40))
        # self.type.setMaximumSize(QtCore.QSize(100, 16777215))
        # self.type.setLayoutDirection(QtCore.Qt.LeftToRight)
        # # self.type.setObjectName("type")
        # self.type.addItem("")
        # self.type.addItem("")
        # self.type.addItem("")
        # self.type.addItem("")
        # self.type.addItem("")
        # self.gridLayout_2.addWidget(self.type, 7, 1, 1, 1)

        # self.marco = QtWidgets.QLineEdit(self.element_group)
        # self.marco.setMinimumSize(QtCore.QSize(0, 40))
        # self.marco.setMaximumSize(QtCore.QSize(100, 16777215))
        # self.marco.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.marco.setObjectName("marco")
        # self.gridLayout_2.addWidget(self.marco, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.element_group)
        # self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.aw = QtWidgets.QLineEdit(self.element_group)
        self.aw.setMinimumSize(QtCore.QSize(0, 40))
        self.aw.setMaximumSize(QtCore.QSize(100, 16777215))
        self.aw.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.aw.setObjectName("aw")
        self.gridLayout_2.addWidget(self.aw, 5, 1, 1, 1)
        self.wz = QtWidgets.QLineEdit(self.element_group)
        self.wz.setMinimumSize(QtCore.QSize(0, 40))
        self.wz.setMaximumSize(QtCore.QSize(100, 16777215))
        self.wz.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.wz.setObjectName("wz")
        self.gridLayout_2.addWidget(self.wz, 4, 1, 1, 1)
        self.wy = QtWidgets.QLineEdit(self.element_group)
        self.wy.setMinimumSize(QtCore.QSize(0, 40))
        self.wy.setMaximumSize(QtCore.QSize(100, 40))
        self.wy.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.wy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.wy.setText("")
        # self.wy.setObjectName("wy")
        self.gridLayout_2.addWidget(self.wy, 3, 1, 1, 1)
        self.x_label_end = QtWidgets.QLabel(self.element_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.x_label_end.setFont(font)
        # self.x_label_end.setObjectName("x_label_end")
        self.gridLayout_2.addWidget(self.x_label_end, 1, 0, 1, 1)
        self.kh = QtWidgets.QLineEdit(self.element_group)
        self.kh.setMinimumSize(QtCore.QSize(0, 40))
        self.kh.setMaximumSize(QtCore.QSize(100, 40))
        self.kh.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.ky.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        # self.ky.setObjectName("ky")
        self.gridLayout_2.addWidget(self.kh, 2, 1, 1, 1)
        self.z_label_end = QtWidgets.QLabel(self.element_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.z_label_end.setFont(font)
        # self.z_label_end.setObjectName("z_label_end")
        self.gridLayout_2.addWidget(self.z_label_end, 3, 0, 1, 1)
        self.kv = QtWidgets.QLineEdit(self.element_group)
        self.kv.setMinimumSize(QtCore.QSize(0, 40))
        self.kv.setMaximumSize(QtCore.QSize(100, 40))
        self.kv.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.kv.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        # self.kv.setObjectName("kv")
        self.gridLayout_2.addWidget(self.kv, 1, 1, 1, 1)
        self.y_label_end = QtWidgets.QLabel(self.element_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.y_label_end.setFont(font)
        # self.y_label_end.setObjectName("y_label_end")
        self.gridLayout_2.addWidget(self.y_label_end, 2, 0, 1, 1)
        # # self.edit_type = QtWidgets.QPushButton(self.element_group)
        # self.edit_type.setObjectName("edit_type")
        # # self.gridLayout_2.addWidget(self.edit_type, 8, 0, 1, 1)
        self.verticalLayout.addWidget(self.element_group)
        self.ok_btn = QtWidgets.QPushButton(self)
        self.ok_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.ok_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.ok_btn.setSizeIncrement(QtCore.QSize(80, 40))
        self.ok_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def save_values(self):
        try:
            self.loads.kv = float(self.kv.text())
            self.loads.kh = float(self.kh.text())
            self.loads.wy = float(self.wy.text())
            self.loads.wz = float(self.wz.text())
            self.loads.aw = float(self.aw.text())
            # self.element.marco = self.marco.text()
            # self.element.set_type(self.type.currentIndex())
        except Exception:
            pass

    def changeEvent(self, event):
        pass

    def closeEvent(self, event):
        try:
            self.control.parent.uis_vector.pop(str(self.element.vector.pos))
            self.control.selection.discard(self.element.vector)
        except:
            pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Loads"))
        self.element_group.setTitle(_translate("Dialog", "In " + str(self.element.vector.pos)))
        self.label_2.setText(_translate("Dialog", "Eje Y Angulo de Carga"))
        # self.label_3.setText(_translate("Dialog", "Marco"))
        # self.label_4.setText(_translate("Dialog", "Tipo"))
        # self.type.setItemText(0, _translate("Dialog", "Concreto"))
        # self.type.setItemText(1, _translate("Dialog", "Or: Acero"))
        # self.type.setItemText(2, _translate("Dialog", "Ir: Acero"))
        # self.type.setItemText(3, _translate("Dialog", "Oc: Acero"))
        # self.type.setItemText(4, _translate("Dialog", "Custom"))
        self.label.setText(_translate("Dialog", "Eje Z Carga Uniforme"))
        self.x_label_end.setText(_translate("Dialog", "Reacción Vertical"))
        self.z_label_end.setText(_translate("Dialog", "Eje Y Carga Uniforme"))
        self.y_label_end.setText(_translate("Dialog", "Reacción Horizontal"))
        # # self.edit_type.setText(_translate("Dialog", "Editar Tipo"))
        self.ok_btn.setText(_translate("Dialog", "OK"))


# if __name__ == "__main__":
#     import sys
#     from Model.classes.element_types import Element
#     from Model.classes.geometry import Vector
#     app = QtWidgets.QApplication(sys.argv)
#     # Dialog = QtWidgets.QWidget()
#     # ui = Ui_Dialog())
#     Dialog = ElementEditor(Element(Vector((0,0,0), (1,1,1))))
#     # ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
