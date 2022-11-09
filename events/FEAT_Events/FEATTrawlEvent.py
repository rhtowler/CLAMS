"""
The CLAMS FEAT Trawl event dialog. This form provides the FEAT trawl select event form and
actions for CLAMS.
"""

#  import
from PyQt4.QtGui import *
from PyQt4 import QtSql
from ui.xga import ui_FEATTrawlEvent
from ui.xga import ui_FEATEventNum
from ui.xga import ui_FEATEventParams
import numpad
import messagedlg
from datetime import datetime as dt


class FEATTrawlEvent(QDialog, ui_FEATTrawlEvent.Ui_Dialog):
    def __init__(self, parent=None):
        """
        The CLAMS Trawl event dialog initialization method. Gets basic information
        and sets up the haul selection form for FEAT
        """
        #  call superclass init methods and GUI form setup method
        super(FEATTrawlEvent, self).__init__(parent)
        self.setupUi(self)

        #  copy some properties from our parent
        self.db = parent.db
        self.schema = parent.schema
        self.activeEvent = parent.activeEvent
        self.survey = parent.survey
        self.ship = parent.ship
        self.backLogger = parent.backLogger
        self.settings = parent.settings
        self.errorSounds = parent.errorSounds
        self.errorIcons = parent.errorIcons
        self.workStation = parent.workStation
        self.testing = parent.testing

        #  setup reoccurring dialogs
        self.numpad = numpad.NumPad(self)
        self.message = messagedlg.MessageDlg(self)

        # set choose event to disabled
        self.pb_choose.setEnabled(False)
        self.pb_edit.setEnabled(False)

        # set up other variables
        self.gear = ""
        self.event_type = ""
        self.sci = ""
        self.active_partition = ""
        self.active = False
        self.check_active()

        # set connect event to disabled until code is finished in 2020
        # TODO: connect event to net config data
        self.pb_connect.setEnabled(False)

        # set slots
        self.lw_events.currentTextChanged.connect(self.check_events)
        self.pb_choose.clicked.connect(self.choose_event)
        self.pb_add.clicked.connect(self.add_event)
        self.pb_connect.clicked.connect(self.connect_event)
        self.pb_cancel.clicked.connect(self.reject)
        self.cb_active.clicked.connect(self.check_active)
        self.pb_edit.clicked.connect(self.edit_event_num)

    def set_cur_event(self):
        """
        fills the event table and sets the current event text
        :return:
        """
        # set current event
        if self.activeEvent != '0':
            self.l_current.setText("Current Event: " + str(self.activeEvent))
        else:
            self.l_current.setText("Current Event: NONE")

        # fill the list with events in the database
        if not self.active:
            query = QtSql.QSqlQuery("SELECT * FROM Events WHERE survey = '" + str(self.survey) + "' ORDER BY event_id")
        else:
            query = QtSql.QSqlQuery("SELECT * FROM Events WHERE survey = '" + str(self.survey) +
                                    "' AND performance_code != 0 ORDER BY event_id")
        self.lw_events.clear()
        while query.next():
            cur_ev = query.value(2).toString()
            perf = query.value(5).toString()
            if self.activeEvent == cur_ev:
                lst_item = QListWidgetItem(cur_ev + "\tCurrent")
            elif perf == '0':
                lst_item = QListWidgetItem(cur_ev + "\tClosed")
            else:
                # check if already has data
                query2_txt = "SELECT * FROM Samples WHERE event_id = '" + str(cur_ev) + "'"
                query2 = QtSql.QSqlQuery(query2_txt)
                query_size = 0
                if query2.last():
                    query_size += query2.at()
                    query2.first()
                    query2.previous()
                if query_size > 0:
                    lst_item = QListWidgetItem(query.value(2).toString() + "\tStarted")
                else:
                    lst_item = QListWidgetItem(query.value(2).toString() + "\tEmpty")
            self.lw_events.addItem(lst_item)
            if self.activeEvent == cur_ev:
                self.lw_events.setCurrentItem(lst_item)
                self.pb_choose.setEnabled(True)
                # check to see if samples exist
                query3 = QtSql.QSqlQuery("SELECT * FROM Samples WHERE event_id = " + str(cur_ev))
                if query3.first():
                    self.pb_edit.setEnabled(False)
                else:
                    self.pb_edit.setEnabled(True)

    def check_events(self):
        """
        checks to enable the edit number button if there are no samples associated with the
        event and enables the choose button
        :return:
        """
        try:
            if self.lw_events.currentItem().text().contains("Empty"):
                self.pb_edit.setEnabled(True)
            elif self.lw_events.currentItem().text().contains("Current"):
                # check to see if samples exist
                temp_event = self.lw_events.currentItem().text().split("\t")[0]
                query = QtSql.QSqlQuery("SELECT * FROM Samples WHERE event_id = " + str(temp_event))
                if query.first():
                    self.pb_edit.setEnabled(False)
                else:
                    self.pb_edit.setEnabled(True)
            else:
                self.pb_edit.setEnabled(False)
        except:
            self.pb_edit.setEnabled(False)
        self.pb_choose.setEnabled(True)

    def choose_event(self):
        """
        sets the currently selected event from the list as the tow to use and updates the application_configuration
        and the events table
        :return:
        """
        temp_event = self.lw_events.currentItem().text().split("\t")
        self.activeEvent = temp_event[0]
        QtSql.QSqlQuery("UPDATE Application_Configuration SET Parameter_Value = " +
                        str(self.activeEvent + " WHERE Parameter = 'ActiveEvent'"))
        QtSql.QSqlQuery("UPDATE Events SET performance_code=-99 WHERE event_id = " + str(self.activeEvent))
        self.accept()

    def add_event(self):
        """
        adds an event to the database without associated data to get CLAMS going - NC data will be added later
        :return:
        """
        new_event = AddEvent(self.numpad)
        if new_event.result() == 1:
            self.activeEvent = new_event.activeEvent
            other_params = AddParams()
            self.gear = other_params.gear
            self.event_type = other_params.event_type
            self.sci = other_params.sci
            cont = 0

            # check if event already exists in database for this gear and survey
            dup_query = QtSql.QSqlQuery("SELECT * FROM EVENTS WHERE event_id=%s and gear='%s'"
                                        % (self.activeEvent, self.gear))
            if not dup_query.first():
                cont = 1
                values = "(" + self.ship + "," + self.survey + "," + self.activeEvent + ",'" + self.gear + "'," \
                         + self.event_type + ",-99,'" + self.sci + "','')"
                query_txt = "INSERT INTO EVENTS (Ship, Survey, Event_Id, Gear, Event_Type, Performance_Code, " \
                            "Scientist, Comments) VALUES %s" % values
                query = QtSql.QSqlQuery()
                query.prepare(query_txt)
                if query.exec_():
                    self.db.commit()
                    cont = 1
                    # insert into the event_data table
                    # get the current date
                    cur_date = int(dt.strftime(dt.now(), "%Y%m%d"))
                    # enter some event data for the CODEND

                    # enter the date of the event (EventOverallDate)
                    values1 = "(" + self.ship + "," + self.survey + "," + self.activeEvent + ",'Codend'" + \
                              ",'EventOverallDate'," + str(cur_date) + ")"
                    query_txt_1 = "INSERT INTO EVENT_DATA (Ship, Survey, Event_Id, Partition, Event_Parameter, " \
                                  "Parameter_Value) VALUES %s" % values1
                    date_data = QtSql.QSqlQuery()
                    date_data.prepare(query_txt_1)
                    if date_data.exec_():
                        self.db.commit()
                        cont = 1
                        # enter the trawl scientist
                        values2 = "(" + self.ship + "," + self.survey + "," + self.activeEvent + ",'Codend'" + \
                                  ",'TrawlScientist','" + self.sci + "')"
                        query_txt2 = "INSERT INTO EVENT_DATA (Ship, Survey, Event_Id, Partition, Event_Parameter, " \
                                     "Parameter_Value) VALUES %s" % values2
                        ev_data = QtSql.QSqlQuery()
                        ev_data.prepare(query_txt2)
                        if ev_data.exec_():
                            self.db.commit()
                            update_txt = "UPDATE APPLICATION_CONFIGURATION SET parameter_value='%s' WHERE " \
                                         "parameter = 'ActiveEvent'" % self.activeEvent
                            update = QtSql.QSqlQuery()
                            update.prepare(update_txt)
                            if update.exec_():
                                self.db.commit()
                                cont = 1
                                self.set_cur_event()

                            else:
                                cont = 0
                                msg = "Updating the current event in the database failed"
                                self.message.setMessage(self.errorIcons[0], self.errorSounds[0], msg)
                                print("update current event failed")
                        else:
                            cont = 0
                            msg = "Event data 'Trawl Scientist' insert failed"
                            self.message.setMessage(self.errorIcons[0], self.errorSounds[0], msg)
                            print("event data scientist insert failed")
                    else:
                        cont = 0
                        msg = "Event data 'EventOverallDate' insert failed"
                        self.message.setMessage(self.errorIcons[0], self.errorSounds[0], msg)
                        print("event data date insert failed")
                else:
                    cont = 0
                    msg = "Event insert failed"
                    self.message.setMessage(self.errorIcons[0], self.errorSounds[0], msg)
                    print("events insert failed")
                # self.accept()
            else:
                cont = 0
                msg = "That event already exists in the database"
                self.message.setMessage(self.errorIcons[0], self.errorSounds[0], msg)
                print("duplicate entry")
            #if cont == 1:
                #self.accept()

    def connect_event(self):
        """
        takes data from the NC db and connects it to this db for final trawl stats
        :return:
        """
        print("connect event")

    def check_active(self):
        """
        checks the shown events
        :return:
        """
        if self.cb_active.isChecked():
            # show only active events
            self.active = True
        else:
            # show all events
            self.active = False
        self.set_cur_event()

    def edit_event_num(self):
        """
        edits the event number if there are no samples associated with the event
        :return:
        """
        # pull event number out of list item
        temp_event = self.lw_events.currentItem().text().split("\t")[0]
        # check again to make sure there are no samples for the event number
        query = QtSql.QSqlQuery("SELECT * FROM Samples WHERE event_id = " + str(temp_event))
        if query.first():
            # if there are samples, send up msg
            self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                    "There are samples associated with this event "
                                    "number, so it cannot be changed. Please write "
                                    "down the issue in the lab notebook.")
        else:
            # if no samples
            # send up numpad to get new number
            self.numpad.msgLabel.setText("Enter the new event number")
            if not self.numpad.exec_():
                return
            value = self.numpad.value
            # check that number isn't in the database
            query_2 = QtSql.QSqlQuery("SELECT * FROM Events WHERE event_id = " + str(value))
            if query_2.first():
                # if there is an event, send up msg
                self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "That event is already in the "
                                                                                 "database, please choose another")
                self.message.exec_()
            else:
                # if not update the event_data table
                try:
                    QtSql.QSqlQuery("ALTER TABLE Event_Data disable constraint EVENTS_EVENT_DATA_FK")
                    QtSql.QSqlQuery("UPDATE Event_Data SET event_id = " + str(value) + " WHERE event_id = "
                                    + str(temp_event))
                    QtSql.QSqlQuery("ALTER TABLE Event_Data enable constraint EVENTS_EVENT_DATA_FK")
                    # update the event table
                    try:
                        QtSql.QSqlQuery("UPDATE Events SET event_id = " + str(value) + " WHERE event_id = "
                                        + str(temp_event))
                        # update the application_configuration table
                        try:
                            QtSql.QSqlQuery("UPDATE Application_Configuration SET parameter_value = " + str(value) +
                                            "WHERE parameter = 'ActiveEvent'")
                            self.activeEvent = value
                            self.set_cur_event()
                        except:
                            self.message.setMessage(self.errorIcons[1], self.errorSounds[1],
                                                    "Could not update Active Event with the new event id")
                            self.message.exec_()
                    except:
                        self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Could not update Events "
                                                                                         "table with the new event id")
                        self.message.exec_()
                except:
                    self.message.setMessage(self.errorIcons[1], self.errorSounds[1], "Could not update Event_Data "
                                                                                     "table with the new event id")
                    self.message.exec_()


