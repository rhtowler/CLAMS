# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\SelectActiveSurveyDlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_selectactivesurveydlg(object):
    def setupUi(self, selectactivesurveydlg):
        selectactivesurveydlg.setObjectName(_fromUtf8("selectactivesurveydlg"))
        selectactivesurveydlg.resize(628, 193)
        font = QtGui.QFont()
        font.setPointSize(18)
        selectactivesurveydlg.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(selectactivesurveydlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(selectactivesurveydlg)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ship = QtGui.QComboBox(selectactivesurveydlg)
        self.ship.setObjectName(_fromUtf8("ship"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.ship)
        self.label = QtGui.QLabel(selectactivesurveydlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(selectactivesurveydlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(300, 0))
        self.label_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.survey = QtGui.QComboBox(selectactivesurveydlg)
        self.survey.setObjectName(_fromUtf8("survey"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.survey)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtGui.QPushButton(selectactivesurveydlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setMinimumSize(QtCore.QSize(140, 0))
        self.cancelBtn.setMaximumSize(QtCore.QSize(140, 16777215))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.okBtn = QtGui.QPushButton(selectactivesurveydlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(140)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBtn.sizePolicy().hasHeightForWidth())
        self.okBtn.setSizePolicy(sizePolicy)
        self.okBtn.setMinimumSize(QtCore.QSize(140, 0))
        self.okBtn.setMaximumSize(QtCore.QSize(140, 16777215))
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout.addWidget(self.okBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(selectactivesurveydlg)
        QtCore.QMetaObject.connectSlotsByName(selectactivesurveydlg)

    def retranslateUi(self, selectactivesurveydlg):
        selectactivesurveydlg.setWindowTitle(_translate("selectactivesurveydlg", "Select Active Survey", None))
        self.label_3.setText(_translate("selectactivesurveydlg", "Select the ship and survey you want to make active", None))
        self.label.setText(_translate("selectactivesurveydlg", "Ship", None))
        self.label_2.setText(_translate("selectactivesurveydlg", "Survey Number", None))
        self.cancelBtn.setText(_translate("selectactivesurveydlg", "Cancel", None))
        self.okBtn.setText(_translate("selectactivesurveydlg", "OK", None))

