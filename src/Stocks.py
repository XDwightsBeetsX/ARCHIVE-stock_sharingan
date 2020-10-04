"""
This module defines a StockInfo obj that holds
    dataframe df
    start_dateTime dateTime
    end_dateTime dateTime

This module handles stock api calls used by Routine
Many/All of these return StockInfo objs
    get_last_workweek_data
    get_winners
    get_losers
"""
import pandas as pd
import datetime as dt


class StockInfo:
    df = pd.DataFrame()
    start_dateTime = dt.time()
    end_dateTime = dt.time()

    def __init__(self, stock_df, start_datetime=dt.time(), end_datetime=dt.time()):
        self.df = stock_df
        self.start_dateTime = start_datetime
        self.end_dateTime = end_datetime
