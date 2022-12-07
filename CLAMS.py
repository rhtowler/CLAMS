'''
    CLAMS.pyw launches the main CLAMS application and pipes the console
    output to a log file. The log files are written to the directory
    specified in the CLAMS.ini file.

    During development we typically run CLAMS from within our IDE and
    do not run it using this script. But in production, running from
    this script logs exceptions that aren't handled and provides valuable
    infomation when tracking down bugs.
'''

import os
import sys
import subprocess
import functools
import datetime
from PyQt4.QtCore import *



def checkpath(path):
    
    if errorLogPath[0:1] in ['./', '.\\']:
        scriptPath = functools.reduce(lambda l,r: l + os.path.sep + r,
                os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
                
        path = scriptPath + os.sep + path[2:]
    
    path = os.path.normpath(path)
    
    return path


#  see if the ini file path was passed in
if (len(sys.argv) > 1):
    iniFile = sys.argv[1]
    iniFile = os.path.normpath(iniFile)
else:
    #  no argument provided, use default
    iniFile = 'clams.ini'

#  create an instance of QSettings to load fundamental CLAMS settings
initSettings = QSettings(iniFile, QSettings.IniFormat)

#  extract log path
errorLogPath = str(initSettings.value('ErrorLogDir', './application_logs').toString())

if errorLogPath[0:1] in ['./', '.\\']:
    scriptPath = functools.reduce(lambda l,r: l + os.path.sep + r,
            os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
    path = scriptPath + os.sep + path[2:]

#  normalize the path and finish with trailing slash
errorLogPath = os.path.normpath(errorLogPath) + os.sep

try:
    #  check for the error log directory, create if needed
    if not (os.path.exists(errorLogPath)):
        #  directory doesn't exist - create it
        os.mkdir(errorLogPath)

    #  generate a file name for the log file
    logFileName = datetime.datetime.utcnow().strftime('D%m%d%YT%H%M%S')
    logFileName = errorLogPath + 'CLAMS_Errors-' + logFileName + '.txt'
    output_f = open(logFileName, 'w')

except:
    #  do not log errors becuase we can't create a log file
    output_f = None


#  start CLAMS and pipe the console output to our errors file
p = subprocess.call(['pythonw.exe', 'CLAMSMain.pyw', iniFile], stdout=output_f, stderr=output_f)


