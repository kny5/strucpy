# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ir_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from classes.element_types import Ir

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent, element):
        super().__init__()
        self.parent = parent
        self.element = element
        self.type = Ir()
        self.setupUi()
        self.parent.ok_btn.clicked.connect(self.save)

    def save(self):
        try:
            self.element.type = self.type
            self.type.armour = bool(self.input_armour_val.isChecked())
            self.type.bf = float(self.input_bf_val.text())
            self.type.d = float(self.input_d_val.text())
            self.type.e = float(self.input_e_val.text())
            self.type.p_mat = float(self.input_pmat_val.text())
            self.type.tf = float(self.input_tf_val.text())
            self.type.tw = float(self.input_tw_val.text())
        except Exception:
            pass

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(282, 424)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.concrete_group = QtWidgets.QFrame(self)
        self.concrete_group.setObjectName("concrete_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.concrete_group)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.concrete_group)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.input_tf_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_tf_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_tf_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_tf_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_tf_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_tf_val.setText("")
        self.input_tf_val.setObjectName("input_tf_val")
        self.gridLayout_2.addWidget(self.input_tf_val, 3, 1, 1, 1)
        self.input_tw_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_tw_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_tw_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_tw_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_tw_val.setObjectName("input_tw_val")
        self.gridLayout_2.addWidget(self.input_tw_val, 4, 1, 1, 1)
        self.input_armour_val = QtWidgets.QRadioButton(self.concrete_group)
        self.input_armour_val.setObjectName("input_armour_val")
        self.gridLayout_2.addWidget(self.input_armour_val, 7, 1, 1, 1)
        self.lab_con_anc = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_con_anc.setFont(font)
        self.lab_con_anc.setObjectName("lab_con_anc")
        self.gridLayout_2.addWidget(self.lab_con_anc, 3, 0, 1, 1)
        self.input_e_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_e_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_e_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_e_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_e_val.setObjectName("input_e_val")
        self.gridLayout_2.addWidget(self.input_e_val, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.concrete_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.concrete_group)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.input_pmat_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_pmat_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_pmat_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_pmat_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_pmat_val.setObjectName("input_pmat_val")
        self.gridLayout_2.addWidget(self.input_pmat_val, 5, 1, 1, 1)
        self.lab_zap_anch = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_anch.setFont(font)
        self.lab_zap_anch.setObjectName("lab_zap_anch")
        self.gridLayout_2.addWidget(self.lab_zap_anch, 1, 0, 1, 1)
        self.input_bf_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_bf_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_bf_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_bf_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_bf_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_bf_val.setObjectName("input_bf_val")
        self.gridLayout_2.addWidget(self.input_bf_val, 2, 1, 1, 1)
        self.input_d_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_d_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_d_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_d_val.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_d_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_d_val.setObjectName("input_d_val")
        self.gridLayout_2.addWidget(self.input_d_val, 1, 1, 1, 1)
        self.lab_zap_alt = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_alt.setFont(font)
        self.lab_zap_alt.setObjectName("lab_zap_alt")
        self.gridLayout_2.addWidget(self.lab_zap_alt, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.concrete_group)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Peso de Material"))
        self.input_armour_val.setText(_translate("Form", "Armadura"))
        self.lab_con_anc.setText(_translate("Form", "Espesor de Patín"))
        self.label_3.setText(_translate("Form", "Modulo de Elasticidad"))
        self.label.setText(_translate("Form", "Espesor de Alma"))
        self.lab_zap_anch.setText(_translate("Form", "Peralte de Sección"))
        self.lab_zap_alt.setText(_translate("Form", "Ancho de Patín"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())

