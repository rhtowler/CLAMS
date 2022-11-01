
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.xga import  ui_TransferDlg
import numpad
import messagedlg
from PyQt4 import QtSql
import typeseldialog


class TransferDlg(QDialog, ui_TransferDlg.Ui_transferDlg):
    def __init__(self, parent=None):
        super(TransferDlg, self).__init__(parent)
        self.setupUi(self)
        # get stuff from your parent
        self.activeHaul=parent.activeHaul
        self.survey=parent.survey
        self.ship=parent.ship
        self.activePartition=parent.activePartition
        self.db=parent.db
        self.basketTypes=parent.basketTypes
        self.serMonitor=parent.serMonitor
        self.devices=parent.devices
        self.sounds=parent.sounds
        self.validList=[1, 1, 1]
        self.errorIcons=parent.errorIcons
        self.errorSounds=parent.errorSounds
        self.manualDevice=parent.manualDevice
        self.transCount=0
        self.transWeight=0
        # set up dialog windows
        self.message=messagedlg.MessageDlg(self)
        self.numpad = numpad.NumPad(self)
        self.typeDlg = typeseldialog.TypeSelDialog(self)


        # populate lists
        self.sampleIds={}
        query=QtSql.QSqlQuery("SELECT samples.sample_id, species.common_name, samples.parent_sample, samples.subcategory FROM samples, species WHERE "+
        "samples.species_code=species.species_code AND samples.ship="+self.ship+" AND samples.survey="+
        self.survey+" AND samples.event_id="+self.activeHaul+" AND samples.partition='"+self.activePartition+"' AND samples.species_code <>0")
        while query.next():
            if query.value(3).toString()<>'None':
                species_tag=query.value(1).toString()+'-'+query.value(3).toString()
            else:
                species_tag=query.value(1).toString()
            self.fromSampleSpc.addItem(species_tag)
            self.sampleIds.update({species_tag:query.value(0).toString()})
            self.toSampleSpc.addItem(species_tag)

        self.fromSampleSpc.setCurrentIndex(-1)
        self.toSampleSpc.setCurrentIndex(-1)

        self.connect(self.cancelBtn, SIGNAL("clicked()"),self.bail)
        self.connect(self.okBtn, SIGNAL("clicked()"),self.bail)
        self.connect(self.getWtBtn, SIGNAL("clicked()"),self.getWeight)
        self.connect(self.getCntBtn, SIGNAL("clicked()"),self.getCount)
        self.connect(self.fromSampleSpc, SIGNAL("activated(int)"), self.getSampleList)
        self.connect(self.toSampleSpc, SIGNAL("activated(int)"), self.getSampleList)
        self.connect(self.fromBasketType, SIGNAL("activated(int)"), self.getOK)
        self.connect(self.toBasketType, SIGNAL("activated(int)"), self.getOK)
        self.connect(self.serMonitor, SIGNAL("SerialDataReceived"), self.getAuto)

    def getWeight(self):
        self.numpad.msgLabel.setText("Enter Weight to Transfer")
        if self.numpad.exec_():
            self.wtLabel.setText(self.numpad.value)
            self.transWeight=float(self.numpad.value)
            self.transDevice=self.manualDevice

    def getAuto(self, device, val):
        if self.getWtBtn.isEnabled():
            self.wtLabel.setText(val)
            self.transWeight=float(val)
            self.transDevice=device
            self.sounds[self.devices.index(device)].play()
            if self.frombasketType.currentText()=='Count' or self.tobasketType.currentText()=='Count':
                self.getCount()

    def getCount(self):
        self.numpad.msgLabel.setText("Enter Count to Transfer")
        self.numpad.exec_()
        self.cntLabel.setText(self.numpad.value)
        self.transCount=float(self.numpad.value)

    def getSampleList(self):

        box=str(self.sender().objectName())
        if box.startswith('from'):
            self.fromSpc=str(self.fromSampleSpc.currentText())
            self.fromSampleKey=self.sampleIds[self.fromSampleSpc.currentText()]
            self.fromBasketType.setEnabled(True)
            self.fromBasketType.clear()
            query=QtSql.QSqlQuery("  SELECT baskets.basket_type FROM baskets WHERE baskets.ship = "+self.ship+" AND baskets.survey="+self.survey+" AND baskets.event_id="+self.activeHaul+" AND baskets.sample_id="+
                                  self.fromSampleKey+" GROUP BY baskets.basket_type")
            while query.next():
                self.fromBasketType.addItem(query.value(0).toString())
                self.fromBasketType.setCurrentIndex(-1)
        else:
            self.toSpc=str(self.toSampleSpc.currentText())
            self.toSampleKey=self.sampleIds[self.toSampleSpc.currentText()]
            self.toBasketType.setEnabled(True)
            self.toBasketType.clear()
            query=QtSql.QSqlQuery("SELECT gear_options.basket_type FROM gear_options INNER JOIN events ON gear_options.gear=events.gear "+
            "WHERE events.ship="+self.ship+" AND events.survey="+self.survey+" AND events.event_id="+self.activeHaul+" AND gear_options.basket_type "+
            "is not NULL ORDER BY gear_options.basket_type")
            while query.next():
                self.toBasketType.addItem(query.value(0).toString())
                self.toBasketType.setCurrentIndex(-1)


    def getOK(self):
        if self.fromBasketType.currentIndex()>=0 and self.toBasketType.currentIndex()>=0:
            self.getWtBtn.setEnabled(True)
            self.fromType=self.fromBasketType.currentText()
            self.toType=self.toBasketType.currentText()
            if  self.fromBasketType.currentText()=='Count' or self.toBasketType.currentText()=='Count':
                self.getCntBtn.setEnabled(True)


    def  bail(self):
        # make sure you have goods
        if self.sender().text()=='OK':
            if self.transWeight==0:
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1],'No transfer weight provided...', 'info')
                self.message.exec_()
                return
            # check weight
            query=QtSql.QSqlQuery("  SELECT sum(baskets.weight) FROM baskets WHERE baskets.ship = "+self.ship+" AND baskets.survey="+
                                  self.survey+" AND baskets.event_id="+self.activeHaul+" AND baskets.sample_id = "+self.fromSampleKey+
                                    " AND baskets.basket_type ='"+self.fromType+"'")
            query.first()
            fullWeight=float(str(query.value(0).toString()))
            if (fullWeight-self.transWeight)<0: # the transfer is more than the total
                self.message.setMessage(self.errorIcons[1],self.errorSounds[1],"Transfer weight exceeds original sample weight, can't do...", 'info')
                return

            if not self.transCount==0:
                #  only verify count if source and destination are both count sample types
                #  (subsample will not have a count at this time so you can't verify)
                if self.fromType== 'Count':
                    query=QtSql.QSqlQuery("SELECT sum(baskets.count) FROM baskets WHERE baskets.ship = "+self.ship+" AND baskets.survey="+self.survey+
                    " AND baskets.event_id="+self.activeHaul+" AND baskets.sample_id = "+self.fromSampleKey+
                    " AND baskets.basket_type ='Count'")
                    query.first()
                    fullCount=float(str(query.value(0).toString()))
                    if (fullCount-self.transCount)<0:
                        self.message.setMessage(self.errorIcons[1],self.errorSounds[1],"Transfer count exceeds original sample weight, You're asking the impossible...", 'info')
                        return

            self.accept()
        else: # cancel button
            self.reject()



