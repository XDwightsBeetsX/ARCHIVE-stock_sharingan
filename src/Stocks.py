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
from iexfinance.stocks import get_historical_data, get_market_losers, get_market_gainers
from Time import get_prev_workday, get_prev_workweek
from Plots import plot_stock


class StockInfo:
    df = pd.DataFrame()
    start_dateTime = dt.time()
    end_dateTime = dt.time()

    def __init__(self, stock_df, start_dateTime=dt.time(), end_dateTime=dt.time()):
        self.df = stock_df
        self.start_dateTime = start_dateTime
        self.end_dateTime = end_dateTime


def get_last_workweek_data(routine):
        """
        Gets last workweek (m, f) and calls Plot.plot_stock() to plot/save data
        """
        last_monday, last_friday = get_prev_workweek()
        last_week_df = get_historical_data(routine.stocks,
                                           last_monday,
                                           last_friday,
                                           token=routine.api_key,
                                           close_only=True,
                                           output_format="pandas")
        return StockInfo(last_week_df, last_monday, last_friday)


def get_winners(routine):
    """
    Get winner values:
        ticker
        price
        $ & % change
        volume
    Save to excel
    Email notify
    """
    print("[SS]-[API] Getting winners...")
    winners_df = get_market_gainers(token=routine.api_key,
                                    output_format="pandas")
    return StockInfo(winners_df)


def get_losers(routine):
    """
    Get lower values:
        ticker
        price
        $ & % change
        volume
    Save to excel
    Email notify
    """
    print("[SS]-[API] Getting losers...")
    losers_df = get_market_losers(token=routine.api_key,
                                    output_format="pandas")
    return StockInfo(losers_df)
