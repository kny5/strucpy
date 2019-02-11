# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vector_edit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


translate = QtCore.QCoreApplication.translate


class properties_group(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.nu_label_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.nu_label_prop, 1, 0, 1, 1)
        self.nu_value_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.nu_value_prop, 1, 1, 1, 1)
        self.lm_label_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.lm_label_prop, 2, 0, 1, 1)
        self.lm_value_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.lm_value_prop, 2, 1, 1, 1)
        self.long_label_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.long_label_prop, 0, 0, 1, 1)
        self.long_value_prop = QtWidgets.QLabel(self)
        self.gridLayout_3.addWidget(self.long_value_prop, 0, 1, 1, 1)
        self.retranslate()

    def retranslate(self):
        global translate
        self.setTitle(translate("vector_widget", "Current Properties"))
        self.nu_label_prop.setText(translate("vector_widget", "Nu:"))
        self.nu_value_prop.setText(translate("vector_widget", "value_nu"))
        self.lm_label_prop.setText(translate("vector_widget", "Lambda:"))
        self.lm_value_prop.setText(translate("vector_widget", "value_lambda"))
        self.long_label_prop.setText(translate("vector_widget", "Long:"))
        self.long_value_prop.setText(translate("vector_widget", "value_long"))


class start_group(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.y_label_start = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.y_label_start.setFont(font)
        self.gridLayout.addWidget(self.y_label_start, 3, 0, 1, 1)
        self.z_label_start = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.z_label_start.setFont(font)
        self.gridLayout.addWidget(self.z_label_start, 5, 0, 1, 1)
        self.x_input_start = QtWidgets.QLineEdit(self)
        self.x_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.x_input_start.setFrame(True)
        self.gridLayout.addWidget(self.x_input_start, 1, 1, 1, 1)
        self.y_input_start = QtWidgets.QLineEdit(self)
        self.y_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout.addWidget(self.y_input_start, 3, 1, 1, 1)
        self.z_input_start = QtWidgets.QLineEdit(self)
        self.z_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout.addWidget(self.z_input_start, 5, 1, 1, 1)
        self.x_label_start = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.x_label_start.setFont(font)
        self.gridLayout.addWidget(self.x_label_start, 1, 0, 1, 1)
        self.y_value_start = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.y_value_start, 2, 1, 1, 1)
        self.x_value_start = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.x_value_start, 0, 1, 1, 1)
        self.z_value_start = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.z_value_start, 4, 1, 1, 1)
        self.retranslate()

    def retranslate(self):
        global translate
        self.setTitle(translate("vector_widget", "Start Point"))
        self.y_label_start.setText(translate("vector_widget", "y"))
        self.z_label_start.setText(translate("vector_widget", "z"))
        self.x_label_start.setText(translate("vector_widget", "x"))
        self.y_value_start.setText(translate("vector_widget", "current_y_value"))
        self.x_value_start.setText(translate("vector_widget", "current_x_value"))
        self.z_value_start.setText(translate("vector_widget", "current_z_value"))


class end_group(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.z_input_end = QtWidgets.QLineEdit(self)
        self.z_input_end.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout_2.addWidget(self.z_input_end, 6, 1, 1, 1)
        self.x_label_end = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.x_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.x_label_end, 2, 0, 1, 1)
        self.y_input_end = QtWidgets.QLineEdit(self)
        self.y_input_end.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout_2.addWidget(self.y_input_end, 4, 1, 1, 1)
        self.z_label_end = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.z_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.z_label_end, 6, 0, 1, 1)
        self.x_input_2 = QtWidgets.QLineEdit(self)
        self.x_input_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout_2.addWidget(self.x_input_2, 2, 1, 1, 1)
        self.y_label_end = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.y_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.y_label_end, 4, 0, 1, 1)
        self.y_value_end = QtWidgets.QLabel(self)
        self.gridLayout_2.addWidget(self.y_value_end, 3, 1, 1, 1)
        self.x_value_end = QtWidgets.QLabel(self)
        self.gridLayout_2.addWidget(self.x_value_end, 1, 1, 1, 1)
        self.z_value_end = QtWidgets.QLabel(self)
        self.gridLayout_2.addWidget(self.z_value_end, 5, 1, 1, 1)
        self.retranslate()

    def retranslate(self):
        self.setTitle(translate("vector_widget", "End Point"))
        self.x_label_end.setText(translate("vector_widget", "x"))
        self.z_label_end.setText(translate("vector_widget", "z"))
        self.y_label_end.setText(translate("vector_widget", "y"))
        self.y_value_end.setText(translate("vector_widget", "current_y_value"))
        self.x_value_end.setText(translate("vector_widget", "current_x_value"))
        self.z_value_end.setText(translate("vector_widget", "current_z_value"))


class Ui_vector_widget(object):
    def setupUi(self, vector_widget):
        vector_widget.setObjectName("vector_widget")
        vector_widget.resize(550, 246)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(vector_widget.sizePolicy().hasHeightForWidth())
        vector_widget.setSizePolicy(sizePolicy)
        vector_widget.setMaximumSize(QtCore.QSize(550, 246))

        self.gridLayout_4 = QtWidgets.QGridLayout(vector_widget)
        self.properties_group = properties_group(vector_widget)
        self.gridLayout_4.addWidget(self.properties_group, 1, 0, 1, 1)
        self.start_group = start_group(vector_widget)
        self.gridLayout_4.addWidget(self.start_group, 1, 2, 1, 1)


        self.set_btn_vector = QtWidgets.QPushButton(vector_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_btn_vector.sizePolicy().hasHeightForWidth())
        self.set_btn_vector.setSizePolicy(sizePolicy)
        self.set_btn_vector.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.set_btn_vector.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.set_btn_vector.setAutoDefault(True)
        self.gridLayout_4.addWidget(self.set_btn_vector, 2, 4, 1, 1)

        self.end_group = end_group(vector_widget)
        self.gridLayout_4.addWidget(self.end_group, 1, 4, 1, 1)

        self.line = QtWidgets.QFrame(vector_widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout_4.addWidget(self.line, 1, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(vector_widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout_4.addWidget(self.line_2, 1, 1, 1, 1)

        self.retranslateUi(vector_widget)
        QtCore.QMetaObject.connectSlotsByName(vector_widget)

    def retranslateUi(self, vector_widget):
        global translate
        vector_widget.setWindowTitle(translate("vector_widget", "Vector Edit"))
        self.set_btn_vector.setText(translate("vector_widget", "Set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vector_widget = QtWidgets.QWidget()
    ui = Ui_vector_widget()
    ui.setupUi(vector_widget)
    vector_widget.show()
    sys.exit(app.exec_())

