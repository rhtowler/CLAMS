from PyQt6.QtSql import QSqlQuery
import pandas as pd


def get_legs():
    """

    :return:
    """
    # get the survey data
    query = QSqlQuery("SELECT * FROM SURVEY_DATA WHERE SURVEY_PARAMETER='Leg'")
    leg_df = pd.DataFrame(columns=['leg', 'start', 'end'])
    while query.next():
        parent = query.value(4).toString()
        leg = query.value(3).toString()
        # get children
        child_q = QSqlQuery("SELECT * FROM SURVEY_DATA WHERE SURVEY_PARAMETER IN "
                            "('Leg start date planned', 'Leg end date planned') AND PARENT_PARAMETER = " + parent)
        leg_vals = {'leg': str(leg), 'start': None, 'end': None}
        while child_q.next():
            if 'start' in child_q.value(2).toString():
                leg_vals['start'] = str(child_q.value(3).toString())
            elif 'end' in child_q.value(2).toString():
                leg_vals['end'] = str(child_q.value(3).toString())
        leg_df = leg_df.append(leg_vals, ignore_index=True)

    return leg_df


def get_len_wt(specimen_key):
    """

    :param specimen_key:
    :return:
    """
    # get length of specimen_id
    len_q = QSqlQuery("SELECT measurement_value FROM Measurements WHERE specimen_id = " + specimen_key +
                      " AND measurement_type LIKE '%length'")
    len_q.first()
    length = str(len_q.value(0).toString())
    # get weight of specimen_id
    wt_q = QSqlQuery("SELECT measurement_value FROM Measurements WHERE specimen_id = " + specimen_key +
                     " AND measurement_type LIKE '%weight'")
    wt_q.first()
    weight = str(wt_q.value(0).toString())

    return length, weight
