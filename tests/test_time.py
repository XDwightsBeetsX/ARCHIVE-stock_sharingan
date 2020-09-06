import pytest
import datetime as dt
import src.Time as Time

def test_get_last_workday():
    testDay1 = dt.date(2020, 9, 6)  # Sunday
    last_workday_test = Time.get_last_workday(testDay1)
    last_workday1 = dt.date(2020, 9, 4)
    test1 = last_workday1 == last_workday_test
    assert test1