class AddEvent(QDialog, ui_FEATEventNum.Ui_Dialog):
    def __init__(self, numpad):
        """
        allows user to add an event
        """
        super(AddEvent, self).__init__()
        self.setupUi(self)

        self.numpad = numpad
        self.activeEvent = ''

        # set slots
        self.pb_ok.clicked.connect(self.add_event)
        self.pb_cancel.clicked.connect(self.reject)
        self.pb_num.clicked.connect(self.set_event)

        self.exec_()

    def set_event(self):
        """
        sets the event by calling the numpad and changing the text of the button
        :return:
        """
        self.numpad.msgLabel.setText("Enter event num")
        if not self.numpad.exec_():
            return
        self.pb_num.setText(self.numpad.value)

    def add_event(self):
        """
        sets the activeEvent and accepts to send back to enter into database
        :return:
        """
        self.activeEvent = str(self.pb_num.text())
        self.accept()


class AddParams(QDialog, ui_FEATEventParams.Ui_Dialog):
    def __init__(self):
        """
        allows user to add an event
        """
        # TODO: take trawl scientist out of add event
        #  call superclass init methods and GUI form setup method
        super(AddParams, self).__init__()
        self.setupUi(self)

        # set up variables
        self.gear = ""
        self.event_type = ""
        self.sci = "Check NC"

        # fill combo boxes
        self.fill_combos()

        # hide the trawl scientist
        self.label_3.hide()
        self.cb_sci.hide()

        # set slots
        self.pb_ok.clicked.connect(self.add_params)
        self.pb_cancel.clicked.connect(self.reject)

        self.exec_()

    def fill_combos(self):
        """
        fills the combo boxes for the parameters (gear, event type, and scientist
        :return:
        """
        # get gear list
        gear = QtSql.QSqlQuery("SELECT gear FROM GEAR WHERE active=1")
        while gear.next():
            self.cb_gear.addItem(gear.value(0).toString())

        # get event_types
        e_types = QtSql.QSqlQuery("SELECT description FROM EVENT_TYPES")
        while e_types.next():
            self.cb_event_type.addItem(e_types.value(0).toString())

        # get scientists
        scis = QtSql.QSqlQuery("SELECT scientist FROM PERSONNEL WHERE active=1")
        while scis.next():
            self.cb_sci.addItem(scis.value(0).toString())

    def add_params(self):
        """
        adds the parameters to the self and accepts to close the dialog
        :return:
        """
        self.gear = self.cb_gear.currentText()
        self.sci = self.cb_sci.currentText()
        desc = self.cb_event_type.currentText()
        # get event_type_id
        ev_type = QtSql.QSqlQuery("SELECT event_type FROM EVENT_TYPES where description = '" + desc + "'")
        ev_type.first()
        self.event_type = ev_type.value(0).toString()
        self.accept()
