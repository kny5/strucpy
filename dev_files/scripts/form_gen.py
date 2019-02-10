# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Model.classes.element_types import Concrete, Element, Vector, Ir, Or


class Ui_Dialog(object):
    def __init__(self):

        self.form_values = []
        self.buttonBox = None
        self.ok_btn = QtWidgets.QDialogButtonBox.Ok
        self.cancel_btn = QtWidgets.QDialogButtonBox.Cancel
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.label = None
        self.lineEdit = None

    def setup_ui(self, dialog, clstouse):

        attributes = [(item, value) for item, value in clstouse.__dict__.items() if not str(item)[0] == "_"]
        print(clstouse.__dict__.keys())
        dialog.setObjectName("dialog")
        dialog.resize(400, 280)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)

        # self.ok_btn.clicked.connect(self.func_add)
        self.buttonBox.setStandardButtons(self.cancel_btn | self.ok_btn)
        # self.buttonBox.accepted.connect(self.func_add)data
        self.buttonBox.setObjectName("buttonBox")

        self.groupBox.setGeometry(QtCore.QRect(10, 10, 270, 260))
        self.groupBox.setObjectName("tools_groupbox")

        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 370))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        for k, item in enumerate(attributes):

            self.label = QtWidgets.QLabel(self.formLayoutWidget)
            self.label.setObjectName("label")
            self.label.setText(str(item[1]))
            self.formLayout.setWidget(0 + k, QtWidgets.QFormLayout.LabelRole, self.label)
            try:
                self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
                self.lineEdit.setText(str(item[1].value))

            except AttributeError:
                if isinstance(item[1], bool):
                    self.lineEdit = QtWidgets.QRadioButton(self.formLayoutWidget)

            self.lineEdit.setObjectName("lineEdit")
            self.formLayout.setWidget(0 + k, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
            self.form_values.append((str(item[0]), self.lineEdit))

        # self.buttonBox.accepted.connect(dialog.accept)
        # self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)


if not __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setup_ui(Dialog, Vector)
    Dialog.show()
    sys.exit(app.exec_())
