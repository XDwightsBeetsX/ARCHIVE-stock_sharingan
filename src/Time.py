"""
This module handles retrieving
    time spans
    dates
"""
import time as t
import datetime as dt

def get_last_workweek():
    today = dt.datetime.today()
    last_monday = today + dt.timedelta(-today.weekday(), weeks=-1)
    last_friday = today + dt.timedelta(-today.weekday() - 3)
    
    return last_monday, last_friday
