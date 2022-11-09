"""
Special dialog for entering gonad collection data - collection and weight

created by: Alicia Billings - alicia.billings@noaa.gov
date: April 2019
notes:

updated November 2022 to PyQt6 and Python 3 by Alicia Billings, NWFSC
specific updates:
- PyQt import statements
- added some function explanation
- fixed any PEP8 issues
- added a main to test if works (commented out)

todo: test this when able to connect to db
"""

from PyQt6.QtWidgets import *
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtGui import QIcon
from ui.xga import ui_FEATNadDlg
import numpad
import messagedlg
from collections import OrderedDict


class FEATNadDlg(QDialog, ui_FEATNadDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(FEATNadDlg, self).__init__(parent)
        self.setupUi(self)

        self.message = messagedlg.MessageDlg(self)

        self.result = OrderedDict()
        self.survey = parent.survey
        self.ship = parent.ship
        self.activeSpcName = parent.activeSpcName
        self.activeSpcCode = parent.activeSpcCode
        self.active_event = parent.activeHaul
        self.active_sample = parent.activeSample
        self.settings = parent.settings
        self.edit_flag = parent.editFieldFlag
        self.specimen_key = parent.specimenKey
        self.errorIcons = parent.errorIcons
        self.errorSounds = parent.errorSounds
        self.oto_present = False
        self.ip = parent.ip
        self.port = parent.port
        self.printer_connected = parent.printer_connected
        self.printer = parent.printer
        # disable buttons
        self.pb_done.setEnabled(False)

        #  connect signals
        self.pb_take_nad.clicked.connect(self.taken)
        self.pb_nad_wt.clicked.connect(self.get_wt)
        self.pb_done.clicked.connect(self.fin)
        self.pb_cancel.clicked.connect(self.close)

    def setup(self, parent):
        # check for otolith
        self.specimen_key = parent.specimenKey
        self.edit_flag = parent.editFieldFlag
        self.oto_present = self.oto()
        if not self.oto_present:
            # send up dialog to tell them they need to enter an otolith number first
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                    "You must enter an otolith vial number FIRST before collecting gonad information. "
                                    "Please either scan or enter a vial number.", 'info')
            self.message.exec_()
            return
        if self.edit_flag:
            # load all diet samples for that measurement
            self.load_measures()

    def oto(self):
        """
        checks if there is an otolith barcode in the measurements and returns if not
        :return:
        """
        rtn = False
        if self.specimen_key is not None:
            exist_query = QSqlQuery("SELECT * FROM Measurements WHERE ship=" + self.ship +
                                    " AND survey=" + self.survey + " AND event_id=" + self.active_event +
                                    " AND sample_id=" + self.active_sample + " AND specimen_id="
                                    + self.specimen_key + " AND measurement_type = 'barcode'")
            if exist_query.first():
                rtn = True

        return rtn

    def load_measures(self):
        """
        loads the measurements from the database
        :return:
        """
        measures_to_load = ['gonad_collect', 'gonad_weight']
        for measure in measures_to_load:
            query_txt = "SELECT measurement_value FROM Measurements WHERE measurement_type = '%s' " \
                        "AND specimen_id = %s" % (measure, self.specimen_key)
            query = QSqlQuery(query_txt)
            if query.first():
                value = query.value(0).toString()
                if measure == 'gonad_collect':
                    self.l_cur_code.setText(str(value))
                    self.pb_take_nad.setText("Reprint label")
                elif measure == 'gonad_weight':
                    self.pb_nad_wt.setText(str(value))
            else:
                if measure == 'gonad_collect':
                    self.l_cur_code.setText("None")
                elif measure == 'gonad_weight':
                    self.pb_nad_wt.setText("Gonad Weight")

    def taken(self):
        """
        sets the gonad_collection measurement to 'Collected'
        sends up a dialog to print the label with a barcode
        sets the gonad_collect measurement to the barcode number
        :return:
        """
        print_label = GetLabel(self)
        if print_label.result() == 1:
            self.result["gonad_collection"] = "Collected"
            self.result["gonad_collect"] = str(print_label.code)
            self.l_cur_code.setText(str(print_label.code))
            self.pb_done.setEnabled(True)

    def get_wt(self):
        """
        opens a number pad and takes the weight, sets the button text to the weight, and sets the gonad_weight
        :return:
        """
        rst = numpad.NumPad()
        rst.exec()
        self.pb_nad_wt.setText(rst.value)
        self.result['gonad_weight'] = rst.value

    def fin(self):
        """
        sets all of the variables into the result dict and accepts to return
        :return:
        """
        # get values out of the buttons just to be sure
        barcode = self.l_cur_code.text()
        weight = self.pb_nad_wt.text()

        if barcode != "None":
            self.result['gonad_collect'] = barcode
            self.result['gonad_collection'] = "Collected"
        else:
            self.result['gonad_collection'] = "Not collected"
            self.result['gonad_collect'] = "Not collected"
        if weight != "Gonad Weight":
            self.result["gonad_weight"] = weight
        self.accept()

    def closeEvent(self, event):
        self.result = (False, "")
        self.reject()


