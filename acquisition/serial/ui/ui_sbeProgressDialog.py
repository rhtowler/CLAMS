# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\acquisition\serial\ui\sbeProgressDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_sbeProgressDialog(object):
    def setupUi(self, sbeProgressDialog):
        sbeProgressDialog.setObjectName("sbeProgressDialog")
        sbeProgressDialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        sbeProgressDialog.resize(400, 84)
        self.verticalLayout = QtWidgets.QVBoxLayout(sbeProgressDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(sbeProgressDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.abortButton = QtWidgets.QPushButton(sbeProgressDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.abortButton.setFont(font)
        self.abortButton.setObjectName("abortButton")
        self.horizontalLayout.addWidget(self.abortButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(sbeProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(sbeProgressDialog)

    def retranslateUi(self, sbeProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        sbeProgressDialog.setWindowTitle(_translate("sbeProgressDialog", "SBE Download Progress"))
        self.abortButton.setText(_translate("sbeProgressDialog", "Abort Download"))
