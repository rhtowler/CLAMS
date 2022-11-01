
import shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_StreamLoadDlg



class StreamLoadDlg(QDialog, ui_StreamLoadDlg.Ui_streamloaddlg):

    def __init__(self, parent=None):
        super(StreamLoadDlg, self).__init__(parent)
        self.setupUi(self)

        self.db=parent.db
        self.ship=parent.ship
        self.survey=parent.survey
        self.settings=parent.settings
        self.workStation=parent.workStation
        self.activeHaul=parent.activeHaul
        self.progressBar.setValue(0)
        self.progressBar.hide()
        #  set up signals
        self.connect(self.loadSBEBtn, SIGNAL("clicked()"), self.loadSBEData)
        self.connect(self.depthBtn, SIGNAL("clicked()"), self.loadBottomData)
        self.connect(self.GPSBtn, SIGNAL("clicked()"), self.loadPositionData)

        self.connect(self.doneBtn, SIGNAL("clicked()"), self.doneClicked)
        

        query=QtSql.QSqlQuery("SELECT haul_data.parameter_value FROM haul_data, haul_parameters WHERE "+
                "haul_data.haul_parameter=haul_parameters.haul_parameter AND haul_data.ship=" +
                              self.ship + " AND haul_data.survey=" + self.survey + " AND haul_data.haul= " +
                              self.activeHaul + " AND haul_parameters.data_type = 'datetime'")
        times=[]
        while query.next():
            times.append(QDateTime().fromString(query.value(0).toString(),  'MMddyyyy hh:mm:ss.zzz'))
        
        self.startTime=min(times)
        self.endTime = max(times)
        
        self.totLines=self.startTime.secsTo(self.endTime)

        self.show()

    def loadPositionData(self):
        query=QtSql.QSqlQuery("SELECT device_id FROM device WHERE device_name='MX420-Lat'")
        query.first()
        latDevice=query.value(0).toString()
        query=QtSql.QSqlQuery("SELECT device_id FROM device WHERE device_name='MX420-Lon'")
        query.first()
        lonDevice=query.value(0).toString()
        # position data
        query=QtSql.QSqlQuery("SELECT * FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" and measurement_type='Longitude'")
        if query.first():
            reply = QMessageBox.question(self, 'Warning!',"<font size = 14> CLAMSbase has GPS position data for this haul.  Do you want to overwrite? </font>", QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No: 
                return
            else:
                query=QtSql.QSqlQuery("DELETE FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" AND measurement_type in ('Latitude', 'Longitude')")
                              
        dirDlg=QFileDialog(self)
        fileName=dirDlg.getOpenFileName(self, "Select MX420 File","C:/")
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        # get GPS MX420 file 
        file = open(str(fileName))
        cnt=0
        
        self.progressBar.show()
        for line in file:
            
            tmp=line.split('\n')
            data =tmp[0].split(',')

            lineTime=QDateTime().fromString(data[0]+" "+data[1], 'MM/dd/yyyy hh:mm:ss.zzz')
            if lineTime>= self.startTime and lineTime<= self.endTime:
                query = QtSql.QSqlQuery("INSERT INTO haul_stream_data (ship, survey, haul, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeHaul+","+ latDevice+",to_timestamp('"+lineTime.toString("MMddyyyy hh:mm:ss.zzz")+
                                "','MMDDYYYY HH24:MI:SS.FF3'),'Latitude','"+data[4]+data[5]+"')")
                query = QtSql.QSqlQuery("INSERT INTO haul_stream_data (ship, survey, haul, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeHaul+","+ lonDevice+",to_timestamp('"+lineTime.toString("MMddyyyy hh:mm:ss.zzz")+
                                "','MMDDYYYY HH24:MI:SS.FF3'),'Longitude','"+data[6]+data[7]+"')")
                cnt+=1
                self.progressBar.setValue(cnt/self.totLines*100)
                                
        file.close()
        QApplication.restoreOverrideCursor()
        
    def loadBottomData(self,  filename):
        query=QtSql.QSqlQuery("SELECT device_id FROM device WHERE device_name='EK60-Depth-m'")
        query.first()
        botDevice=query.value(0).toString()
        
        query=QtSql.QSqlQuery("SELECT * FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" and measurement_type='BottomDepth'")
        if query.first():
            reply = QMessageBox.question(self, 'Warning!',"<font size = 14> CLAMSbase has bottom depth data for this haul.  Do you want to overwrite? </font>", QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No: 
                return
            else:
                query=QtSql.QSqlQuery("DELETE FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" AND measurement_type ='BottomDepth'")
                              
        dirDlg=QFileDialog(self)
        fileName=dirDlg.getOpenFileName(self, "Select EK 60 bottom depth File","C:/")
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        file = open(str(fileName))
        self.progressBar.show()
        cnt=0
        for line in file:
            tmp=line.split('\n')
            data =tmp[0].split(',')
            lineTime=QDateTime().fromString(data[0]+" "+data[1], 'MM/dd/yyyy hh:mm:ss.zzz')
            if lineTime>= self.startTime and lineTime<= self.endTime:
                query = QtSql.QSqlQuery("INSERT INTO haul_stream_data (ship, survey, haul, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeHaul+","+botDevice+",to_timestamp('"+lineTime.toString("MMddyyyy hh:mm:ss.zzz")+
                                "','MMDDYYYY HH24:MI:SS.FF3'),'BottomDepth','"+data[5]+"')")
                cnt+=1
                self.progressBar.setValue(cnt/self.totLines*100)
                
        file.close()
        QApplication.restoreOverrideCursor()
            
    def loadSBEData(self):
        '''
        uploads SBE files into haul stream data 
        '''
        query=QtSql.QSqlQuery("SELECT device_id FROM device WHERE device_name='SBE'")
        query.first()
        sbeDevice=query.value(0).toString()

        query=QtSql.QSqlQuery("SELECT * FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" and measurement_type='SBEPressure'")
        if query.first():
            reply = QMessageBox.question(self, 'Warning!',"<font size = 14> CLAMSbase has SBE data for this haul.  Do you want to overwrite? </font>", QMessageBox.Yes, QMessageBox.No)
            if reply==QMessageBox.No: 
                return
            else:
                query=QtSql.QSqlQuery("DELETE FROM haul_stream_data WHERE ship=" +
                              self.ship + " AND survey=" + self.survey + " AND haul= " +
                              self.activeHaul +" AND measurement_type in ('SBEPressure', 'SBETemperature')")
                              
        dirDlg=QFileDialog(self)
        fileName=dirDlg.getOpenFileName(self, "Select SBE File","C:/")
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        # get GPS MX420 file 
        file = open(str(fileName))
        cnt=0
        self.progressBar.show()
        for line in file:
            if cnt==0:
                cnt+=1
                continue
            tmp=line.split('\n')
            data =tmp[0].split(',')

            lineTime=QDateTime().fromString(data[4], 'M/d/yyyy hh:mm:ss')
            if lineTime>= self.startTime.addSecs(-3600) and lineTime<= self.endTime.addSecs(+3600):
                query = QtSql.QSqlQuery("INSERT INTO haul_stream_data (ship, survey, haul, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeHaul+","+sbeDevice+",to_timestamp('"+lineTime.toString("MMddyyyy hh:mm:ss.zzz")+
                                "','MMDDYYYY HH24:MI:SS.FF3'),'SBETemperature','"+data[5]+"')")
                query = QtSql.QSqlQuery("INSERT INTO haul_stream_data (ship, survey, haul, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeHaul+","+sbeDevice+",to_timestamp('"+lineTime.toString("MMddyyyy hh:mm:ss.zzz")+
                                "','MMDDYYYY HH24:MI:SS.FF3'),'SBEPressure','"+data[6]+"')")
                self.progressBar.setValue(cnt/(self.totLines/3)*100)
                cnt+=1
                                
        file.close()
        QApplication.restoreOverrideCursor()
        #  get the Haul

    def doneClicked(self):
        self.reject()


    def closeEvent(self, event=None):
        self.reject()


