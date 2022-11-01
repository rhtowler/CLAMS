
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_EventSelDlg
import numpad

class EventSelDlg(QDialog, ui_EventSelDlg.Ui_eventselDlg):

    def __init__(self, parent=None, eventType=None):
        super(EventSelDlg, self).__init__(parent)
        self.setupUi(self)

        self.activeEvent = None
        self.eventTable.setRowCount(0)
        cnt=0

        # setup some bits
        self.numpad = numpad.NumPad(self)
        self.eventTable.verticalHeader().setVisible(False)
        self.eventTable.setColumnWidth(0, 60)
        self.eventTable.setColumnWidth(1, 150)
        self.eventTable.setColumnWidth(2, 250)
        self.eventTable.scrollToBottom()
        self.ship=parent.ship
        self.survey=parent.survey

        #  this was changed (I think by Robert Levine) to handle "non catch" events but
        #  this needs to be re-thought since he's hard coded filters based on gear type.
        #  At the very least the filtering could be handled by the "retains_catch"
        #  column of gear_types.

        #  I'm assuming he passes in eventType when this object is created

        # Populate the GUI
        if eventType != None:
            query = QtSql.QSqlQuery("SELECT a.event_id, a.gear FROM (select event_id, gear, "+
                "ship, survey from events )a JOIN (select gear, gear_type from gear) b on a.gear = b.gear "+
                "WHERE a.ship = "+parent.ship+" AND a.survey= "+parent.survey+
                "  AND b.gear_type = '"+eventType+"'  ORDER BY event_id ASC")
        else:
            # CHANGE THIS TO WHERE GEAR IS NOT CTD OR MOORING OR SEABIRD
            query = QtSql.QSqlQuery("SELECT a.event_id, a.gear FROM (select event_id, gear, "+
                "ship, survey from events )a JOIN (select gear, gear_type from gear) b on a.gear = b.gear "+
                "WHERE a.ship = "+parent.ship+" AND a.survey= "+parent.survey+
                "  AND b.gear_type <> 'Mooring_Station' AND  b.gear_type <> 'CTD_Station' "+
                " AND b.gear_type <> 'Seabird_Station' ORDER BY event_id ASC")

        #  loop through the events
        while query.next():
            #  add the event number
            self.eventTable.insertRow(cnt)
            self.eventTable.setItem(cnt, 0, QTableWidgetItem(query.value(0).toString()))
            if eventType !=None:
                query1 = QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE (event_parameter='EQ'" +
                        " OR event_parameter = 'TimeStamp' OR event_parameter = 'Released') "
                        " AND event_id=" +query.value(0).toString() + " AND ship=" + parent.ship +
                        " AND survey=" + parent.survey)
                hbTime = query1.first()
                if hbTime:
                    #  event is closed - insert the gear in black text
                    self.eventTable.setItem(cnt, 1, QTableWidgetItem(query.value(1).toString()))
                    self.eventTable.setItem(cnt, 2, QTableWidgetItem(query1.value(0).toString()))
                else:
                    #  event is not closed - insert the gear text with a pink background
                    item = QTableWidgetItem(query.value(1).toString())
                    brush = QBrush(QColor(250, 200, 200))
                    brush.setStyle(Qt.SolidPattern)
                    item.setBackground(brush)
                    self.eventTable.setItem(cnt, 1, item)
            else:
                #  check if the event is "closed" defined by having a HB time
                query1 = QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE event_parameter='Haulback'" +
                        " AND event_id=" +query.value(0).toString() + " AND ship=" + parent.ship +
                        " AND survey=" + parent.survey)
                hbTime = query1.first()

                #  I don't know where this code came from but we don't define an event
                #  complete when there isn't a HB time. It is commented out because of this.
#                query2 = QtSql.QSqlQuery("SELECT parameter_value FROM event_data WHERE event_parameter='EQ'" +
#                        " AND event_id=" +query.value(0).toString() + " AND ship=" + parent.ship +
#                        " AND survey=" + parent.survey)
#                eqTime = query2.first()
                if hbTime:
                    #  event is closed - insert the gear in black text
                    self.eventTable.setItem(cnt, 1, QTableWidgetItem(query.value(1).toString()))
                    self.eventTable.setItem(cnt, 2, QTableWidgetItem(query1.value(0).toString()))
#                elif eqTime:
#                    self.eventTable.setItem(cnt, 1, QTableWidgetItem(query.value(1).toString()))
#                    self.eventTable.setItem(cnt, 2, QTableWidgetItem(query2.value(0).toString()))
                else:
                    #  event is not closed - insert the gear text with a pink background
                    item = QTableWidgetItem(query.value(1).toString())
                    brush = QBrush(QColor(250, 200, 200))
                    brush.setStyle(Qt.SolidPattern)
                    item.setBackground(brush)
                    self.eventTable.setItem(cnt, 1, item)
            cnt+=1

        self.eventTable.scrollToBottom()
        #  connect signals and slots
        if eventType != None:
            self.newEventBtn.setText('Start New '+eventType+' Event')
        else:
            self.newEventBtn.setText('Start New Trawl Event')
        self.connect(self.newEventBtn, SIGNAL("clicked()"),self.getNewEvent)
        self.connect(self.cancelBtn, SIGNAL("clicked()"),self.goExit)
        self.connect(self.okBtn, SIGNAL("clicked()"),self.goOn)
        self.connect(self.eventTable, SIGNAL("itemSelectionChanged()"),self.getPrevEvent)


    def getNewEvent(self):
        eventList=[]
        query= QtSql.QSqlQuery("Select event_id from events where survey ="+
            self.survey+"and ship= "+self.ship+" ORDER BY event_id ASC")
        while query.next():
            eventList.append(int(query.value(0).toString()))
       # for i in range(self.eventTable.rowCount()):
        #   eventList.append(int(self.eventTable.item(i, 0).text()))
        if len(eventList)>0:
            lastEvent=max(eventList)
        else:
            lastEvent=0

        self.activeEvent=str(lastEvent+1)
        self.eventTable.insertRow(self.eventTable.rowCount())
        self.eventTable.setItem(self.eventTable.rowCount()-1, 0, QTableWidgetItem(self.activeEvent))

        self.goOn()
        self.reloaded=False


    def getPrevEvent(self):
        self.activeEvent=self.eventTable.item(self.eventTable.currentRow(), 0).text()
        self.reloaded=True


    def goOn(self):
        self.accept()


    def goExit(self):
        self.reject()

