# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modnode.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class NodeEditor(QtWidgets.QWidget):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(450, 200)
        self.setMinimumSize(QtCore.QSize(450, 240))
        self.setMaximumSize(QtCore.QSize(450, 600))
        self.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dx_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.dx_bool.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.dx_bool)
        self.dy_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.dy_bool.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.dy_bool)
        self.dz_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.dz_bool.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.dz_bool)
        self.mx_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.mx_bool.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.mx_bool)
        self.my_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.my_bool.setObjectName("checkBox_5")
        self.horizontalLayout_4.addWidget(self.my_bool)
        self.mz_bool = QtWidgets.QCheckBox(self.groupBox_3)
        self.mz_bool.setObjectName("checkBox_6")
        self.horizontalLayout_4.addWidget(self.mz_bool)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 405, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_dx = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_dx.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_dx.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.group_dx)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.group_dx)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dx_load = QtWidgets.QLineEdit(self.group_dx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dx_load.sizePolicy().hasHeightForWidth())
        self.dx_load.setSizePolicy(sizePolicy)
        self.dx_load.setMinimumSize(QtCore.QSize(100, 0))
        self.dx_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dx_load.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.dx_load)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.group_dx)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.dx_spring = QtWidgets.QLineEdit(self.group_dx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dx_spring.sizePolicy().hasHeightForWidth())
        self.dx_spring.setSizePolicy(sizePolicy)
        self.dx_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.dx_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dx_spring.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.dx_spring)
        self.verticalLayout_2.addWidget(self.group_dx)
        self.group_dy = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_dy.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_dy.setObjectName("groupBox_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.group_dy)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.group_dy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.dy_load = QtWidgets.QLineEdit(self.group_dy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dy_load.sizePolicy().hasHeightForWidth())
        self.dy_load.setSizePolicy(sizePolicy)
        self.dy_load.setMinimumSize(QtCore.QSize(100, 0))
        self.dy_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dy_load.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.dy_load)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.group_dy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.dy_spring = QtWidgets.QLineEdit(self.group_dy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dy_spring.sizePolicy().hasHeightForWidth())
        self.dy_spring.setSizePolicy(sizePolicy)
        self.dy_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.dy_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dy_spring.setObjectName("lineEdit_10")
        self.horizontalLayout_7.addWidget(self.dy_spring)
        self.verticalLayout_2.addWidget(self.group_dy)
        self.group_dz = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_dz.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_dz.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.group_dz)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.group_dz)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.dz_load = QtWidgets.QLineEdit(self.group_dz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dz_load.sizePolicy().hasHeightForWidth())
        self.dz_load.setSizePolicy(sizePolicy)
        self.dz_load.setMinimumSize(QtCore.QSize(100, 0))
        self.dz_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dz_load.setObjectName("lineEdit_7")
        self.horizontalLayout_6.addWidget(self.dz_load)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.group_dz)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.dz_spring = QtWidgets.QLineEdit(self.group_dz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dz_spring.sizePolicy().hasHeightForWidth())
        self.dz_spring.setSizePolicy(sizePolicy)
        self.dz_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.dz_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dz_spring.setObjectName("lineEdit_8")
        self.horizontalLayout_6.addWidget(self.dz_spring)
        self.verticalLayout_2.addWidget(self.group_dz)
        self.group_mx = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_mx.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_mx.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.group_mx)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.group_mx)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.mx_load = QtWidgets.QLineEdit(self.group_mx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mx_load.sizePolicy().hasHeightForWidth())
        self.mx_load.setSizePolicy(sizePolicy)
        self.mx_load.setMinimumSize(QtCore.QSize(100, 0))
        self.mx_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mx_load.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.mx_load)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.group_mx)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.mx_spring = QtWidgets.QLineEdit(self.group_mx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mx_spring.sizePolicy().hasHeightForWidth())
        self.mx_spring.setSizePolicy(sizePolicy)
        self.mx_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.mx_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mx_spring.setObjectName("lineEdit_6")
        self.horizontalLayout_5.addWidget(self.mx_spring)
        self.verticalLayout_2.addWidget(self.group_mx)
        self.group_my = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_my.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_my.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.group_my)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.group_my)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.my_load = QtWidgets.QLineEdit(self.group_my)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_load.sizePolicy().hasHeightForWidth())
        self.my_load.setSizePolicy(sizePolicy)
        self.my_load.setMinimumSize(QtCore.QSize(100, 0))
        self.my_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.my_load.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.my_load)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.group_my)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.my_spring = QtWidgets.QLineEdit(self.group_my)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_spring.sizePolicy().hasHeightForWidth())
        self.my_spring.setSizePolicy(sizePolicy)
        self.my_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.my_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.my_spring.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.my_spring)
        self.verticalLayout_2.addWidget(self.group_my)
        self.group_mz = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.group_mz.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly | QtCore.Qt.ImhPreferNumbers)
        self.group_mz.setObjectName("groupBox_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.group_mz)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.group_mz)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.mz_load = QtWidgets.QLineEdit(self.group_mz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mz_load.sizePolicy().hasHeightForWidth())
        self.mz_load.setSizePolicy(sizePolicy)
        self.mz_load.setMinimumSize(QtCore.QSize(100, 0))
        self.mz_load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mz_load.setObjectName("lineEdit_15")
        self.horizontalLayout_10.addWidget(self.mz_load)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.label_16 = QtWidgets.QLabel(self.group_mz)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.mz_spring = QtWidgets.QLineEdit(self.group_mz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mz_spring.sizePolicy().hasHeightForWidth())
        self.mz_spring.setSizePolicy(sizePolicy)
        self.mz_spring.setMinimumSize(QtCore.QSize(100, 0))
        self.mz_spring.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mz_spring.setObjectName("lineEdit_16")
        self.horizontalLayout_10.addWidget(self.mz_spring)
        self.verticalLayout_2.addWidget(self.group_mz)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btn_save.clicked.connect(self.save_values)

        self.dx_load.setText(str(self.node.conf['dx']['load']))
        self.dy_load.setText(str(self.node.conf['dy']['load']))
        self.dz_load.setText(str(self.node.conf['dz']['load']))
        self.mx_load.setText(str(self.node.conf['mx']['load']))
        self.my_load.setText(str(self.node.conf['my']['load']))
        self.mz_load.setText(str(self.node.conf['mz']['load']))
        self.dx_spring.setText(str(self.node.conf['dx']['spring']))
        self.dy_spring.setText(str(self.node.conf['dy']['spring']))
        self.dz_spring.setText(str(self.node.conf['dz']['spring']))
        self.mx_spring.setText(str(self.node.conf['mx']['spring']))
        self.my_spring.setText(str(self.node.conf['my']['spring']))
        self.mz_spring.setText(str(self.node.conf['mz']['spring']))

        self.dx_bool.setChecked(self.node.conf['dx']['activated'])
        self.dy_bool.setChecked(self.node.conf['dy']['activated'])
        self.dz_bool.setChecked(self.node.conf['dz']['activated'])
        self.mx_bool.setChecked(self.node.conf['mx']['activated'])
        self.my_bool.setChecked(self.node.conf['my']['activated'])
        self.mz_bool.setChecked(self.node.conf['mz']['activated'])

    def save_values(self):
        self.node.conf['dx']['load'] = float(self.dx_load.text())
        self.node.conf['dx']['spring'] = float(self.dx_spring.text())
        self.node.conf['dx']['activated'] = self.dx_bool.isChecked()

        self.node.conf['dy']['load'] = float(self.dy_load.text())
        self.node.conf['dy']['spring'] = float(self.dy_spring.text())
        self.node.conf['dy']['activated'] = self.dy_bool.isChecked()

        self.node.conf['dz']['load'] = float(self.dz_load.text())
        self.node.conf['dz']['spring'] = float(self.dz_spring.text())
        self.node.conf['dz']['activated'] = self.dz_bool.isChecked()

        self.node.conf['mx']['load'] = float(self.mx_load.text())
        self.node.conf['mx']['spring'] = float(self.mx_spring.text())
        self.node.conf['mx']['activated'] = self.mx_bool.isChecked()

        self.node.conf['my']['load'] = float(self.my_load.text())
        self.node.conf['my']['spring'] = float(self.my_spring.text())
        self.node.conf['my']['activated'] = self.my_bool.isChecked()

        self.node.conf['mz']['load'] = float(self.mz_load.text())
        self.node.conf['mz']['spring'] = float(self.mz_spring.text())
        self.node.conf['mz']['activated'] = self.mz_bool.isChecked()

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # # print(self.node.conf, sep='')

    def closeEvent(self, event):
        try:
            self.control.parent.uis_node.pop(str(self.node.pos))
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Node " + str(self.node.pos)))
        self.groupBox_3.setTitle(_translate("Dialog", "Degrees of Freedom"))
        self.dx_bool.setText(_translate("Dialog", "DX"))
        self.dy_bool.setText(_translate("Dialog", "DY"))
        self.dz_bool.setText(_translate("Dialog", "DZ"))
        self.mx_bool.setText(_translate("Dialog", "MX"))
        self.my_bool.setText(_translate("Dialog", "MY"))
        self.mz_bool.setText(_translate("Dialog", "MZ"))
        self.group_dx.setTitle(_translate("Dialog", "DX"))
        self.label_3.setText(_translate("Dialog", "Load"))
        self.label_4.setText(_translate("Dialog", "Spring"))
        self.group_dy.setTitle(_translate("Dialog", "DY"))
        self.label_9.setText(_translate("Dialog", "Load"))
        self.label_10.setText(_translate("Dialog", "Spring"))
        self.group_dz.setTitle(_translate("Dialog", "DZ"))
        self.label_7.setText(_translate("Dialog", "Load"))
        self.label_8.setText(_translate("Dialog", "Spring"))
        self.group_mx.setTitle(_translate("Dialog", "MX"))
        self.label_5.setText(_translate("Dialog", "Load"))
        self.label_6.setText(_translate("Dialog", "Spring"))
        self.group_my.setTitle(_translate("Dialog", "MY"))
        self.label.setText(_translate("Dialog", "Load"))
        self.label_2.setText(_translate("Dialog", "Spring"))
        self.group_mz.setTitle(_translate("Dialog", "MZ"))
        self.label_15.setText(_translate("Dialog", "Load"))
        self.label_16.setText(_translate("Dialog", "Spring"))
        self.btn_save.setText(_translate("Dialog", "OK"))


# if __name__ == "__main__":
#     import sys
#     from Model.classes.geometry import Node
#     app = QtWidgets.QApplication(sys.argv)
#     # Dialog = QtWidgets.QWidget()
#     ui = NodeEditor(Node((0, 0, 0)))
#     # ui.setupUi(Dialog)
#     ui.show()
#     sys.exit(app.exec_())
