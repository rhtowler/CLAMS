'''

    checkBodyOrHeadSalmon

    checkBodyOrHeadSalmon is a CLAMS validation class that checks if a body or head should be frozen

    Validations are classes that are used by the CLAMS specimen module
    to check


'''

from PyQt4.QtCore import *
from PyQt4 import QtSql
from math import ceil

class BodyOrHeadSalmon(QObject):

    def __init__(self, db):
        '''
            The init methods of CLAMS conditionals are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The two input arguments are:

                db - a reference to the CLAMS QtSQLDatabase object
                speciesCode - the

        '''
        #  call the superclass init
        QObject.__init__(self, None)
        self.cnt = 0;           # initialize the counter


    def evaluate(self,   measurements,  values,  result):
        '''
            The evaluate method is called when measuremets are taken to see what changes in the protocol
        '''
        
        if values[0] != None:                                 # first reading must be mandatory and completed
            if values.count(None) == len(values)-1:   # all other readings must be None
                self.cnt = self.cnt+1                          # increment the counter
        
		
        if self.cnt < 21:
            try:
                result[measurements.index('fish_head')] = False
            except:
                pass
        elif self.cnt > 20 & self.cnt < 51:
            try:
                result[measurements.index('whole_fish')] = False
            except:
                pass
        elif self.cnt > 51:
            try:
                result[measurements.index('whole_fish')] = False
                result[measurements.index('fish_head')] = False
            except:
                pass
                
        return result




