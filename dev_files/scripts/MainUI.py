# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupbox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupbox.setTitle("")
        self.groupbox.setObjectName("tools_groupbox")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_7, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_8)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.gridLayout_7.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_8)
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupbox)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle("")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_4.addWidget(self.radioButton, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setTitle("")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_6.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.gridLayout_6.addWidget(self.label_2, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setTitle("")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridLayout_5.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_5.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupbox)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout.addWidget(self.groupbox)
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.horizontalLayout.addWidget(self.openGLWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_DXF = QtWidgets.QAction(MainWindow)
        self.actionAbrir_DXF.setObjectName("actionAbrir_DXF")
        self.actionGuardar_DXF = QtWidgets.QAction(MainWindow)
        self.actionGuardar_DXF.setObjectName("actionGuardar_DXF")
        self.actionBorrar_Todo = QtWidgets.QAction(MainWindow)
        self.actionBorrar_Todo.setObjectName("actionBorrar_Todo")
        self.menuArchivo.addAction(self.actionAbrir_DXF)
        self.menuArchivo.addAction(self.actionGuardar_DXF)
        self.menuArchivo.addAction(self.actionBorrar_Todo)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vectors, draw"))
        self.pushButton.setText(_translate("MainWindow", "Edit"))
        self.pushButton_7.setText(_translate("MainWindow", "SET"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Del"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Nodes, forces and DoF"))
        self.pushButton_8.setText(_translate("MainWindow", "Edit"))
        self.pushButton_9.setText(_translate("MainWindow", "SET"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Elements, section and types"))
        self.pushButton_3.setText(_translate("MainWindow", "EDIT"))
        self.pushButton_10.setText(_translate("MainWindow", "SET"))
        self.pushButton_4.setText(_translate("MainWindow", "CONF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Analysis"))
        self.radioButton.setText(_translate("MainWindow", "Analytic"))
        self.radioButton_3.setText(_translate("MainWindow", "B Aprox"))
        self.label_2.setText(_translate("MainWindow", "MAX B"))
        self.radioButton_2.setText(_translate("MainWindow", "MonteCarlo"))
        self.label.setText(_translate("MainWindow", "Iterations"))
        self.pushButton_5.setText(_translate("MainWindow", "Run"))
        self.menuArchivo.setTitle(_translate("MainWindow", "File"))
        self.actionAbrir_DXF.setText(_translate("MainWindow", "Open DXF"))
        self.actionGuardar_DXF.setText(_translate("MainWindow", "Save as DXF"))
        self.actionBorrar_Todo.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

