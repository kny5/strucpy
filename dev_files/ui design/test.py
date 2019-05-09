# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Concrete_editor_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 389)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.concrete_group = QtWidgets.QGroupBox(Dialog)
        self.concrete_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.concrete_group.setObjectName("concrete_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.concrete_group)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lab_mat_peso = QtWidgets.QLabel(self.concrete_group)
        self.lab_mat_peso.setObjectName("lab_mat_peso")
        self.gridLayout_2.addWidget(self.lab_mat_peso, 5, 0, 1, 1)
        self.lab_e = QtWidgets.QLabel(self.concrete_group)
        self.lab_e.setObjectName("lab_e")
        self.gridLayout_2.addWidget(self.lab_e, 4, 0, 1, 1)
        self.input_pmat_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_pmat_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_pmat_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.input_pmat_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_pmat_val.setObjectName("input_pmat_val")
        self.gridLayout_2.addWidget(self.input_pmat_val, 5, 1, 1, 1)
        self.e = QtWidgets.QLineEdit(self.concrete_group)
        self.e.setMinimumSize(QtCore.QSize(0, 40))
        self.e.setMaximumSize(QtCore.QSize(100, 16777215))
        self.e.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.e.setObjectName("e")
        self.gridLayout_2.addWidget(self.e, 4, 1, 1, 1)
        self.input_bp_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_bp_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_bp_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_bp_val.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input_bp_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_bp_val.setText("")
        self.input_bp_val.setObjectName("input_bp_val")
        self.gridLayout_2.addWidget(self.input_bp_val, 3, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.input_h_val, 2, 1, 1, 1)
        self.lab_con_anc = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_con_anc.setFont(font)
        self.lab_con_anc.setObjectName("lab_con_anc")
        self.gridLayout_2.addWidget(self.lab_con_anc, 3, 0, 1, 1)
        self.input_b_val = QtWidgets.QLineEdit(self.concrete_group)
        self.input_b_val.setMinimumSize(QtCore.QSize(0, 40))
        self.input_b_val.setMaximumSize(QtCore.QSize(100, 40))
        self.input_b_val.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_b_val.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.input_b_val.setObjectName("input_b_val")
        self.gridLayout_2.addWidget(self.input_b_val, 1, 1, 1, 1)
        self.lab_zap_alt = QtWidgets.QLabel(self.concrete_group)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lab_zap_alt.setFont(font)
        self.lab_zap_alt.setObjectName("lab_zap_alt")
        self.gridLayout_2.addWidget(self.lab_zap_alt, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.concrete_group)
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
        self.concrete_group.setTitle(_translate("Dialog", "Element id"))
        self.lab_mat_peso.setText(_translate("Dialog", "Peso de Material"))
        self.lab_e.setText(_translate("Dialog", "Modulo de Elasticidad"))
        self.lab_zap_anch.setText(_translate("Dialog", "Ancho"))
        self.lab_con_anc.setText(_translate("Dialog", "Contratrabe Ancho"))
        self.lab_zap_alt.setText(_translate("Dialog", "Alto"))
        self.ok_btn.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
