# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Custom_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from classes.element_types import Custom


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent, element):
        super().__init__()
        self.parent = parent
        self.element = element
        self.type = Custom()
        self.setupUi()
        self.parent.ok_btn.clicked.connect(self.save)
        # self.defaults()

    def save(self):
        try:
            self.element.type = self.type
            self.type.e = float(self.input_e_val.text())
            self.type.p_mat = float(self.input_pmat_val.text())
            self.type.area_ = float(self.input_area_val.text())
            self.type.b = float(self.input_b_val.text())
            self.type.h = float(self.input_h_val.text())
            self.type.iyy_ = float(self.input_iyy_val.text())
            self.type.izz_ = float(self.input_izz_val.text())
            self.type.j =  float(self.input_j_val.text())
        except Exception:
            pass

    def defaults(self):
        self.input_izz_val.setText()
        self.input_iyy_val.setText()
        self.input_h_val.setText()
        self.input_b_val.setText()
        self.input_area_val.setText()
        self.input_pmat_val.setText()
        self.input_e_val.setText()
        self.input_j_val.setText(str(self.type.j))
        self.input_armour_val.isChecked(self.input_armour_val)

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(282, 562)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.concrete_group = QtWidgets.QFrame(self)
        self.concrete_group.setObjectName("concrete_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.concrete_group)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.concrete_group)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.input_area_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_area_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_area_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_area_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_area_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_area_val.setText("")
        self.input_area_val.setObjectName("input_area_val")
        self.gridLayout_2.addWidget(self.input_area_val, 4, 1, 1, 1)
        self.input_izz_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_izz_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_izz_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_izz_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_izz_val.setObjectName("input_izz_val")
        self.gridLayout_2.addWidget(self.input_izz_val, 5, 1, 1, 1)
        self.input_armour_val = QtWidgets.QRadioButton(self.concrete_group)
        self.input_armour_val.setObjectName("input_armour_val")
        self.gridLayout_2.addWidget(self.input_armour_val, 11, 1, 1, 1)
        self.lab_con_anc = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_con_anc.setFont(font)
        self.lab_con_anc.setObjectName("lab_con_anc")
        self.gridLayout_2.addWidget(self.lab_con_anc, 4, 0, 1, 1)
        self.input_j_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_j_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_j_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_j_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_j_val.setObjectName("input_j_val")
        self.gridLayout_2.addWidget(self.input_j_val, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.concrete_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 7, 0, 1, 1)
        self.input_e_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_e_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_e_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_e_val.setObjectName("input_e_val")
        self.gridLayout_2.addWidget(self.input_e_val, 8, 1, 1, 1)
        self.input_pmat_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_pmat_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_pmat_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_pmat_val.setObjectName("input_pmat_val")
        self.gridLayout_2.addWidget(self.input_pmat_val, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.concrete_group)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.input_iyy_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_iyy_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_iyy_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_iyy_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_iyy_val.setObjectName("input_iyy_val")
        self.gridLayout_2.addWidget(self.input_iyy_val, 6, 1, 1, 1)
        self.lab_zap_anch = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_anch.setFont(font)
        self.lab_zap_anch.setObjectName("lab_zap_anch")
        self.gridLayout_2.addWidget(self.lab_zap_anch, 1, 0, 1, 1)
        self.input_h_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_h_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_h_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_h_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_h_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_h_val.setObjectName("input_h_val")
        self.gridLayout_2.addWidget(self.input_h_val, 3, 1, 1, 1)
        self.lab_zap_alt = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_alt.setFont(font)
        self.lab_zap_alt.setObjectName("lab_zap_alt")
        self.gridLayout_2.addWidget(self.lab_zap_alt, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.concrete_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.concrete_group)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 9, 0, 1, 1)
        self.input_b_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_b_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_b_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_b_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_b_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_b_val.setObjectName("input_b_val")
        self.gridLayout_2.addWidget(self.input_b_val, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.concrete_group)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Eje Y: Inercia"))
        self.input_armour_val.setText(_translate("Form", "Armadura"))
        self.lab_con_anc.setText(_translate("Form", "Área de Sección"))
        self.label_3.setText(_translate("Form", "Inercia: Momento Polar"))
        self.label.setText(_translate("Form", "Eje X: Inercia"))
        self.lab_zap_anch.setText(_translate("Form", "Ancho de Sección"))
        self.lab_zap_alt.setText(_translate("Form", "Alto de Sección"))
        self.label_4.setText(_translate("Form", "Modulo de Elasticidad"))
        self.label_5.setText(_translate("Form", "Peso de Material"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

