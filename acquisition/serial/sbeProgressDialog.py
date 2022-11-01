#!/usr/bin/env python

#  add the UI files to the python path
import sys
import os
pyPath = reduce(lambda l,r: l + os.path.sep + r, os.path.dirname(os.path.realpath(__file__)).split(os.path.sep))
sys.path.append(os.path.join(pyPath, 'ui'))

#  import dependent modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_sbeProgressDialog


class sbeProgressDialog(QDialog, ui_sbeProgressDialog.Ui_sbeProgressDialog):

    def __init__(self, sbeObject, parent=None):
        super(sbeProgressDialog, self).__init__(parent)
        self.setupUi(self)

        self.sbe = sbeObject
        self.connect(self.sbe, SIGNAL("SBEProgress"), self.__updateProgress)
        self.connect(self.sbe, SIGNAL("SBEAbort"), self.__abortComplete)
        self.setWindowTitle(self.sbe.deviceName + ' Download Progress')
        self.progressBar.setValue(0)
        self.connect(self.abortButton, SIGNAL("clicked()"), self.__abort)


    def __updateProgress(self, device, pct):
        self.progressBar.setValue(pct)

    def __abort(self):
        self.sbe.abort()

    def __abortComplete(self):
        self.reset()
        self.hide()

    def reset(self):
        self.progressBar.setValue(0)
