# Form implementation generated from reading ui file 'FEATDietTypeDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 568)
        self.tw_stom_type = QtWidgets.QTabWidget(Dialog)
        self.tw_stom_type.setGeometry(QtCore.QRect(10, 40, 441, 451))
        self.tw_stom_type.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 18pt \"Calibri\";")
        self.tw_stom_type.setObjectName("tw_stom_type")
        self.collect = QtWidgets.QWidget()
        self.collect.setObjectName("collect")
        self.pb_taken = QtWidgets.QPushButton(self.collect)
        self.pb_taken.setGeometry(QtCore.QRect(120, 80, 171, 51))
        self.pb_taken.setObjectName("pb_taken")
        self.pb_not_taken = QtWidgets.QPushButton(self.collect)
        self.pb_not_taken.setGeometry(QtCore.QRect(120, 200, 171, 51))
        self.pb_not_taken.setObjectName("pb_not_taken")
        self.label_4 = QtWidgets.QLabel(self.collect)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 191, 41))
        self.label_4.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.l_cur_code = QtWidgets.QLabel(self.collect)
        self.l_cur_code.setGeometry(QtCore.QRect(220, 300, 191, 41))
        self.l_cur_code.setStyleSheet("font: 14pt \"Calibri\";")
        self.l_cur_code.setObjectName("l_cur_code")
        self.tw_stom_type.addTab(self.collect, "")
        self.contents = QtWidgets.QWidget()
        self.contents.setObjectName("contents")
        self.pb_not_taken_2 = QtWidgets.QPushButton(self.contents)
        self.pb_not_taken_2.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.pb_not_taken_2.setObjectName("pb_not_taken_2")
        self.pb_sp_1 = QtWidgets.QPushButton(self.contents)
        self.pb_sp_1.setGeometry(QtCore.QRect(20, 210, 261, 51))
        self.pb_sp_1.setObjectName("pb_sp_1")
        self.pb_sp_2 = QtWidgets.QPushButton(self.contents)
        self.pb_sp_2.setGeometry(QtCore.QRect(20, 280, 261, 51))
        self.pb_sp_2.setObjectName("pb_sp_2")
        self.pb_sp_3 = QtWidgets.QPushButton(self.contents)
        self.pb_sp_3.setGeometry(QtCore.QRect(20, 350, 261, 51))
        self.pb_sp_3.setObjectName("pb_sp_3")
        self.pb_overall = QtWidgets.QPushButton(self.contents)
        self.pb_overall.setGeometry(QtCore.QRect(240, 100, 171, 51))
        self.pb_overall.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_overall.setObjectName("pb_overall")
        self.label = QtWidgets.QLabel(self.contents)
        self.label.setGeometry(QtCore.QRect(305, 180, 51, 21))
        self.label.setStyleSheet("font: 10pt \"Calibri\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.contents)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 121, 41))
        self.label_3.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.pb_vol_3 = QtWidgets.QPushButton(self.contents)
        self.pb_vol_3.setGeometry(QtCore.QRect(300, 350, 71, 51))
        self.pb_vol_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_vol_3.setObjectName("pb_vol_3")
        self.pb_vol_2 = QtWidgets.QPushButton(self.contents)
        self.pb_vol_2.setGeometry(QtCore.QRect(300, 280, 71, 51))
        self.pb_vol_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_vol_2.setObjectName("pb_vol_2")
        self.pb_vol_1 = QtWidgets.QPushButton(self.contents)
        self.pb_vol_1.setGeometry(QtCore.QRect(300, 210, 71, 51))
        self.pb_vol_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_vol_1.setObjectName("pb_vol_1")
        self.pb_code_1 = QtWidgets.QPushButton(self.contents)
        self.pb_code_1.setEnabled(True)
        self.pb_code_1.setGeometry(QtCore.QRect(390, 210, 41, 51))
        self.pb_code_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_code_1.setObjectName("pb_code_1")
        self.pb_code_3 = QtWidgets.QPushButton(self.contents)
        self.pb_code_3.setEnabled(True)
        self.pb_code_3.setGeometry(QtCore.QRect(390, 350, 41, 51))
        self.pb_code_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_code_3.setObjectName("pb_code_3")
        self.pb_code_2 = QtWidgets.QPushButton(self.contents)
        self.pb_code_2.setEnabled(True)
        self.pb_code_2.setGeometry(QtCore.QRect(390, 280, 41, 51))
        self.pb_code_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pb_code_2.setObjectName("pb_code_2")
        self.tw_stom_type.addTab(self.contents, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pb_done = QtWidgets.QPushButton(Dialog)
        self.pb_done.setGeometry(QtCore.QRect(280, 500, 161, 51))
        self.pb_done.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 16pt \"Calibri\";")
        self.pb_done.setObjectName("pb_done")
        self.pb_cancel = QtWidgets.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(20, 500, 161, 51))
        self.pb_cancel.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 16pt \"Calibri\";")
        self.pb_cancel.setObjectName("pb_cancel")

        self.retranslateUi(Dialog)
        self.tw_stom_type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stomachs"))
        self.pb_taken.setText(_translate("Dialog", "Taken"))
        self.pb_not_taken.setText(_translate("Dialog", "Not Taken"))
        self.label_4.setText(_translate("Dialog", "Current Barcode"))
        self.l_cur_code.setText(_translate("Dialog", "None"))
        self.tw_stom_type.setTabText(self.tw_stom_type.indexOf(self.collect), _translate("Dialog", "Stomach Collection"))
        self.pb_not_taken_2.setText(_translate("Dialog", "Can\'t be sampled"))
        self.pb_sp_1.setText(_translate("Dialog", "Species 1"))
        self.pb_sp_2.setText(_translate("Dialog", "Species 2"))
        self.pb_sp_3.setText(_translate("Dialog", "Species 3"))
        self.pb_overall.setText(_translate("Dialog", "Overall Weight"))
        self.label.setText(_translate("Dialog", "Volume"))
        self.label_3.setText(_translate("Dialog", "Overall Weight"))
        self.pb_vol_3.setText(_translate("Dialog", "Vol 3"))
        self.pb_vol_2.setText(_translate("Dialog", "Vol 2"))
        self.pb_vol_1.setText(_translate("Dialog", "Vol 1"))
        self.pb_code_1.setText(_translate("Dialog", "sp_code"))
        self.pb_code_3.setText(_translate("Dialog", "sp_code"))
        self.pb_code_2.setText(_translate("Dialog", "sp_code"))
        self.tw_stom_type.setTabText(self.tw_stom_type.indexOf(self.contents), _translate("Dialog", "Stomach Contents"))
        self.label_2.setText(_translate("Dialog", "Select Diet Collection Type..."))
        self.pb_done.setText(_translate("Dialog", "Done"))
        self.pb_cancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())