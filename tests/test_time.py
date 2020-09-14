import pytest
import datetime as dt
import src.Time as Time

def test_get_prev_workday_1():
    """Sunday -> Friday"""
    testDay = dt.datetime(2020, 9, 6)  # Sunday
    prev_workday_test = Time.get_prev_workday(testDay)
    prev_workday = dt.datetime(2020, 9, 4)  # Friday
    test = prev_workday == prev_workday_test
    assert test

def test_get_prev_workday_2():
    """Monday -> Friday"""
    testDay = dt.datetime(2020, 9, 7)  # Monday
    prev_workday_test = Time.get_prev_workday(testDay)
    prev_workday = dt.datetime(2020, 9, 4)  # Friday (same)
    test = prev_workday == prev_workday_test
    assert test

def test_get_prev_workday_3():
    """Wednesday -> Tuesday"""
    testDay = dt.datetime(2020, 9, 9)  # Wednesday
    prev_workday_test = Time.get_prev_workday(testDay)
    prev_workday = dt.datetime(2020, 9, 8)  # Tuesday
    test = prev_workday == prev_workday_test
    assert test

def test_get_prev_workday_4():
    """Friday 5p+ -> Friday"""
    testDay = dt.datetime(2020, 9, 4, 17, 1)  # Friday 1min after 5
    prev_workday_test = Time.get_prev_workday(testDay)
    prev_workday = dt.datetime(2020, 9, 4)  # Friday (same)
    test = prev_workday == prev_workday_test
    assert test

def test_get_prev_workwk_1():
    """Sunday -> M/F"""
    testDay = dt.datetime(2020, 9, 6, 0, 0)  # Sunday
    prev_wk_m, prev_wk_f = Time.get_prev_workweek(testDay)
    prev_wk_m_test = dt.datetime(2020, 8, 31)  # Monday
    prev_wk_f_test = dt.datetime(2020, 9, 4)  # Friday
    test = (prev_wk_m == prev_wk_m_test) and (prev_wk_f == prev_wk_f_test)
    assert test

def test_get_prev_workwk_2():
    """Friday -> M/F(prev)"""
    testDay = dt.datetime(2020, 9, 4, 0, 0)  # Friday
    prev_wk_m, prev_wk_f = Time.get_prev_workweek(testDay)
    prev_wk_m_test = dt.datetime(2020, 8, 24)  # Monday
    prev_wk_f_test = dt.datetime(2020, 8, 28)  # Friday (prev)
    test = (prev_wk_m == prev_wk_m_test) and (prev_wk_f == prev_wk_f_test)
    assert test

def test_get_prev_workwk_3():
    """Friday 5p+ -> M/F(same)"""
    testDay = dt.datetime(2020, 9, 4, 17, 1)  # Friday 1min after 5
    prev_wk_m, prev_wk_f = Time.get_prev_workweek(testDay)
    prev_wk_m_test = dt.datetime(2020, 8, 31)  # Monday
    prev_wk_f_test = dt.datetime(2020, 9, 4)  # Friday (same)
    test = (prev_wk_m == prev_wk_m_test) and (prev_wk_f == prev_wk_f_test)
    assert test
