'''

sensorLogger is a basic application that acts like a simplified SCS
server. It maps serial devices such as GPS receivers to "sensors"
which are parsed data elements received from the devices. An example
sensor would be "GPS_Lat" which would be the latitude value from the
GPS.

Device and sensor names are arbitrary and their configuration is defined
in an xml file. The device section contains all of the defined devices.
Device and sensor names must be unique.
Device sections must include a name, comport, and baud
Sensor sections must contain:
        name
        nmea_source which defines the NMEA string that will be parsed
        parse_type: specifies how the string will be parsed. Values are
                    'delimited' - parsed using a delimiter
                    'regex' - parsed using a regular expression
                    'none' - not parsed
        parse_expression: is the delimiter if the parse type is delimited and
                        it is the regular expression if the parse type is regex.
        parse_index: is a comma separated list of indicies into the parsed NMEA
                     string. If multiple indicies are provided, the elements they
                     define will be concatenated together (without delimiter)

<devices>
    <device name="GPS" comport="COM11" baud="4800">
        <logger nmea_source="$GPGGA"/>
        <logger nmea_source="$GPRMC"/>
        <sensor name="GPS-GPRMC-RAW" nmea_source="$GPRMC" parse_type="none" parse_expression="" parse_index=""/>
        <sensor name="GPS-Lat" nmea_source="$GPRMC" parse_type="delimited" parse_expression="," parse_index="3,4"/>
        <sensor name="GPS-Lon" nmea_source="$GPRMC" parse_type="delimited" parse_expression="," parse_index="5,6"/>
        <sensor name="GPS-SOG" nmea_source="$GPRMC" parse_type="delimited" parse_expression="," parse_index="7"/>
        <sensor name="GPS-TMG" nmea_source="$GPRMC" parse_type="delimited" parse_expression="," parse_index="8"/>
    </device>
</devices>


Rick Towler
NOAA Alaska Fisheries Science Center
rick.towler@noaa.gov

'''

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import string
import datetime
import re
from PyQt4 import QtCore, QtGui
from xml.etree import ElementTree as ET
from acquisition.scs import QSCSServer
from acquisition.serial import SerialMonitor
from ui import ui_sensorLogger


