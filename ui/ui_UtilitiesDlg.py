# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\UtilitiesDlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_utilitiesdlg(object):
    def setupUi(self, utilitiesdlg):
        utilitiesdlg.setObjectName("utilitiesdlg")
        utilitiesdlg.resize(400, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(utilitiesdlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.exportFSCSBtn = QtWidgets.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.exportFSCSBtn.setFont(font)
        self.exportFSCSBtn.setObjectName("exportFSCSBtn")
        self.verticalLayout.addWidget(self.exportFSCSBtn)
        self.setupBtn = QtWidgets.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.setupBtn.setFont(font)
        self.setupBtn.setObjectName("setupBtn")
        self.verticalLayout.addWidget(self.setupBtn)
        self.loadStreamBtn = QtWidgets.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.loadStreamBtn.setFont(font)
        self.loadStreamBtn.setObjectName("loadStreamBtn")
        self.verticalLayout.addWidget(self.loadStreamBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneBtn = QtWidgets.QPushButton(utilitiesdlg)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.verticalLayout.addWidget(self.doneBtn)

        self.retranslateUi(utilitiesdlg)
        QtCore.QMetaObject.connectSlotsByName(utilitiesdlg)

    def retranslateUi(self, utilitiesdlg):
        _translate = QtCore.QCoreApplication.translate
        utilitiesdlg.setWindowTitle(_translate("utilitiesdlg", "CLAMS Utilities"))
        self.label.setText(_translate("utilitiesdlg", "CLAMS Utilities"))
        self.exportFSCSBtn.setText(_translate("utilitiesdlg", "Export FSCS files"))
        self.setupBtn.setText(_translate("utilitiesdlg", "Setup Serial Devices"))
        self.loadStreamBtn.setText(_translate("utilitiesdlg", "load stream data"))
        self.doneBtn.setText(_translate("utilitiesdlg", "Done"))