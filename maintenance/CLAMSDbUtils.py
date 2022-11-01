# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:58:40 2014

@author: rick.towler

CLAMSdbUtils is a collection of commonly used functions for CLAMS database
manipulation.

Note that these functions all assume the "db" object is an instance of the
dbConnection class.

"""

import dbConnection

def resetSequences(db, ship, survey):
    '''
    resetSequences resets the sequences on the samples, baskets, and specimen tables
    so they start at an appropriate value for the given ship and survey.

    CLAMS uses sequences to generate specimen, sample, and basket ID numbers but
    these numbers are by design only unique to a given ship/survey. When the
    ship and/or survey are changed, we need to alter the sequence parameters so we
    generate numbers that make sense for the new survey.

    And if you're wondering why we use sequences instead of just generating these
    values ourselves? Because it is simpler to use sequences when multiple users
    (CLAMS workstations) are inserting data at the exact same time.
    '''

    tablenames = ['samples','baskets', 'specimen']
    fieldnames = ['sample_id','basket_id', 'specimen_id']

    for i in range(len(tablenames)):
        table=tablenames[i]
        field=fieldnames[i]
        #  note the type of quotes for our string fields below. Also, the SQL is
        #  very specific, you need the "begin" and "end" and you need the ";"
        #  after your call to the reset function.
        sql = "begin Reset_Sequence_By_Survey('" + table + "','" + field + \
                    "'," + ship + "," + survey +"); end;"
        db.dbExec(sql)


def deleteEvent(db, ship, survey, event_id, schema='clamsbase2'):

    sql = ("DELETE FROM " + schema + ".measurements WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".specimen WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".baskets WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".sample_data WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".samples WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".gear_accessory WHERE ship=" + ship + " AND survey = " +
            survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".event_stream_data WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".event_data WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".events WHERE ship=" + ship + " AND survey = " +
           survey + " AND event_id=" + event_id)
    db.dbExec(sql)


def buildEventConstraint(startEvent, endEvent):
    '''
    buildEventConstraint is a simple function to build an "AND" constraint which
    selects continuous events between a start and end event id.
    '''

    eventConstraint = ''
    if (startEvent >= 0) or (endEvent):
        #  build the constraint
        eventConstraint = ' AND '
        if (startEvent > 1):
            eventConstraint = eventConstraint + 'event_id >= ' + str(startEvent) + ' '
            if (endEvent):
                 eventConstraint = eventConstraint + 'AND event_id <= '  + str(endEvent) + ' '
        elif (endEvent):
            eventConstraint = eventConstraint + 'event_id <= ' + str(endEvent) + ' '

    return eventConstraint


def deleteSurvey(db, ship, survey, startEvent=-1, endEvent=None, schema='clamsbase2'):
    '''
    deleteSurvey deletes an entire survey's worth of data given the Qt database
    connection object and the ship and survey as strings. It optionally can delete
    partial surveys if the event bounds are provided.

    It will only delete the entry in the survey table if *all* of the clamsbase
    events have been deleted AND there are no macebase2 data sets linked to the
    survey. It returns true if the survey entry has been deleted and false if it
    wasn't.
    '''

    surveyDeleted=True

    #  check if we have been given event bounds and need to build a constraint
    eventConstraint = buildEventConstraint(startEvent, endEvent)

    #  delete the data...
    sql = ("DELETE FROM " + schema + ".measurements WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".specimen WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".baskets WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".sample_data WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".samples WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".gear_accessory WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".event_stream_data WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".event_data WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)
    sql = ("DELETE FROM " + schema + ".events WHERE ship=" + ship + " AND survey = " +
            survey + eventConstraint)
    db.dbExec(sql)

    #  attempt to delete the survey entry - only succeeds if the entire clamsbase 2
    #  survey is deleted and if there is no macebase 2 data linked to it.
    sql = ("DELETE FROM " + schema + ".surveys WHERE survey=" + survey +
            " AND ship=" + ship)
    try:
        db.dbExec(sql)
    except dbConnection.SQLError as e:
        surveyDeleted=False

    return surveyDeleted


#def updateSurveyRecord(db, ship, survey,)
