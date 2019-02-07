# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vectoreditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import sys


class Ui_Form(object):
    # def __init__(self):
        # app = QtWidgets.QApplication()
        # form = QtWidgets.QWidget()
        # self.setupUi(form)
        # form.show()
        # sys.exit(app.exec_())

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(548, 539)
        Form.setMaximumSize(QtCore.QSize(548, 539))
        Form.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("")
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vector Editor"))
        self.pushButton.setText(_translate("Form", "Load DXF"))
        self.pushButton_2.setText(_translate("Form", "Save as DXF"))
        self.pushButton_3.setText(_translate("Form", "Delete all"))
        self.groupBox_2.setTitle(_translate("Form", "New"))
        self.pushButton_6.setText(_translate("Form", "Add"))
        self.groupBox.setTitle(_translate("Form", "Selection"))
        self.pushButton_4.setText(_translate("Form", "Edit"))
        self.pushButton_5.setText(_translate("Form", "Delete"))
        self.pushButton_8.setText(_translate("Form", "Next"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
