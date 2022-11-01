

import telnetlib
from xml.etree import ElementTree as ET
from PyQt4.QtCore import *

class QSCSTelnetThread(QThread):

    def __init__(self, host, port, timeout=15, parent=None):

        QThread.__init__(self, parent)

        #  set default values
        self.__txBuffer = []
        self.__running = False
        self.__msleepInt = 100
        self.host = host
        self.port = port
        self.timeout = timeout

        #  define the XML parsing tags - This is a dictionary that is keyed
        #  by request type. The values associated with the keys are a list
        #  that contains the XML tag names we key on when parsing the XML.
        self.__parseTags = {}
        self.__parseTags['SensorDescription'] = ['sensor','sensorname']
        self.__parseTags['Get'] = ['sensordata','sensor_name']

        #  create an instance of the telnet client
        self.__scs = telnetlib.Telnet()

        #  connect this thread to the monitor's signals
        self.connect(parent, SIGNAL("_txSCSData"), self.__write)


    def startMonitor(self):
        """Open the telnet connection to the SCS server
        """

        if not self.isRunning():
            try:
                #  open the connection to the SCS server
                self.__scs.open(self.host, self.port, self.timeout)

                #  read the initial server response
                response = self.__scs.read_until('\n', self.timeout)

                #  confirm we're connected to an SCS server
                if (response.find('SCS') > -1):
                    # start the thread
                    self.__running = True
                    self.start()
                else:
                    raise QSCSError('No response from server at' + self.host + ':' + self.port, parent=err)
            except Exception as err:
                raise QSCSError('Unable to connect to SCS server at' + self.host + ':' + self.port, parent=err)


    def stopMonitor(self):
        """Stop the currently running thread which will also close the SCS connection
        """
        if self.isRunning():
            #  set the "running" state to false
            self.__running = False
            #  wait here until the thread exits the run method
            self.wait()
            #  close the connection to the server
            self.__scs.close()


    def __write(self, type, data):
        """Send commands to the SCS server. This method simply appends the data
          to the tx buffer.  Data is written in the "run" method.
        """
        reqData = {'type':type, 'text':data}
        self.__txBuffer.append(reqData)


    def run(self):
        """This method monitors the tx queue, transmits a requests when data is
          added to the queue, receives the response from the SCS server, then
          parses the response and returns it to the SCSClient object.

          This method is called automagically by QThread after we call QThread's
          start method. This method is never called directly.
        """

        while self.__running:
            try:
                #  check if we have any commands to Tx
                nCommandsTx = len(self.__txBuffer)

                if (nCommandsTx > 0):
                    #  there are commands to send - get a copy of them
                    commandList = self.__txBuffer
                    self.__txBuffer = []

                    for command in commandList:
                        #  send the command to the SCS server
                        self.__scs.write(command['text'])

                        #  Rx the response
                        response = self.__scs.read_until('\n', self.timeout)

                        #  strip the "junk" - The SensorList datagram has a bit of
                        #  crud that is pre/appended onto the XML string. We'll just remove it.
                        response = response[response.find('<'):response.rfind('>')+1]

                        try:
                            #  parse the XML string
                            eTree = ET.XML(response)

                            #  parse the element tree and return as a dictionary
                            data = {}
                            for subElement in eTree:
                                if (subElement.tag.lower() == self.__parseTags[command['type']][0]):
                                    dictKey = ''
                                    tempDict = {}
                                    for propNode in subElement:
                                        if (propNode.tag.lower() == self.__parseTags[command['type']][1]):
                                            dictKey = propNode.text
                                        else:
                                            tempDict[propNode.tag] = propNode.text
                                    data[dictKey] = tempDict

                            #  send the parsed dictionary to the QSCSClient
                            self.emit(SIGNAL("_SCSDataReceived"), command['type'], data)

                        except Exception as err:
                            #  emit an error signal if we run into problems parsing the data. This
                            #  may happen if we receive a malformed/partial response from the server.
                            scsError = QSCSError('Error parsing XML response from SCS Server.', 2, parent=err)
                            self.emit(SIGNAL("_SCSDataReceived"), 'error', scsError)

                else:
                    #  nothing to do - so we'll sleep
                    self.msleep(self.__msleepInt)


            except Exception as err:
                #  emit an error signal if we lose our connection to the server
                scsError =  QSCSError('Connection to SCS server lost.', 1, parent=err)
                self.emit(SIGNAL("_SCSDataReceived"), 'error', scsError)

                #  stop running
                self.__running = False

                #  close the connection to the server
                self.__scs.close()

                #  clear the queue
                self.__txBuffer = []

#
#  QSSCSClient Exception class
#
class QSCSError(Exception):
    def __init__(self, errText, errCode, parent=None):
        self.errText = errText
        self.errCode = errCode
        self.parent = parent

    def __str__(self):
        return repr(self.errText)
