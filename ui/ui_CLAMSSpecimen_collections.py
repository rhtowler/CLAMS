# Form implementation generated from reading ui file 'C:\Users\rick.towler\Work\AFSCGit\CLAMS\application\ui\CLAMSSpecimen_collections.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_clamsSpecimen(object):
    def setupUi(self, clamsSpecimen):
        clamsSpecimen.setObjectName("clamsSpecimen")
        clamsSpecimen.resize(1047, 647)
        self.label_10 = QtWidgets.QLabel(clamsSpecimen)
        self.label_10.setGeometry(QtCore.QRect(440, 29, 162, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.speciesLabel = QtWidgets.QLabel(clamsSpecimen)
        self.speciesLabel.setGeometry(QtCore.QRect(92, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.speciesLabel.setFont(font)
        self.speciesLabel.setAutoFillBackground(True)
        self.speciesLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.speciesLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.speciesLabel.setLineWidth(1)
        self.speciesLabel.setText("")
        self.speciesLabel.setObjectName("speciesLabel")
        self.label_9 = QtWidgets.QLabel(clamsSpecimen)
        self.label_9.setGeometry(QtCore.QRect(19, 17, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(clamsSpecimen)
        self.label_2.setGeometry(QtCore.QRect(19, 39, 79, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sciLabel = QtWidgets.QLabel(clamsSpecimen)
        self.sciLabel.setGeometry(QtCore.QRect(590, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sciLabel.setFont(font)
        self.sciLabel.setAutoFillBackground(True)
        self.sciLabel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.sciLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.sciLabel.setLineWidth(1)
        self.sciLabel.setText("")
        self.sciLabel.setObjectName("sciLabel")
        self.bottomBox = QtWidgets.QGroupBox(clamsSpecimen)
        self.bottomBox.setGeometry(QtCore.QRect(20, 560, 981, 61))
        self.bottomBox.setTitle("")
        self.bottomBox.setObjectName("bottomBox")
        self.addspcBtn = QtWidgets.QPushButton(self.bottomBox)
        self.addspcBtn.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addspcBtn.setFont(font)
        self.addspcBtn.setObjectName("addspcBtn")
        self.commentBtn = QtWidgets.QPushButton(self.bottomBox)
        self.commentBtn.setGeometry(QtCore.QRect(440, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commentBtn.setFont(font)
        self.commentBtn.setObjectName("commentBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.bottomBox)
        self.deleteBtn.setGeometry(QtCore.QRect(310, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.doneBtn = QtWidgets.QPushButton(self.bottomBox)
        self.doneBtn.setGeometry(QtCore.QRect(839, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doneBtn.setFont(font)
        self.doneBtn.setObjectName("doneBtn")
        self.collectBtn = QtWidgets.QPushButton(self.bottomBox)
        self.collectBtn.setGeometry(QtCore.QRect(580, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.collectBtn.setFont(font)
        self.collectBtn.setObjectName("collectBtn")
        self.protoBtn = QtWidgets.QPushButton(self.bottomBox)
        self.protoBtn.setEnabled(True)
        self.protoBtn.setGeometry(QtCore.QRect(150, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.protoBtn.setFont(font)
        self.protoBtn.setObjectName("protoBtn")
        self.printBtn = QtWidgets.QPushButton(self.bottomBox)
        self.printBtn.setGeometry(QtCore.QRect(710, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printBtn.setFont(font)
        self.printBtn.setObjectName("printBtn")
        self.groupBox = QtWidgets.QGroupBox(clamsSpecimen)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 151, 481))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_0 = QtWidgets.QPushButton(self.groupBox)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.verticalLayout.addWidget(self.btn_0)
        self.btn_1 = QtWidgets.QPushButton(self.groupBox)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.verticalLayout.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.verticalLayout.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.groupBox)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.verticalLayout.addWidget(self.btn_3)
        self.btn_4 = QtWidgets.QPushButton(self.groupBox)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.verticalLayout.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.groupBox)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.verticalLayout.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.groupBox)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.verticalLayout.addWidget(self.btn_6)
        self.btn_7 = QtWidgets.QPushButton(self.groupBox)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.verticalLayout.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.groupBox)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.verticalLayout.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.groupBox)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.verticalLayout.addWidget(self.btn_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.measureView = QtWidgets.QTableView(clamsSpecimen)
        self.measureView.setGeometry(QtCore.QRect(170, 300, 841, 251))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.measureView.setFont(font)
        self.measureView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.measureView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.measureView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.measureView.setObjectName("measureView")
        self.measureView.verticalHeader().setVisible(True)
        self.picLabel = QtWidgets.QLabel(clamsSpecimen)
        self.picLabel.setGeometry(QtCore.QRect(370, 80, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.picLabel.setFont(font)
        self.picLabel.setAutoFillBackground(True)
        self.picLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.picLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.samplingMethodBox = QtWidgets.QComboBox(clamsSpecimen)
        self.samplingMethodBox.setGeometry(QtCore.QRect(760, 250, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.samplingMethodBox.setFont(font)
        self.samplingMethodBox.setObjectName("samplingMethodBox")
        self.label_3 = QtWidgets.QLabel(clamsSpecimen)
        self.label_3.setGeometry(QtCore.QRect(760, 220, 191, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(clamsSpecimen)
        self.label_5.setGeometry(QtCore.QRect(761, 70, 151, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.protoLabel = QtWidgets.QLabel(clamsSpecimen)
        self.protoLabel.setGeometry(QtCore.QRect(761, 100, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.protoLabel.setFont(font)
        self.protoLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.protoLabel.setText("")
        self.protoLabel.setObjectName("protoLabel")
        self.cycleBtn = QtWidgets.QPushButton(clamsSpecimen)
        self.cycleBtn.setEnabled(True)
        self.cycleBtn.setGeometry(QtCore.QRect(180, 120, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cycleBtn.setFont(font)
        self.cycleBtn.setCheckable(False)
        self.cycleBtn.setChecked(False)
        self.cycleBtn.setObjectName("cycleBtn")
        self.autoCheck = QtWidgets.QCheckBox(clamsSpecimen)
        self.autoCheck.setGeometry(QtCore.QRect(199, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.autoCheck.setFont(font)
        self.autoCheck.setObjectName("autoCheck")
        self.label_6 = QtWidgets.QLabel(clamsSpecimen)
        self.label_6.setGeometry(QtCore.QRect(180, 220, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.specimenLabel = QtWidgets.QLabel(clamsSpecimen)
        self.specimenLabel.setGeometry(QtCore.QRect(180, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.specimenLabel.setFont(font)
        self.specimenLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.specimenLabel.setText("")
        self.specimenLabel.setObjectName("specimenLabel")
        self.label = QtWidgets.QLabel(clamsSpecimen)
        self.label.setGeometry(QtCore.QRect(760, 140, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lengthTypeBox = QtWidgets.QComboBox(clamsSpecimen)
        self.lengthTypeBox.setGeometry(QtCore.QRect(760, 170, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lengthTypeBox.setFont(font)
        self.lengthTypeBox.setObjectName("lengthTypeBox")

        self.retranslateUi(clamsSpecimen)
        QtCore.QMetaObject.connectSlotsByName(clamsSpecimen)

    def retranslateUi(self, clamsSpecimen):
        _translate = QtCore.QCoreApplication.translate
        clamsSpecimen.setWindowTitle(_translate("clamsSpecimen", "CLAMS Specimen"))
        self.label_10.setText(_translate("clamsSpecimen", "Today\'s Scientist"))
        self.label_9.setText(_translate("clamsSpecimen", "Current"))
        self.label_2.setText(_translate("clamsSpecimen", "Species"))
        self.addspcBtn.setText(_translate("clamsSpecimen", "Species"))
        self.commentBtn.setText(_translate("clamsSpecimen", "Comment"))
        self.deleteBtn.setText(_translate("clamsSpecimen", "Delete"))
        self.doneBtn.setText(_translate("clamsSpecimen", "Done"))
        self.collectBtn.setText(_translate("clamsSpecimen", "Collect"))
        self.protoBtn.setText(_translate("clamsSpecimen", "Protocol"))
        self.printBtn.setText(_translate("clamsSpecimen", "Print"))
        self.btn_0.setText(_translate("clamsSpecimen", "0"))
        self.btn_1.setText(_translate("clamsSpecimen", "1"))
        self.btn_2.setText(_translate("clamsSpecimen", "2"))
        self.btn_3.setText(_translate("clamsSpecimen", "3"))
        self.btn_4.setText(_translate("clamsSpecimen", "4"))
        self.btn_5.setText(_translate("clamsSpecimen", "5"))
        self.btn_6.setText(_translate("clamsSpecimen", "6"))
        self.btn_7.setText(_translate("clamsSpecimen", "7"))
        self.btn_8.setText(_translate("clamsSpecimen", "8"))
        self.btn_9.setText(_translate("clamsSpecimen", "9"))
        self.label_3.setText(_translate("clamsSpecimen", "Sampling Method"))
        self.label_5.setText(_translate("clamsSpecimen", "Current Protocol"))
        self.cycleBtn.setText(_translate("clamsSpecimen", "Next"))
        self.autoCheck.setText(_translate("clamsSpecimen", "Auto Next"))
        self.label_6.setText(_translate("clamsSpecimen", "Specimen ID"))
        self.label.setText(_translate("clamsSpecimen", "Length type"))