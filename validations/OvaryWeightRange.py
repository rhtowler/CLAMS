'''

    checkOrganismWeight

    checkOrganismWeight is a CLAMS validation class that checks if

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class OvaryWeightRange(QObject):

    def __init__(self, db, speciesCode,  subcategory='None'):
        '''
            The init methods of CLAMS validations are run whenever a new protocol
            or species is selected in the specimen module. Any setup that the
            validation requires should be done here. The two input arguments are:

                db - a reference to the CLAMS QtSQLDatabase object
                speciesCode - the

        '''

        #  call the superclass init
        QObject.__init__(self, None)

        #  Get the valid weight range for this species from the species table
        query = QtSql.QSqlQuery("SELECT parameter_value FROM application_configuration WHERE lower(parameter)='maxgsi'", db)

        #  extract returned results
        query.first()

        self.maxGSI=float(query.value(0).toString())

    def validate(self,  currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        gonadWt = float(currentValue)
        fishWt = float(values[measurements.index('organism_weight')])
        if fishWt==None:
            result = (False, "There's no organism weight")
            return result
        print gonadWt, ((self.maxGSI/100)*fishWt)
        if (gonadWt/fishWt) >  (self.maxGSI/100):# not a good value
            #  weight check failed - weight is outside valid range
            result = (False, "The GSI you've got here is "+str((gonadWt/fishWt) )+", which is more than the reference maximum. Do you want to re-enter weight? ")

        else:
            #  weight check succeeded - weight is o.k.
            result = (True, '')

        return result

