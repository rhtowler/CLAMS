'''

    VialNumberDuplicate

    VialNumberDuplicate is a CLAMS validation class that checks if vial_number is a duplicate vial_number within a Survey

    Validations are classes that are used by the CLAMS specimen module
    to check


'''
from PyQt4.QtCore import *
from PyQt4 import QtSql

class VialNumberDuplicate(QObject):

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


    def validate(self,  currentValue,  measurements,  values):
        '''
            The validate method is called when
        '''

        vial_num = currentValue
        query=QtSql.QSqlQuery("SELECT parameter_value FROM application_configuration WHERE parameter = 'ActiveSurvey'")
        query.first()
        survey=query.value(0).toString()
        query=QtSql.QSqlQuery("SELECT device_id FROM measurements WHERE measurement_type ='vial_number' AND measurement_value ='"+vial_num+"' AND survey ="+survey)
        if query.first():
            #  weight check failed - weight is outside valid range
            result = (False, 'This vial number already exists in the database for this survey.  Do you want to re-enter?')

        else:
            #  weight check succeeded - weight is o.k.
            result = (True, '')

        return result

