#!/usr/bin/env python
"""

sbeTester provides an example of using the sbe39 class to interact with an
SBE 39 bathythermograph.

"""

#  add the UI files to the python path
import sys
import os
pyPath = reduce(lambda l,r: l + os.path.sep + r, os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
sys.path.append(os.path.join(pyPath, 'ui'))


#  import dependent modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_sbeTester
import sbeSetInterval
from acquisition.serial import sbe39
#  the progress dialog is only required if you want to display download progess
from acquisition.serial import sbeProgressDialog


class sbeTester(QMainWindow, ui_sbeTester.Ui_sbeTester):

    def __init__(self, comPort, parent=None):
        super(sbeTester, self).__init__(parent)
        self.setupUi(self)

        self.comPort = comPort
        self.__dataText = []
        self.__maxDataTextLines = 500


        #  create an instance of the set interval dialog
        self.sbeIntervalDlg = sbeSetInterval.sbeSetInterval()

        #  connect the dialog's sbeSetInterval signal - emitted when the user clicks o.k.
        #  on the sbeSetInterval dialog
        self.connect(self.sbeIntervalDlg, SIGNAL("sbeSetInterval"), self.intervalSet)


        #  create an instance of the SBE39 class
        self.sbe = sbe39.sbe39(self.comPort)

        #  connect the SBE39's signals - The SBE39 class emits a load of signals. Not all signals
        #  are required for typical use but all of them are listed here in this example for reference.

        #  SBEStatus signal is emitted after a status request - args are (device name, status dictionary)
        self.connect(self.sbe, SIGNAL("SBEStatus"), self.updateStatus)

        #  SBECalibration signal is emitted after a calibration parameter request (DC)
        #  args are (device name calParms dictionary)
        self.connect(self.sbe, SIGNAL("SBECalibration"), self.updateCalParms)

        #  SBEConnected signal is emitted after a successful connection is established. Args are (device name)
        self.connect(self.sbe, SIGNAL("SBEConnected"), self.connected)

        #  SBETimeout is emitted when a connection times out. Args are (device name). The connection can time out
        #  right after you try to connect, or at any other time if communication is lost
        self.connect(self.sbe, SIGNAL("SBETimeout"), self.sbeTimeout)

        #  SBEData is emitted when a line of data is received from the SBE. ANY data.
        #  This would only be used if you wanted to monitor the output of the device.
        #  Args are (device name, line of data as string)
        self.connect(self.sbe, SIGNAL("SBEData"), self.showSBEData)

        #  SBEProgress is emitted during download. Args are (device name, progress (float as pct))
        self.connect(self.sbe, SIGNAL("SBEProgress"), self.showProgress)

        #  SBEDownloadComplete is emitted when downloading is complete.
        #  Args are (device name, n records downloaded, n records dropped/lost)
        self.connect(self.sbe, SIGNAL("SBEDownloadComplete"), self.downloadComplete)

        #  SBEDownloadData is emitted for each line of data downloaded.
        #  Args are (device name, [time (as datetime obj), temp (as float), pressure (as float)])
        self.connect(self.sbe, SIGNAL("SBEDownloadData"), self.downloadingData)

        #  SBEAbort is emitted for each line of data downloaded. Args are (device name)
        self.connect(self.sbe, SIGNAL("SBEAbort"), self.downloadAbort)


        #  connect this GUI's button signals
        self.connect(self.actionExit, SIGNAL("triggered()"), SLOT('close()'))
        self.connect(self.actionSetInterval, SIGNAL("triggered()"), self.setInterval)
        self.connect(self.statusButton, SIGNAL("clicked()"), self.__status)
        self.connect(self.downloadButton, SIGNAL("clicked()"), self.__download)
        self.connect(self.setTimeButton, SIGNAL("clicked()"), self.__setTime)
        self.connect(self.connectButton, SIGNAL("clicked()"), self.__connect)
        self.connect(self.disconnectButton, SIGNAL("clicked()"), self.__disconnect)
        self.connect(self.startButton, SIGNAL("clicked()"), self.__startLogging)
        self.connect(self.stopButton, SIGNAL("clicked()"), self.__stopLogging)

        #  set up the button states
        self.__setGUIButtons(False)


        #  create an instance of the SBE progress dialog - this dialog shows download progress
        #  and it also has an abort button. You pass it the reference to the sbe object and it
        #  handles the signals internally. You just need to show and hide it.
        self.sbeProgress = sbeProgressDialog.sbeProgressDialog(self.sbe, parent=self)


        #  restore the application state
        self.__appSettings = QSettings('afsc.noaa.gov', 'SBETester')
        size = self.__appSettings.value('winsize', QSize(660,700)).toSize()
        self.resize(size)
        position = self.__appSettings.value('winposition', QPoint(10,10)).toPoint()
        self.move(position)
        self.__saveDir = self.__appSettings.value('savedir', QDir.home().path()).toString()


    def showProgress(self, device, pctComplete):
        #  this is just here as a stub since we're using the SBE progress dialog to display
        #  progress. If you use the SBE progress dialog you don't need to connect the progress
        #  signal nor implement this function
        pass


    def downloadComplete(self, device, nDownloaded, nDropped):

        #  hide and reset the progress dialog
        self.sbeProgress.hide()
        self.sbeProgress.reset()

        #  close the output file
        self.fileObj.close()

        #  reconnect the SBEData signal
        self.connect(self.sbe, SIGNAL("SBEData"), self.showSBEData)

        #  show a temporary message on the status bar
        self.statusbar.showMessage('Download complete.', 5000)


    def downloadAbort(self):
        #  hide and reset the progress dialog
        self.sbeProgress.hide()
        self.sbeProgress.reset()

        #  close the output file
        self.fileObj.close()

        #  reconnect the SBEData signal
        self.connect(self.sbe, SIGNAL("SBEData"), self.showSBEData)

        #  show a temporary message on the status bar
        self.statusbar.showMessage('Downloading aborted.', 5000)


    def downloadingData(self, device, line):

        try:
            mdy = '{:02d}/{:02d}/{:04d}'.format(line[0].month, line[0].day, line[0].year)
            hms = '{:02d}:{:02d}:{:02d}'.format(line[0].hour, line[0].minute, line[0].second +
                                                int(round(line[0].microsecond/1000000.)))
            textLine = mdy + ' ' + hms + ',' + str(line[1]) + ',' + str(line[2]) + '\n'
            self.fileStream << textLine

        except Exception, e:
            #  there was an error writing to the file
            self.sbe.abort()
            msgBox = QMessageBox.critical(self, 'Error', 'Error writing to file ' + self.saveFile)


    def __connect(self):

        #  attempt to connect to the SBE - do this in a try block so we can capture any errors from
        #  SerialMonitor to display in a dialog
        try:
            self.statusbar.showMessage('Trying to wake SBE...')
            self.sbe.connect()
        except Exception, e:
             msgBox = QMessageBox.critical(self, 'Error', 'Unable to connect to SBE on COM' + str(self.comPort+1))


    def __disconnect(self):

        #  disconnect the SBE
        self.sbe.disconnect()

        #  update the GUI
        self.__setGUIButtons(False)
        self.__clearGUI()


    def connected(self, device):

        #  show a temporary message on the status bar
        self.statusbar.showMessage('Connected to ' + device, 5000)

        #  set up the GUI
        self.__setGUIButtons(True)

        #  get the status and calibration parameters from the SBE
        self.sbe.getStatus()
        self.sbe.getCalParms()


    def __startLogging(self):

        ok = QMessageBox.question(self, 'Start Logging', 'Reset the sample number to 0 and start logging? \n' +
                                      'Existing data will be overwritten!', QMessageBox.Ok | QMessageBox.Cancel)

        if (ok == QMessageBox.Ok):
            self.sbe.setSampleNumber(0)
            self.sbe.startNow()


    def __stopLogging(self):
        self.sbe.stop()


    def updateStatus(self, device, status):

        #  pupulate the GUI fields with data
        self.sampInterval.setText(status['sample interval'])
        self.loggingStatus.setText(status['logging status'])
        self.binaryUpload.setText(status['binary upload config'])
        self.realtimeOutput.setText(status['real-time output'])
        self.serialSync.setText(status['serial sync'])
        self.serialNumber.setText(status['serial number'])
        self.firmwareVersion.setText(status['version'])
        self.voltage.setText(status['voltage'])
        self.currentSample.setText(status['sample number'])
        self.freeSamples.setText(status['sample free'])
        self.configuration.setText(status['configuration'])
        self.temperature.setText(status['temperature'])
        self.currentTime.setText(status['time'].strftime("%m/%d/%Y  %H:%M:%S"))


    def updateCalParms(self, device, calibration):

        #  pupulate the GUI fields with data
        self.tempCalDate.setText(calibration['temp cal date'])
        self.presCalDate.setText(calibration['pressure cal date'])
        self.presRange.setText(calibration['pressure range'])
        self.presSerialNum.setText(calibration['pressure s/n'])
        self.TA0.setText(str(calibration['TA0']))
        self.TA1.setText(str(calibration['TA1']))
        self.TA2.setText(str(calibration['TA2']))
        self.TA3.setText(str(calibration['TA3']))
        self.PA0.setText(str(calibration['PA0']))
        self.PA1.setText(str(calibration['PA1']))
        self.PA2.setText(str(calibration['PA2']))
        self.PTHA0.setText(str(calibration['PTHA0']))
        self.PTHA1.setText(str(calibration['PTHA1']))
        self.PTHA2.setText(str(calibration['PTHA2']))
        self.PTCA0.setText(str(calibration['PTCA0']))
        self.PTCA1.setText(str(calibration['PTCA1']))
        self.PTCA2.setText(str(calibration['PTCA2']))
        self.PTCB0.setText(str(calibration['PTCB0']))
        self.PTCB1.setText(str(calibration['PTCB1']))
        self.PTCB2.setText(str(calibration['PTCB2']))


    def sbeTimeout(self):

        msgBox = QMessageBox.critical(self, 'Error', 'Unable to connect or lost connection to SBE on COM' + str(self.comPort+1))

        self.__setGUIButtons(False)


    def intervalSet(self, interval, rto):
        #  this method is called when the sbeSetInterval signal is received meaning the
        #  user has set a new sampling interval.

        self.sbe.setSamplingInterval(interval)
        self.sbe.setTxRealTime(rto)


    def setInterval(self):

        #  get the current interval and RealTime Output values
        rtoText = self.sbe.status.get('real-time output', 'not')
        if (rtoText.lower().find('not') > -1) or (rtoText.lower().find('disabled') > -1):
            rto = False
        else:
            rto = True
        interval = int(self.sbe.status.get('sample interval', '0').split()[0])

        #  set the values in the dialog and show
        self.sbeIntervalDlg.setInterval(interval, rto)
        self.sbeIntervalDlg.show()


    def __setGUIButtons(self, state):

        self.connectButton.setEnabled(not state)
        self.actionSetInterval.setEnabled(state)
        self.disconnectButton.setEnabled(state)
        self.statusButton.setEnabled(state)
        self.setTimeButton.setEnabled(state)
        self.startButton.setEnabled(state)
        self.stopButton.setEnabled(state)
        self.downloadButton.setEnabled(state)


    def __clearGUI(self):

        #  clear out the GUI fields
        self.sampInterval.setText('')
        self.loggingStatus.setText('')
        self.binaryUpload.setText('')
        self.realtimeOutput.setText('')
        self.serialSync.setText('')
        self.serialNumber.setText('')
        self.firmwareVersion.setText('')
        self.voltage.setText('')
        self.currentSample.setText('')
        self.freeSamples.setText('')
        self.configuration.setText('')
        self.temperature.setText('')
        self.currentTime.setText('')

        self.tempCalDate.setText('')
        self.presCalDate.setText('')
        self.presRange.setText('')
        self.presSerialNum.setText('')
        self.TA0.setText('')
        self.TA1.setText('')
        self.TA2.setText('')
        self.TA3.setText('')
        self.PA0.setText('')
        self.PA1.setText('')
        self.PA2.setText('')
        self.PTHA0.setText('')
        self.PTHA1.setText('')
        self.PTHA2.setText('')
        self.PTCA0.setText('')
        self.PTCA1.setText('')
        self.PTCA2.setText('')
        self.PTCB0.setText('')
        self.PTCB1.setText('')
        self.PTCB2.setText('')


    def __status(self):

        self.sbe.getStatus()


    def __setTime(self):

        #  calling the setRTC method with no arguments sets the time to the PC's UTC time
        self.sbe.setRTC()


    def __download(self):


        #  get the filename and path
        saveFile = QFileDialog.getSaveFileName(self, 'Save SBE data to:', self.__saveDir,
                                               'All Files (*.*)')

        if saveFile:
            #  update the application settings with the data directory
            dirName = str(saveFile).rsplit('/',1)[0]
            self.__appSettings.setValue('savedir', dirName)
            self.__saveDir = dirName
            self.saveFile = saveFile

            try:
                self.fileObj = QFile(self.saveFile)
                self.fileObj.open(QIODevice.WriteOnly | QIODevice.Truncate | QIODevice.Text)
                self.fileStream = QTextStream(self.fileObj)
                self.fileStream.setCodec("UTF-8")

                #  write the header line to the file
                self.fileStream << "DATE_TIME, TEMPERATURE, PRESSURE(dbars)\n"

                #  show the progess dialog
                self.sbeProgress.show()

                #  disconnect the SBEData signal since displaying the data during
                #  download slows the download down significantly.
                self.disconnect(self.sbe, SIGNAL("SBEData"), self.showSBEData)

                #  download all samples for previous logging session - calling download with
                #  no arguments will download all samples from 0 to the current sample.
                #  NOTE THAT YOU MUST UPDATE THE STATUS OF THE DEVICE AFTER IT IS STOPPED TO
                #  MAKE SURE THAT SAMPLE NUMBER IS UP TO DATE.

                self.sbe.download()

            except Exception, e:
                #  there was an error writing to the file
                if self.fileObj:
                    self.fileObj.close()
                msgBox = QMessageBox.critical(self, 'Error', 'Error writing to file ' + self.saveFile)


    def showSBEData(self, name, val):

        if val:
            #  update the display with this new line of text
            text = '<text style="color:black">' + val + '<br />'
            self.__dataText.append(text)
            if len(self.__dataText) > self.__maxDataTextLines:
                self.__dataText.pop(0)
            text = ''.join(self.__dataText)
            text = QString('<html><body><p>' + text + '</p></body></html>')
            self.dataText.setHtml(text)

            #  ensure that the window is scrolled to see the new line of text.
            self.dataText.verticalScrollBar().setValue(self.dataText.verticalScrollBar().maximum())



    def closeEvent(self, event=None):

        self.sbe.disconnect()

        self.__appSettings.setValue('winposition', self.pos())
        self.__appSettings.setValue('winsize', self.size())



if __name__ == "__main__":

    #  SET THE COM PORT NUMBER HERE - NOTE THAT ON WINDOWS YOU SPECIFY THE COM PORT
    #  NUMBER AS ONE LESS THAN REPORTED "COMX" NUMBER. For example "COM3" would be
    #  specified as 2.
    comPort = 14

    app = QApplication(sys.argv)
    form = sbeTester(comPort)
    form.show()
    app.exec_()