class sensorLogger(QtGui.QMainWindow, ui_sensorLogger.Ui_sensorLogger):

    def __init__(self, iniFile=None):
        #  initialize the superclasses
        super(sensorLogger, self).__init__(None)

        #  initialize the GUI form
        self.setupUi(self)

        #  set the base directory path - this is the full path to this application
        self.baseDir = reduce(lambda l,r: l + os.path.sep + r,
                os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))

        #  initialize default properties
        self.saveData = False
        self.saveDataPath = self.baseDir + os.path.sep + 'data'
        self.serverIP = '0.0.0.0'
        self.serverPort = 5005
        self.scsServer = None
        self.maxDisplayLines = 500
        self.displayText = []
        self.loggers = {}
        self.logFlushInterval = 5 * 60 * 1000

        if (iniFile):
            self.configFile = os.path.normpath(iniFile)
        else:
            self.configFile = os.path.normpath(self.baseDir + os.path.sep +
                    'sensorLogger.xml')

        #  create an instance of the serial monitor
        self.serialMonitor = SerialMonitor.SerialMonitor()
        self.connect(self.serialMonitor, QtCore.SIGNAL("SerialDataReceived"), self.receiveDeviceData)

        #  restore the GUI state
        appSettings = QtCore.QSettings('afsc.noaa.gov', 'sensorLogger')
        size = appSettings.value('winsize', QtCore.QSize(700,400)).toSize()
        self.resize(size)
        position = appSettings.value('winposition', QtCore.QPoint(10,10)).toPoint()
        self.move(position)

        try:
            self.setWindowIcon(QtGui.QIcon(self.baseDir + os.sep + 'icons/echoIcon.png'))
        except:
            pass

        #  create a label in the status bar
        self.SCSServerLabel = QtGui.QLabel('')
        self.statusbar.addPermanentWidget(self.SCSServerLabel)

        #  create the timer that we'll use to periodically flush the log data to disk
        self.logFlushTimer = QtCore.QTimer(self)
        self.logFlushTimer.timeout.connect(self.flushLogBuffers)

        #  start the logger
        initTimer = QtCore.QTimer(self)
        initTimer.setSingleShot(True)
        initTimer.timeout.connect(self.startLogging)
        initTimer.start(1)


    def startLogging(self):

        #  read the configuration file
        if (not os.path.isfile(self.configFile)):
            errorText = 'Unable to find the sensorLogger configuration file: ' + \
                    self.configFile
            QtGui.QMessageBox.critical(self, 'Error', errorText)
            self.close()
            return
        try:
            tree = ET.parse(self.configFile)
        except:
            errorText = 'Unable to parse the sensorLogger configuration file: ' + \
                    self.configFile
            QtGui.QMessageBox.critical(self, 'Error', errorText)
            self.close()
            return

        #  note the day of the year - this is uesed to handle log file rollovers
        self.dayOfYear = datetime.datetime.now().timetuple().tm_yday

        #  get the root of the XML file
        root = tree.getroot()

        #  process the application section
        for section in root:
            if (section.tag.lower() == 'application'):
                for c in section:
                    if (c.tag.lower() == 'log_data'):
                        if (c.text.lower() == 'true'):
                            self.saveData = True
                    if (c.tag.lower() == 'log_data_path'):
                        self.saveDataPath = os.path.normpath(c.text)
                    if (c.tag.lower() == 'log_flush_interval'):
                        try:
                            #  get the log flush interval in mins and convert to milliseconds
                            self.logFlushInterval = int(c.text)
                            if (self.logFlushInterval < 1):
                                #  enforce a minumum 1 minute interval
                                self.logFlushInterval = 1 * 60 * 1000
                            else:
                                self.logFlushInterval = self.logFlushInterval * 60 * 1000
                        except:
                            errorText = 'Bad log_flush_interval in configuration file'
                            QtGui.QMessageBox.critical(self, 'Error', errorText)
                            self.close()
                            return
                    if (c.tag.lower() == 'start_scs_server'):
                        if (c.text.lower() == 'true'):
                            startSCSServer = True
                    if (c.tag.lower() == 'scs_server_port'):
                        try:
                            serverPort = int(c.text)
                        except:
                            errorText = 'Bad server port in configuration file'
                            QtGui.QMessageBox.critical(self, 'Error', errorText)
                            self.close()
                            return
                    if (c.tag.lower() == 'scs_server_ip'):
                        serverIP = c.text

        #  create an instance of the scsServer
        if (startSCSServer):
            self.scsServer = QSCSServer.QSCSServer(self.serialMonitor, ip=serverIP,
                    port=serverPort)
            self.serverIP = self.scsServer.ip.toString()
            self.serverPort = self.scsServer.port

        #  now parse the devices
        for section in root:
            if (section.tag.lower() == 'devices'):
                for device in section:
                    if (device.tag.lower() == 'device'):
                        deviceName = device.attrib['name']
                        sensorList = []
                        loggerList = []
                        comport = device.attrib['comport']
                        try:
                            baud = int(device.attrib['baud'])
                        except:
                            errorText = 'Bad baud for device: ' + deviceName
                            QtGui.QMessageBox.critical(self, 'Error', errorText)
                            self.close()
                            return

                        for config in device:
                            if (config.tag.lower() == 'sensor'):
                                sensorList.append(config.attrib)
                            if (config.tag.lower() == 'logger'):
                                loggerList.append(config.attrib)

                        #  add the device to the serial monitor
                        self.serialMonitor.addDevice(deviceName, comport, baud, 'none', '', '')

                        #  add the loggers
                        if (self.saveData):
                            for logger in loggerList:
                                doChecksum = False
                                if ('verify_checksum' in logger):
                                    if (logger['verify_checksum'].lower() == 'true'):
                                        doChecksum = True
                                self.addLogger(deviceName, logger['nmea_source'],
                                        verify_checksum=doChecksum)

                        #  if we're running the SCS server, start it
                        if (startSCSServer):
                            #  first we have to convert the parse_index from a comma string
                            #  to a list of indicies
                            for sensor in sensorList:
                                if (sensor['parse_type'].lower() != 'none'):
                                    #  split by comma
                                    pi = sensor['parse_index'].split(',')
                                    parseIndex = []
                                    try:
                                        #  loop thru the elements and try to convert to int
                                        for p in pi:
                                            parseIndex.append(int(p))
                                    except:
                                        #  couldn't parse the string
                                        errorText = ('Bad parse index defined for device: ' + deviceName +
                                                ' sensor: ' + sensor['name'])
                                        QtGui.QMessageBox.critical(self, 'Error', errorText)
                                        self.close()
                                        return
                                else:
                                    #  for parse type none we pass a dummy entry
                                    parseIndex = [0]

                                #  add the sensor to the server
                                self.scsServer.addNMEASensor(sensor['name'], deviceName,
                                        sensor['nmea_source'],sensor['parse_type'],
                                        sensor['parse_expression'], parseIndex)

        #  try to start the serial monitor
        try:
            self.serialMonitor.startMonitoring()
        except Exception, e:
            errorText = 'Unable to start the serial monitor:' + e.errText
            QtGui.QMessageBox.critical(self, 'Error', errorText)
            self.close()
            return

        #  start the SCS server
        if (startSCSServer):
            ok = self.scsServer.startServer()
            if (not ok):
                errorText = 'Unable to open SCS Server on ' + self.serverIP + ':' + str(self.serverPort)
                QtGui.QMessageBox.critical(self, 'Error', errorText)
                self.close()
                return
            else:
                self.SCSServerLabel.setText('SCS Server open at ' + self.serverIP + ':' + str(self.serverPort))

        #  start the log flush timer
        self.logFlushTimer.start(self.logFlushInterval)


    def receiveDeviceData(self, device, data, err):
        '''
        receiveDeviceData prints all data to the screen and logs data that has been
        configured to be logged. Some day the GUI can be designed
        '''

        #  check if we need to roll over our log files
        thisDay = datetime.datetime.now().timetuple().tm_yday
        if (thisDay != self.dayOfYear):
            #  yes, the day has changed
            self.dayOfYear = thisDay

            #  roll over all loggers for all devices
            for device in self.loggers:
                for logger in self.loggers[device]:
                    self.rolloverLogger(logger)

        #  make sure we got some data before we do anything
        if (data):

            rxTime = datetime.datetime.now()
            timeString = rxTime.strftime('D%Y%m%d-T%H%M%S') + '.%03d' % (rxTime.microsecond / 1000)

            #  check if we're logging anything from this device
            if (device in self.loggers.keys()):
                #  we are, loop through the loggers to find the one we need
                for logger in self.loggers[device]:
                    if (logger['source'] in data):
                        #  this is the logger we're looking for
                        try:
                            if (logger['verifyChecksum']):
                                ok = self.checkNMEAChecksum(data)
                            if (ok):
                                logger['filehandle'].write(timeString + ':::' + data + '\n')
                        except:
                            #  must have received gibberish - ignore
                            pass

            #  show the data on the screen
            self.showText(device, data)


    def checkNMEAChecksum(self, data):

        csum = 0
        ok = False

        try:
            cksum = int(data[len(data) - 2:], 16)
        except:
            return ok

        chksumdata = re.sub("(\n|\r\n)","", data[data.find("$")+1:data.find("*")])

        for c in chksumdata:
            csum ^= ord(c)

        if hex(csum) == hex(int(cksum, 16)):
            ok = True

        return ok


    def showText(self, name, val):
        '''
        showText formats the text for display in the GUI
        '''

        #  filter any non-printable characters
        val = ''.join(filter(lambda x:x in string.printable, val))

        #  update the display with this new line of text
        text = '<text style="color:black">' + name + ' : ' + val + '<br/>'
        self.displayText.append(text)
        if len(self.displayText) > self.maxDisplayLines:
            self.displayText.pop(0)
        text = ''.join(self.displayText)
        text = QtCore.QString('<html><body><p>' + text + '</p></body></html>')
        self.textBrowser.setHtml(text)

        #  ensure that the window is scrolled to see the new line of text.
        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())


    def addLogger(self, deviceName, nmeaSource, verify_checksum=False):

        #  make sure we have an antry for this device
        if (deviceName not in self.loggers.keys()):
            self.loggers[deviceName] = []

        #  strip the leading "$" if provided
        if (nmeaSource[0] == '$'):
            nmeaSource = nmeaSource[1:]

        #  make sure the main logging directory exists
        if (not os.path.isdir(self.saveDataPath)):
            #  directory doesn't exist, create it
            os.makedirs(self.saveDataPath)

        #  create the logging directory if needed and the datafile name
        loggingDir = self.saveDataPath + os.path.sep + deviceName
        if (not os.path.isdir(loggingDir)):
            #  directory doesn't exist, create it
            os.makedirs(loggingDir)

        #  create the base datafile name
        basename = loggingDir + os.path.sep + deviceName + '-' + nmeaSource + '-RAW_'

        #  and add it to our dict of loggers
        thisLogger = {'filehandle':None, 'source':nmeaSource, 'basename':basename,
                'verifyChecksum':verify_checksum}
        self.loggers[deviceName].append(thisLogger)

        #  roll over the log file (this will create the file handle)
        self.rolloverLogger(thisLogger)


    def rolloverLogger(self, logger):

        #  close the old file
        if (logger['filehandle']):
            logger['filehandle'].close()

        #  open the new one
        newfile = logger['basename'] + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.raw'
        logger['filehandle'] = open(newfile,'w')


    def flushLogBuffers(self):
        '''
        flushLogFiles flushes data to OS level buffers then forces a sync to
        ensure data is written to disk. This method is run periodically to
        ensure that we don't lose (much) data if the application or OS crashes.
        '''
        for devices in self.loggers:
            for logger in self.loggers[devices]:
                logger['filehandle'].flush()
                os.fsync(logger['filehandle'])


    def closeEvent(self, event):

        #  stop the log flush timer
        self.logFlushTimer.stop()

        #  stop the serial monitor
        self.serialMonitor.stopMonitoring()

        #  shut down our loggers
        for devices in self.loggers:
            for logger in self.loggers[devices]:
                logger['filehandle'].close()


        #  store the GUI state
        appSettings = QtCore.QSettings('afsc.noaa.gov', 'sensorLogger')
        appSettings.setValue('winposition', self.pos())
        appSettings.setValue('winsize', self.size())

        event.accept()


if __name__ == '__main__':

    #  create an QApplication instance
    app = QtGui.QApplication(sys.argv)

    #  create an instance of our  application and show
    form = sensorLogger()
    form.show()

    #  start the Qt event processor
    sys.exit(app.exec_())
