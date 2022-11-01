'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''

from PyQt4.QtCore import *
from PyQt4 import QtSql

class TakingOvaryFemaleRockfish(QObject):

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


    def evaluate(self, measurements, values, result):
        '''
            The evaluate method is called when measuremets are taken to see what changes in the protocol
        '''

        #  first make sure we have a sex measurement...
        if values[measurements.index('sex')]:
            
            if str(values[measurements.index('sex')]).lower()=='male':
                #  for males we don't take ovaries, their weights, or livers
                if 'ovary_taken' in measurements:
                    result[measurements.index('ovary_taken')]=False
            
            
            #  DISABLE THIS CODE FOR WINTER 2013 - We want the option to weigh ovaries even
            #  though we aren't taking a specimen for preservation.
#            elif values[measurements.index('ovary_taken')]=='0':
#                #  if we don't take an ovary from a female, we don't get the weight or take a liver
#                if 'liver_weight' in measurements:
#                    result[measurements.index('liver_weight')]=False
#                if 'ovary_weight' in measurements:
#                    result[measurements.index('ovary_weight')]=False

        return result

