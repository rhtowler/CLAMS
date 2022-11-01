# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rick.towler\Desktop\CLAMS\ui\xga\PrinterAdminDlg.ui'
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

class Ui_printerAdminDlg(object):
    def setupUi(self, printerAdminDlg):
        printerAdminDlg.setObjectName(_fromUtf8("printerAdminDlg"))
        printerAdminDlg.resize(407, 387)
        self.verticalLayout = QtGui.QVBoxLayout(printerAdminDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(printerAdminDlg)
        self.textEdit.setEnabled(True)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.detectMediaBtn = QtGui.QPushButton(printerAdminDlg)
        self.detectMediaBtn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detectMediaBtn.setFont(font)
        self.detectMediaBtn.setObjectName(_fromUtf8("detectMediaBtn"))
        self.verticalLayout.addWidget(self.detectMediaBtn)
        self.testFormat1Btn = QtGui.QPushButton(printerAdminDlg)
        self.testFormat1Btn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.testFormat1Btn.setFont(font)
        self.testFormat1Btn.setObjectName(_fromUtf8("testFormat1Btn"))
        self.verticalLayout.addWidget(self.testFormat1Btn)
        self.testFormat2Btn = QtGui.QPushButton(printerAdminDlg)
        self.testFormat2Btn.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.testFormat2Btn.setFont(font)
        self.testFormat2Btn.setObjectName(_fromUtf8("testFormat2Btn"))
        self.verticalLayout.addWidget(self.testFormat2Btn)

        self.retranslateUi(printerAdminDlg)
        QtCore.QMetaObject.connectSlotsByName(printerAdminDlg)

    def retranslateUi(self, printerAdminDlg):
        printerAdminDlg.setWindowTitle(_translate("printerAdminDlg", "Printer Administration", None))
        self.textEdit.setHtml(_translate("printerAdminDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Zebra Label Printer Maintenance</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">After loading labels or ink you must run the autodetect media routine so the printer can detect the media breaks. This may also be required after the printer lid has been opened. Use this method sparingly since it will feed out 5 or 6 labels.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You can use the &quot;Test Label&quot; buttons to print test labels to verify the printer is working correctly.</span></p></body></html>", None))
        self.detectMediaBtn.setText(_translate("printerAdminDlg", "Autodetect Media", None))
        self.testFormat1Btn.setText(_translate("printerAdminDlg", "Print Test Label: Format 1", None))
        self.testFormat2Btn.setText(_translate("printerAdminDlg", "Print Test Label: Format 2", None))

