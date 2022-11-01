from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_NetDlg
import numpad

class NetDlg(QDialog, ui_NetDlg.Ui_netDlg):

    def __init__(self, parent=None):
        super(NetDlg, self).__init__(parent)
        self.setupUi(self)
        self.settings=parent.settings
        self.db = parent.db
        self.backLogger = parent.backLogger
        self.activeEvent=parent.activeEvent
        self.survey=parent.survey
        self.ship=parent.ship
        self.defTime=QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss.zzz')
        self.reloaded=parent.reloaded
        self.buttons=[self.btn1,self.btn2,self.btn3,self.btn4]
        self.measurements=['NetVerticalOpening', 'NetHorizontalOpening','HeadRopeDepth','TrawlWireOut']
        self.timeDlg = parent.timeDlg
        self.setTime=None
        self.editFlag=False
        self.doneEditing=False

        self.numpad=numpad.NumPad(self)
        #  set up signals
        for btn in self.buttons:
            self.connect(btn, SIGNAL("clicked()"), self.getValue)
            btn.setText('')

        self.connect(self.okBtn, SIGNAL("clicked()"), self.doneClicked)
        self.connect(self.addRecordBtn, SIGNAL("clicked()"), self.addRecord)
        self.connect(self.deleteBtn, SIGNAL("clicked()"), self.deleteRecord)
        self.connect(self.netTable, SIGNAL("itemSelectionChanged()"),  self.editData)
        if self.reloaded:
            self.reloadData()
            query=QtSql.QSqlQuery("SELECT to_char(min(time_stamp), 'MMDDYYYY HH24:MI:SS.FF3') FROM event_stream_data WHERE ship="+self.ship+
            " AND survey="+self.survey+" AND event_id="+self.activeEvent)
            query.first()
            self.minTime=QDateTime().fromString(query.value(0).toString(), 'MMddyyyy hh:mm:ss.zzz')
            query=QtSql.QSqlQuery("SELECT to_char(max(time_stamp), 'MMDDYYYY HH24:MI:SS.FF3') FROM event_stream_data WHERE ship="+self.ship+
            " AND survey="+self.survey+" AND event_id="+self.activeEvent)
            query.first()
            self.maxTime=QDateTime().fromString(query.value(0).toString(), 'MMddyyyy hh:mm:ss.zzz')

    def reloadData(self):
        # get times
        self.netTable.clearContents()
        self.netTable.setRowCount(0)
        query=QtSql.QSqlQuery("SELECT to_char(time_stamp,'MMDDYYYY HH24:MI:SS.FF3') FROM event_stream_data WHERE ship="+
                self.ship+ " AND survey="+self.survey+" AND event_id="+self.activeEvent+
                " AND measurement_type IN('NetVerticalOpening','NetHorizontalOpening','HeadRopeDepth'," +
                "'TrawlWireOut') GROUP BY time_stamp ORDER BY time_stamp ASC")
        row=0
        while query.next():
            self.netTable.insertRow(self.netTable.rowCount())
            self.netTable.setItem(row, 0,QTableWidgetItem(query.value(0).toString()))
            for i in range(len(self.measurements)):
                query1=QtSql.QSqlQuery("SELECT measurement_value FROM event_stream_data WHERE ship="+self.ship+
                " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND measurement_type='"+self.measurements[i]+
                "' AND time_stamp=to_timestamp('"+query.value(0).toString()+"','MMDDYYYY HH24:MI:SS.FF3')")
                if query1.first():
                    self.netTable.setItem(row, i+1,QTableWidgetItem(query1.value(0).toString()))
                else:
                    self.netTable.setItem(row, i+1,QTableWidgetItem(''))
            row+=1

        self.netTable.resizeColumnsToContents()
        self.netTable.scrollToBottom()

    def editData(self):
        if self.doneEditing:
            self.doneEditing=False
            return
        for i in range(4):
            if self.netTable.item(self.netTable.currentRow(), i+1):
                self.buttons[i].setText(self.netTable.item(self.netTable.currentRow(), i+1).text())
        self.editFlag=True
        self.addRecordBtn.setText('Update \nRecord')


    def deleteRecord(self):
        if self.netTable.currentRow()>-1:
            delTime=self.netTable.item(self.netTable.currentRow(),0).text()
            query = QtSql.QSqlQuery("DELETE FROM event_stream_data WHERE measurement_type IN"+
                    "('NetVerticalOpening', 'NetHorizontalOpening','HeadRopeDepth','TrawlWireOut') "+
                    "AND time_stamp=to_timestamp('"+delTime+"', 'MMDDYYYY HH24:MI:SS.FF3') ")
            self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
            self.reloadData()
            self.addRecordBtn.setText('Add \nRecord')
            self.editFlag=False

    def getValue(self):
        self.numpad.msgLabel.setText("Enter value")
        if not self.numpad.exec_():
            return
        ind=self.buttons.index(self.sender())
        self.buttons[ind].setText(self.numpad.value)


    def addRecord(self):
        # update record
        if self.editFlag:
            for i in range(len(self.measurements)):
                if not self.buttons[i].text()=='':
                    query=QtSql.QSqlQuery("SELECT * FROM event_stream_data WHERE ship="+self.ship+
                        " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND measurement_type='"+self.measurements[i]+
                        "' AND time_stamp=to_timestamp('"+self.netTable.item(self.netTable.currentRow(), 0).text()+"','MMDDYYYY HH24:MI:SS.FF3')")
                    if not query.first():
                        query = QtSql.QSqlQuery("INSERT INTO event_stream_data (ship, survey, event_id, device_id, time_stamp, measurement_type, measurement_value) "+
                                "VALUES ("+self.ship+","+self.survey+","+self.activeEvent+",0,to_timestamp('"+
                                self.netTable.item(self.netTable.currentRow(), 0).text()+"','MMDDYYYY HH24:MI:SS.FF3'),'"+self.measurements[i]+
                                "','"+self.buttons[i].text()+"')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                    else:
                        query = QtSql.QSqlQuery("UPDATE event_stream_data SET measurement_value='"+self.buttons[i].text()+"' WHERE ship="+self.ship+
                            " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND measurement_type='"+self.measurements[i]+
                            "' AND time_stamp=to_timestamp('"+self.netTable.item(self.netTable.currentRow(), 0).text()+"','MMDDYYYY HH24:MI:SS.FF3')")
                        self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())
                else:
                    query = QtSql.QSqlQuery("DELETE FROM event_stream_data WHERE ship="+self.ship+
                        " AND survey="+self.survey+" AND event_id="+self.activeEvent+" AND measurement_type='"+self.measurements[i]+
                        "' AND time_stamp=to_timestamp('"+self.netTable.item(self.netTable.currentRow(), 0).text()+"','MMDDYYYY HH24:MI:SS.FF3')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())


            self.editFlag=False
            self.addRecordBtn.setText('Add \nRecord')
            self.doneEditing=True
            self.netTable.clearSelection()
        else:# new record

            if self.reloaded:
                self.timeDlg.setTime(self.defTime)
                if self.timeDlg.exec_():
                    if self.timeDlg.qTime<self.minTime or self.timeDlg.qTime>self.maxTime:
                        QMessageBox.critical(self, "ERROR", "<font size = 12> This time is not valid for this event_id.")
                        return
                    self.setTime=self.timeDlg.time

                else:
                    QMessageBox.critical(self, "ERROR", "<font size = 12> Must... Have... Time...")
                    return
            else:
                if self.setTime==None:
                    self.setTime=QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss.zzz')
            for i in range(4):
                if not self.buttons[i].text()=='':
                    query = QtSql.QSqlQuery("INSERT INTO event_stream_data (ship, survey, event_id, device_id, time_stamp," +
                            "measurement_type, measurement_value) VALUES ("+self.ship+","+self.survey+","+self.activeEvent+
                            ",0,to_timestamp('"+self.setTime+ "','MMDDYYYY HH24:MI:SS.FF3'),'"+self.measurements[i]+"','"+
                            self.buttons[i].text()+"')")
                    self.backLogger.info(QDateTime.currentDateTime().toString('MMddyyyy hh:mm:ss')+","+query.lastQuery())

        self.setTime=None
        self.reloadData()

    def doneClicked(self):
        self.close()

    def closeEvent(self, event=None):
        self.accept()


