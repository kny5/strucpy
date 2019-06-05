# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Oc_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.concrete_group = QtWidgets.QFrame(Form)
        self.concrete_group.setObjectName("concrete_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.concrete_group)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_armour_val = QtWidgets.QRadioButton(self.concrete_group)
        self.input_armour_val.setObjectName("input_armour_val")
        self.gridLayout_2.addWidget(self.input_armour_val, 7, 1, 1, 1)
        self.input_e_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_e_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_e_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_e_val.setObjectName("input_e_val")
        self.gridLayout_2.addWidget(self.input_e_val, 4, 1, 1, 1)
        self.input_pmat_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_pmat_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_pmat_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_pmat_val.setObjectName("input_pmat_val")
        self.gridLayout_2.addWidget(self.input_pmat_val, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.concrete_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.concrete_group)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.input_d_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_d_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_d_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_d_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_d_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_d_val.setObjectName("input_d_val")
        self.gridLayout_2.addWidget(self.input_d_val, 1, 1, 1, 1)
        self.lab_zap_anch = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_anch.setFont(font)
        self.lab_zap_anch.setObjectName("lab_zap_anch")
        self.gridLayout_2.addWidget(self.lab_zap_anch, 1, 0, 1, 1)
        self.input_t_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_t_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_t_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_t_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_t_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_t_val.setObjectName("input_t_val")
        self.gridLayout_2.addWidget(self.input_t_val, 3, 1, 1, 1)
        self.lab_zap_alt = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_alt.setFont(font)
        self.lab_zap_alt.setObjectName("lab_zap_alt")
        self.gridLayout_2.addWidget(self.lab_zap_alt, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.concrete_group)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input_armour_val.setText(_translate("Form", "Armadura"))
        self.label_4.setText(_translate("Form", "Modulo de Elasticidad"))
        self.label_5.setText(_translate("Form", "Peso de Material"))
        self.lab_zap_anch.setText(_translate("Form", "Diámetro de Sección"))
        self.lab_zap_alt.setText(_translate("Form", "Espesor de Sección"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

