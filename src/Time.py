"""
This module handles retrieving
    time spans
    dates
"""
import time as t
import datetime as dt

def get_last_workday(ref_date=dt.datetime.today()):
    timedelta = dt.timedelta(max(1, (ref_date.weekday() + 6) % 7 - 3))
    last_workday = ref_date - timedelta
    
    return last_workday


def get_last_workweek(ref_date=dt.datetime.today()):
    last_monday = ref_date + dt.timedelta(-ref_date.weekday(), weeks=-1)
    last_friday = ref_date + dt.timedelta(-ref_date.weekday() - 3)

    return last_monday, last_friday
