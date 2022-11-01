
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import  ui_MatGuide
import os
from PyQt4 import QtSql

class MatGuide(QDialog, ui_MatGuide.Ui_matGuide):
    def __init__(self,  parent=None):
        super(MatGuide, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.db=parent.db
        self.speciesName=parent.speciesName
        self.settings=parent.settings

        self.descLabel.palette().setColor(self.descLabel.backgroundRole(), QColor(255, 255, 255))

        #  get the maturity table information
        query=QtSql.QSqlQuery("SELECT species_code FROM species WHERE common_name='"+self.speciesName+"'", self.db)
        query.first()
        self.speciesCode=query.value(0).toString()
        query=QtSql.QSqlQuery("SELECT parameter_value FROM species_data WHERE lower(species_parameter)='maturity_table' "+
                "AND species_code="+self.speciesCode, self.db)
        query.first()
        self.maturityTable=query.value(0).toString()

        self.spcLabel.setText(self.speciesName)
        self.matTabLabel.setText(self.maturityTable)
        query=QtSql.QSqlQuery("SELECT button_text, description_text_male, description_text_female FROM " +
                "maturity_description WHERE maturity_table="+self.maturityTable+" ORDER BY maturity_key",  self.db)
        self.maturityBtnText=[]
        self.maleDesc=[]
        self.femaleDesc=[]
        self.nextBtn.setEnabled(False)
        self.prevBtn.setEnabled(False)
        while query.next():
            self.maturityBtnText.append(query.value(0).toString())
            self.maleDesc.append(query.value(1).toString())
            self.femaleDesc.append(query.value(2).toString())

        self.imageList=[]
        fileList=os.listdir(self.settings[QString('ImageDir')]+'\\matPics')
        for i in range(len(fileList)):
            if fileList[i].startswith(str(self.speciesCode)):
                self.imageList.append(fileList[i])

        for i in range(8):
            try:
                exec(str("self.mat"+str(i+1)+"Btn.setText(self.maturityBtnText[i])"))
            except:
                exec(str("self.mat"+str(i+1)+"Btn.setText(' -  ')"))
                exec(str("self.mat"+str(i+1)+"Btn.setEnabled(False)"))

        self.connect(self.mat1Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat2Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat3Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat4Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat5Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat6Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat7Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.mat8Btn, SIGNAL("clicked()"), self.getMat)
        self.connect(self.nextBtn,  SIGNAL("clicked()"), self.getNext)
        self.connect(self.prevBtn,  SIGNAL("clicked()"), self.getPrev)
        self.connect(self.exitBtn, SIGNAL("clicked()"),self.goExit)
        self.connect(self.maleBtn, SIGNAL("clicked()"),self.getMat)
        self.connect(self.femaleBtn, SIGNAL("clicked()"),self.getMat)

        screen=QDesktopWidget().screenGeometry()
        window=self.geometry()
        self.setGeometry((screen.width()-window.width())/2, self.settings[QString('WindowAnchor')]-
                window.height(), window.width(), window.height())
        self.setMinimumSize(window.width(), window.height())
        self.setMaximumSize(window.width(), window.height())


    def getMat(self):
        matStage=-1
        for i in range(8):
            exec(str("button=self.mat"+str(i+1)+"Btn.isChecked()"))
            if button:
                matStage=i
        if matStage<0:# no maturity has been selected
            return
        self.dispImages=[]
        if self.maleBtn.isChecked():
            self.descLabel.setText(self.maleDesc[matStage])
            for i in range(len(self.imageList)):
                if self.imageList[i].startswith(str(self.speciesCode)+"_M_"+str(matStage+1)):
                    self.dispImages.append(self.imageList[i])
        else:
            self.descLabel.setText(self.femaleDesc[matStage])
            for i in range(len(self.imageList)):
                if self.imageList[i].startswith(str(self.speciesCode)+"_F_"+str(matStage+1)):
                    self.dispImages.append(self.imageList[i])
        self.pic=QImage()
        self.counter=0
        try:
            self.pic.load(self.settings[QString('ImageDir')]+'\\matPics\\'+self.dispImages[self.counter])
            self.pic=self.pic.scaledToHeight(511, Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(self.pic))
        except:
            self.picLabel.setText("<font size = 24> No Image </font>")
        self.nextBtn.setEnabled(True)
        self.prevBtn.setEnabled(True)

    def getNext(self):
        if self.counter<len(self.dispImages)-1:
            self.counter+=1
        else:
            self.counter=0
        try:
            self.pic.load(self.settings[QString('ImageDir')]+'\\matPics\\'+self.dispImages[self.counter])
            self.pic=self.pic.scaledToHeight(511, Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(self.pic))
        except:
            self.picLabel.setText("<font size = 24> No Image </font>")
    def getPrev(self):
        if self.counter>0:
            self.counter-=1
        else:
            self.counter=len(self.dispImages)-1
        try:
            self.pic.load(self.settings[QString('ImageDir')]+'\\matPics\\'+self.dispImages[self.counter])
            self.pic=self.pic.scaledToHeight(511, Qt.SmoothTransformation)
            self.picLabel.setPixmap(QPixmap.fromImage(self.pic))
        except:
            self.picLabel.setText("<font size = 24> No Image </font>")


    def goExit(self):
        self.accept()