class GetLabel(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.survey = parent.survey
        self.ship = parent.ship
        self.activeSpcName = parent.activeSpcName
        self.activeSpcCode = parent.activeSpcCode
        self.active_event = parent.active_event
        self.active_sample = parent.active_sample
        self.specimen_key = parent.specimen_key
        self.code = ""
        self.settings = parent.settings
        self.ip = parent.ip
        self.port = parent.port
        self.printer_connected = parent.printer_connected
        self.printer = parent.printer
        self.message = parent.message
        self.errorIcons = parent.errorIcons
        self.errorSounds = parent.errorSounds

        # create the popup
        title = "Print Label"
        win_icon = QIcon()
        win_icon.addFile(self.settings['IconDir'] + "/giant_clam.ico")

        self.setWindowTitle(title)
        self.setFixedWidth(350)
        self.setFixedHeight(100)
        self.setWindowIcon(win_icon)

        print_btn = QPushButton()
        print_btn.setStyleSheet("color: rgb(0, 0, 127); font: 16pt 'Calibri';")
        print_btn.setText("Print Label")
        print_btn.clicked.connect(self.create_label)

        overall_layout = QVBoxLayout()
        overall_layout.addWidget(print_btn)

        self.setLayout(overall_layout)

        self.exec()

    def create_label(self):
        """
        creates the small popup to prompt user to print the label
        :return:
        """
        # create the barcode
        # get the last five of the otolith
        query = QSqlQuery("SELECT measurement_value FROM Measurements WHERE ship=" + self.ship +
                          " AND survey=" + self.survey + " AND event_id=" + self.active_event +
                          " AND sample_id=" + self.active_sample + " AND specimen_id=" + self.specimen_key +
                          " AND measurement_type = 'barcode'")
        query.first()
        last_five = query.value(0).toString()[-5:]
        self.code = str(str(self.survey) + str(self.ship) + str(last_five))

        # set the project
        project = "FEAT Gonad Collection"

        # get the ship name
        query_txt = "SELECT name FROM Ships WHERE ship=" + self.ship
        query = QSqlQuery(query_txt)
        query.first()
        ship_name = query.value(0).toString()
        if self.printer is not None:
            if self.printer_connected:
                # test again, just to be sure
                if self.printer.printer_status():
                    self.printer.print_label(project, self.activeSpcName,
                                             self.activeSpcCode, self.active_event, self.code)
                else:
                    self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                            "Printer not responding, please use a paper label",
                                            'info')
                    self.message.exec_()
            else:
                self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                        "Printer not responding, please use a paper label",
                                        'info')
                self.message.exec_()
        else:
            self.message.setMessage(self.errorIcons[2], self.errorSounds[2],
                                    "No printer is configured for this station, please use a paper label",
                                    'info')
            self.message.exec_()

        self.accept()

    def closeEvent(self, QCloseEvent):
        self.reject()
