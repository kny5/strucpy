# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addvector.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class edit_vector(object):

    def __init__(self, vector):
        self.vector = vector
        self.start = vector.start
        self.end = vector.end
        # self.setupUi(QtWidgets.QWidget())

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 240)
        Dialog.setMinimumSize(QtCore.QSize(450, 240))
        Dialog.setMaximumSize(QtCore.QSize(450, 240))
        Dialog.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.groupBox.setObjectName("groupbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("%.3f" % self.start[0])

        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
        # self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("%.3f" % self.start[1])

        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 16777215))
        # self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("%.3f" % self.start[2])

        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        # self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("%.3f" % self.end[0])

        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        # self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("%.3f" % self.end[1])

        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        # self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText("%.3f" % self.end[2])

        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.push_save)

        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def push_save(self):
        x1 = float(self.lineEdit.text())
        y1 = float(self.lineEdit_2.text())
        z1 = float(self.lineEdit_3.text())
        x2 = float(self.lineEdit_4.text())
        y2 = float(self.lineEdit_5.text())
        z2 = float(self.lineEdit_6.text())

        self.vector.start = (x1, y1, z1)
        self.vector.end = (x2, y2, z2)
        self.vector.reformat_byz()
        self.dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Vector "))
        self.groupBox.setTitle(_translate("Dialog", "Start"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.groupBox_2.setTitle(_translate("Dialog", "End"))
        self.label_4.setText(_translate("Dialog", "X"))
        self.label_5.setText(_translate("Dialog", "Y"))
        self.label_6.setText(_translate("Dialog", "Z"))
        self.pushButton.setText(_translate("Dialog", "OK"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
#
