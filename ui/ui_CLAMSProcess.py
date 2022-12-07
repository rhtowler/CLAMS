# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\CLAMSProcess.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsProcess(object):
    def setupUi(self, clamsProcess):
        clamsProcess.setObjectName("clamsProcess")
        clamsProcess.resize(1020, 760)
        self.haulBtn = QtWidgets.QPushButton(clamsProcess)
        self.haulBtn.setEnabled(False)
        self.haulBtn.setGeometry(QtCore.QRect(120, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.haulBtn.setFont(font)
        self.haulBtn.setAutoFillBackground(True)
        self.haulBtn.setCheckable(False)
        self.haulBtn.setObjectName("haulBtn")
        self.haulLabel = QtWidgets.QLabel(clamsProcess)
        self.haulLabel.setGeometry(QtCore.QRect(20, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.haulLabel.setFont(font)
        self.haulLabel.setAutoFillBackground(True)
        self.haulLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.haulLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.haulLabel.setLineWidth(1)
        self.haulLabel.setText("")
        self.haulLabel.setObjectName("haulLabel")
        self.label = QtWidgets.QLabel(clamsProcess)
        self.label.setGeometry(QtCore.QRect(8, 0, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.doneBtn = QtWidgets.QPushButton(clamsProcess)
        self.doneBtn.setGeometry(QtCore.QRect(650, 680, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.doneBtn.setFont(font)
        self.doneBtn.setAutoFillBackground(True)
        self.doneBtn.setObjectName("doneBtn")
        self.catchBtn = QtWidgets.QPushButton(clamsProcess)
        self.catchBtn.setEnabled(False)
        self.catchBtn.setGeometry(QtCore.QRect(567, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.catchBtn.setFont(font)
        self.catchBtn.setAutoFillBackground(True)
        self.catchBtn.setCheckable(False)
        self.catchBtn.setObjectName("catchBtn")
        self.lengthBtn = QtWidgets.QPushButton(clamsProcess)
        self.lengthBtn.setEnabled(False)
        self.lengthBtn.setGeometry(QtCore.QRect(707, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lengthBtn.setFont(font)
        self.lengthBtn.setAutoFillBackground(True)
        self.lengthBtn.setCheckable(False)
        self.lengthBtn.setObjectName("lengthBtn")
        self.specBtn = QtWidgets.QPushButton(clamsProcess)
        self.specBtn.setEnabled(False)
        self.specBtn.setGeometry(QtCore.QRect(847, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.specBtn.setFont(font)
        self.specBtn.setAutoFillBackground(True)
        self.specBtn.setCheckable(False)
        self.specBtn.setObjectName("specBtn")
        self.line = QtWidgets.QFrame(clamsProcess)
        self.line.setGeometry(QtCore.QRect(10, 80, 1001, 21))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.picLabel = QtWidgets.QLabel(clamsProcess)
        self.picLabel.setGeometry(QtCore.QRect(10, 100, 981, 561))
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.partitionBox = QtWidgets.QComboBox(clamsProcess)
        self.partitionBox.setGeometry(QtCore.QRect(268, 30, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.partitionBox.setFont(font)
        self.partitionBox.setObjectName("partitionBox")
        self.label_2 = QtWidgets.QLabel(clamsProcess)
        self.label_2.setGeometry(QtCore.QRect(265, 0, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fixSpeciesBtn = QtWidgets.QPushButton(clamsProcess)
        self.fixSpeciesBtn.setGeometry(QtCore.QRect(20, 620, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fixSpeciesBtn.setFont(font)
        self.fixSpeciesBtn.setAutoFillBackground(True)
        self.fixSpeciesBtn.setObjectName("fixSpeciesBtn")
        self.editCodendStateBtn = QtWidgets.QPushButton(clamsProcess)
        self.editCodendStateBtn.setGeometry(QtCore.QRect(20, 680, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editCodendStateBtn.setFont(font)
        self.editCodendStateBtn.setObjectName("editCodendStateBtn")

        self.retranslateUi(clamsProcess)
        QtCore.QMetaObject.connectSlotsByName(clamsProcess)

    def retranslateUi(self, clamsProcess):
        _translate = QtCore.QCoreApplication.translate
        clamsProcess.setWindowTitle(_translate("clamsProcess", "CLAMS Haul Processing"))
        self.haulBtn.setText(_translate("clamsProcess", "Haul Form"))
        self.label.setText(_translate("clamsProcess", "Haul Number"))
        self.doneBtn.setText(_translate("clamsProcess", "Finished processing haul"))
        self.catchBtn.setText(_translate("clamsProcess", "Catch Form"))
        self.lengthBtn.setText(_translate("clamsProcess", "Length Form"))
        self.specBtn.setText(_translate("clamsProcess", "Specimen Form"))
        self.label_2.setText(_translate("clamsProcess", "Partiton"))
        self.fixSpeciesBtn.setText(_translate("clamsProcess", "Fix Species/Sex Assignment"))
        self.editCodendStateBtn.setText(_translate("clamsProcess", "Edit Codend State"))