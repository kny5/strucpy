# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vector_edit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vector_widget(QtWidgets.QWidget):
    def __init__(self, vectors):
        super().__init__()
        self.vectors = vectors
        self.setupUi()
        self.show()

    def filter_common_fields(self):
        if self.vectors.__len__() > 1:
            for vector in self.vectors:
                pass
        else:
            return False

    def save_values(self):
        if self.vectors.__len__() == 1:
            pass
        else:
            for vector in self.vectors:
                pass

    def setupUi(self):
        self.resize(550, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(550, 304))
        self.gridLayout_4 = QtWidgets.QGridLayout(self)

        self.properties_group = QtWidgets.QGroupBox(self)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.properties_group)
        self.nu_value_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.nu_value_prop, 2, 1, 1, 1)
        self.lm_value_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.lm_value_prop, 3, 1, 1, 1)
        self.long_value_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.long_value_prop, 1, 1, 1, 1)
        self.long_label_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.long_label_prop, 1, 0, 1, 1)
        self.lm_label_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.lm_label_prop, 3, 0, 1, 1)
        self.nu_label_prop = QtWidgets.QLabel(self.properties_group)
        self.gridLayout_3.addWidget(self.nu_label_prop, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.properties_group, 1, 0, 1, 1)

        self.start_group = QtWidgets.QGroupBox(self)
        self.gridLayout = QtWidgets.QGridLayout(self.start_group)
        self.x_input_start = QtWidgets.QLineEdit(self.start_group)
        self.x_input_start.setMinimumSize(QtCore.QSize(0, 40))
        self.x_input_start.setMaximumSize(QtCore.QSize(16777215, 40))
        self.x_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout.addWidget(self.x_input_start, 1, 1, 1, 1)
        self.x_value_start = QtWidgets.QLabel(self.start_group)
        self.x_value_start.setEnabled(False)
        self.gridLayout.addWidget(self.x_value_start, 0, 1, 1, 1)
        self.y_label_start = QtWidgets.QLabel(self.start_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.y_label_start.setFont(font)
        self.gridLayout.addWidget(self.y_label_start, 3, 0, 1, 1)
        self.z_label_start = QtWidgets.QLabel(self.start_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.z_label_start.setFont(font)
        self.gridLayout.addWidget(self.z_label_start, 5, 0, 1, 1)
        self.y_input_start = QtWidgets.QLineEdit(self.start_group)
        self.y_input_start.setMinimumSize(QtCore.QSize(0, 40))
        self.y_input_start.setMaximumSize(QtCore.QSize(16777215, 40))
        self.y_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout.addWidget(self.y_input_start, 3, 1, 1, 1)
        self.z_input_start = QtWidgets.QLineEdit(self.start_group)
        self.z_input_start.setMinimumSize(QtCore.QSize(0, 40))
        self.z_input_start.setMaximumSize(QtCore.QSize(16777215, 40))
        self.z_input_start.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout.addWidget(self.z_input_start, 5, 1, 1, 1)
        self.x_label_start = QtWidgets.QLabel(self.start_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.x_label_start.setFont(font)
        self.gridLayout.addWidget(self.x_label_start, 1, 0, 1, 1)
        self.y_value_start = QtWidgets.QLabel(self.start_group)
        self.y_value_start.setEnabled(False)
        self.gridLayout.addWidget(self.y_value_start, 2, 1, 1, 1)
        self.z_value_start = QtWidgets.QLabel(self.start_group)
        self.z_value_start.setEnabled(False)
        self.gridLayout.addWidget(self.z_value_start, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.start_group, 1, 2, 1, 1)

        self.set_btn_vector = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_btn_vector.sizePolicy().hasHeightForWidth())
        self.set_btn_vector.setSizePolicy(sizePolicy)
        self.set_btn_vector.setMinimumSize(QtCore.QSize(80, 40))
        self.set_btn_vector.setMaximumSize(QtCore.QSize(80, 40))
        self.set_btn_vector.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.set_btn_vector.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.set_btn_vector.setAutoDefault(True)
        self.gridLayout_4.addWidget(self.set_btn_vector, 2, 4, 1, 1)


        self.end_group = QtWidgets.QGroupBox(self)
        self.end_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.end_group)
        self.z_input_end = QtWidgets.QLineEdit(self.end_group)
        self.z_input_end.setMinimumSize(QtCore.QSize(0, 40))
        self.z_input_end.setMaximumSize(QtCore.QSize(16777215, 40))
        self.z_input_end.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.z_input_end.setText("")
        self.gridLayout_2.addWidget(self.z_input_end, 6, 1, 1, 1)
        self.x_label_end = QtWidgets.QLabel(self.end_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.x_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.x_label_end, 2, 0, 1, 1)
        self.y_input_end = QtWidgets.QLineEdit(self.end_group)
        self.y_input_end.setMinimumSize(QtCore.QSize(0, 40))
        self.y_input_end.setMaximumSize(QtCore.QSize(16777215, 40))
        self.y_input_end.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout_2.addWidget(self.y_input_end, 4, 1, 1, 1)
        self.z_label_end = QtWidgets.QLabel(self.end_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.z_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.z_label_end, 6, 0, 1, 1)
        self.x_input_2 = QtWidgets.QLineEdit(self.end_group)
        self.x_input_2.setMinimumSize(QtCore.QSize(0, 40))
        self.x_input_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.x_input_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.gridLayout_2.addWidget(self.x_input_2, 2, 1, 1, 1)
        self.y_label_end = QtWidgets.QLabel(self.end_group)
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setWeight(50)
        # self.y_label_end.setFont(font)
        self.gridLayout_2.addWidget(self.y_label_end, 4, 0, 1, 1)
        self.y_value_end = QtWidgets.QLabel(self.end_group)
        self.y_value_end.setEnabled(False)
        self.gridLayout_2.addWidget(self.y_value_end, 3, 1, 1, 1)
        self.x_value_end = QtWidgets.QLabel(self.end_group)
        self.x_value_end.setEnabled(False)
        self.gridLayout_2.addWidget(self.x_value_end, 1, 1, 1, 1)
        self.z_value_end = QtWidgets.QLabel(self.end_group)
        self.z_value_end.setEnabled(False)
        self.gridLayout_2.addWidget(self.z_value_end, 5, 1, 1, 1)
        self.gridLayout_4.addWidget(self.end_group, 1, 4, 1, 1)

        # self.line = QtWidgets.QFrame(vector_widget)
        # self.line.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.gridLayout_4.addWidget(self.line, 1, 3, 1, 1)
        # self.line_2 = QtWidgets.QFrame(vector_widget)
        # self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.gridLayout_4.addWidget(self.line_2, 1, 1, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, vector_widget):
        _translate = QtCore.QCoreApplication.translate
        vector_widget.setWindowTitle(_translate("vector_widget", "Vector Edit"))
        self.properties_group.setTitle(_translate("vector_widget", "Current Properties"))
        self.nu_value_prop.setText(_translate("vector_widget", "value_nu"))
        self.lm_value_prop.setText(_translate("vector_widget", "value_lambda"))
        self.long_value_prop.setText(_translate("vector_widget", "value_long"))
        self.long_label_prop.setText(_translate("vector_widget", "Long:"))
        self.lm_label_prop.setText(_translate("vector_widget", "Lambda:"))
        self.nu_label_prop.setText(_translate("vector_widget", "Nu:"))
        self.start_group.setTitle(_translate("vector_widget", "Start Point"))
        self.x_value_start.setText(_translate("vector_widget", "current_x_value"))
        self.y_label_start.setText(_translate("vector_widget", "y"))
        self.z_label_start.setText(_translate("vector_widget", "z"))
        self.x_label_start.setText(_translate("vector_widget", "x"))
        self.y_value_start.setText(_translate("vector_widget", "current_y_value"))
        self.z_value_start.setText(_translate("vector_widget", "current_z_value"))
        self.set_btn_vector.setText(_translate("vector_widget", "Set"))
        self.end_group.setTitle(_translate("vector_widget", "End Point"))
        self.x_label_end.setText(_translate("vector_widget", "x"))
        self.z_label_end.setText(_translate("vector_widget", "z"))
        self.y_label_end.setText(_translate("vector_widget", "y"))
        self.y_value_end.setText(_translate("vector_widget", "current_y_value"))
        self.x_value_end.setText(_translate("vector_widget", "current_x_value"))
        self.z_value_end.setText(_translate("vector_widget", "current_z_value"))


if __name__ == "__main__":
    import sys
    from Model.classes.geometry import Vector
    app = QtWidgets.QApplication([])
    # vector_widget = QtWidgets.QWidget()
    ui = Ui_vector_widget(Vector((0,0,0), (11,1,1)))
    # ui.setupUi(vector_widget)
    # vector_widget.show()
    sys.exit(app.exec_())

