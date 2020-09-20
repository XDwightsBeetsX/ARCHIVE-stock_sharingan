"""
This module handles retrieving
    prev workday
    prev workweek
"""
import time as t
import datetime as dt


def get_prev_workday(ref_date=dt.datetime.today()):
    """
    Returns the last workday.
    If after 5p friday, returns the current day.
    """
    prev_workday = ref_date - dt.timedelta(max(1, (ref_date.day + 6) % 7 - 3))
    prev_workday = prev_workday.replace(hour=0, minute=0, second=0, microsecond=0)
    
    if ref_date.day == 4 and ref_date > dt.datetime.combine(ref_date, dt.time(hour=17)):
        prev_workday += dt.timedelta(days=1)
    
    return prev_workday


def get_prev_workweek(ref_date=dt.datetime.today()):
    """
    Returns the last monday and friday.
    If after 5p friday, returns the current week.
    """
    week = dt.timedelta(days=0, weeks=1)
    # clear time data, and go back a week
    prev_monday = ref_date - dt.timedelta(days=ref_date.weekday(),
        hours=ref_date.hour,
        minutes=ref_date.minute,
        seconds=ref_date.second,
        microseconds=ref_date.microsecond) - week
    prev_friday = prev_monday + dt.timedelta(days=4)

    # if a weekend, update to wk that just ended
    if ref_date.day > 4:
        prev_monday += week
        prev_friday += week

    # if after 5 on a friday, prev_monday is this monday
    elif ref_date.day == 4 and ref_date - dt.datetime.combine(prev_friday, dt.time(17)) > week:
        prev_monday += week
        prev_friday += week
    
    return prev_monday, prev_friday
