# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\acquisition\serial\ui\SelectWinPortDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SelectWinPortDialog(object):
    def setupUi(self, SelectWinPortDialog):
        SelectWinPortDialog.setObjectName("SelectWinPortDialog")
        SelectWinPortDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SelectWinPortDialog.resize(505, 191)
        SelectWinPortDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SelectWinPortDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtWidgets.QLabel(SelectWinPortDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(SelectWinPortDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.cbPorts = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cbPorts.setFont(font)
        self.cbPorts.setObjectName("cbPorts")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbPorts)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.cbBaud = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cbBaud.setFont(font)
        self.cbBaud.setMaxVisibleItems(6)
        self.cbBaud.setObjectName("cbBaud")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbBaud)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(SelectWinPortDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.descLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.descLabel.setFont(font)
        self.descLabel.setText("")
        self.descLabel.setObjectName("descLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descLabel)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(110, 0))
        self.label_3.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(110, 0))
        self.label_5.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.idLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.idLabel.setFont(font)
        self.idLabel.setText("")
        self.idLabel.setObjectName("idLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idLabel)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.statusLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.statusLabel)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbOK = QtWidgets.QPushButton(SelectWinPortDialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_3.addWidget(self.pbOK)
        self.pbCancel = QtWidgets.QPushButton(SelectWinPortDialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_3.addWidget(self.pbCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SelectWinPortDialog)
        self.cbBaud.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(SelectWinPortDialog)

    def retranslateUi(self, SelectWinPortDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectWinPortDialog.setWindowTitle(_translate("SelectWinPortDialog", "Select COM port"))
        self.titleLabel.setText(_translate("SelectWinPortDialog", "Select a COM Port"))
        self.groupBox_2.setTitle(_translate("SelectWinPortDialog", "COM Port"))
        self.label_4.setText(_translate("SelectWinPortDialog", "Port"))
        self.label_8.setText(_translate("SelectWinPortDialog", "Baud"))
        self.cbBaud.setItemText(0, _translate("SelectWinPortDialog", "1200"))
        self.cbBaud.setItemText(1, _translate("SelectWinPortDialog", "2400"))
        self.cbBaud.setItemText(2, _translate("SelectWinPortDialog", "4800"))
        self.cbBaud.setItemText(3, _translate("SelectWinPortDialog", "9600"))
        self.cbBaud.setItemText(4, _translate("SelectWinPortDialog", "19200"))
        self.cbBaud.setItemText(5, _translate("SelectWinPortDialog", "31250"))
        self.cbBaud.setItemText(6, _translate("SelectWinPortDialog", "38400"))
        self.cbBaud.setItemText(7, _translate("SelectWinPortDialog", "57600"))
        self.cbBaud.setItemText(8, _translate("SelectWinPortDialog", "115200"))
        self.cbBaud.setItemText(9, _translate("SelectWinPortDialog", "230400"))
        self.groupBox.setTitle(_translate("SelectWinPortDialog", "COM Port Details"))
        self.label_3.setText(_translate("SelectWinPortDialog", "Description:"))
        self.label_5.setText(_translate("SelectWinPortDialog", "Hardware ID:"))
        self.label.setText(_translate("SelectWinPortDialog", "Status:"))
        self.pbOK.setText(_translate("SelectWinPortDialog", "OK"))
        self.pbCancel.setText(_translate("SelectWinPortDialog", "Cancel"))
