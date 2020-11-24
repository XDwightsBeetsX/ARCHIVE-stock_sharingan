"""
This module handles the procedural execution of requests over time,
implementing other modules.
Next steps for Routine.py:
    1. set up timed loop to run
    2. make api calls and get data
    3. link to email / sms for updates
    4. make this easily customizable
"""
import time as t
import datetime as dt
from iexfinance.stocks import get_historical_data, get_market_losers, get_market_gainers
from src.Time import get_prev_workweek
from src.Plots import plot_stock
from src.Stocks import StockInfo


class Routine:
    """
    API key, Stock obj, and time parameters are required to make a Routine

    Time properties use the time module and are in seconds
    For conversions, use datetime.fromtimestamp()
    """
    api_key = ""
    stocks = ()
    frequency_s = 0
    duration_s = 0
    start_time_t = 0
    running_time_t = 0
    routine_iter = 0
    file_save_destination = ""
    notify_email = ""
    notify_sms = ""

    def __init__(self, api_key, stocks, frequency_min, duration_hr, file_save_destination="", notify_email="",
                 notify_sms=""):
        self.api_key = api_key
        self.stocks = stocks
        self.frequency_s = frequency_min * 60  # min to sec
        self.duration_s = duration_hr * 60 * 60  # hr to min to sec
        self.file_save_destination = file_save_destination
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] New routine created: " +
              f"freq={frequency_min:.3f}s, dur={duration_hr:.3f}hr, stocks={stocks}")

    def setup(self, change_stocks=stocks, frequency_min=frequency_s/60, duration_hr=duration_s/60/60,
              file_save_destination=file_save_destination, notify_email=notify_email, notify_sms=notify_sms):
        """
        Used to modify the routine
        """
        self.stocks = change_stocks
        self.frequency_s = frequency_min * 60  # min to sec
        self.duration_s = duration_hr * 60 * 60  # hr to min to sec
        self.file_save_destination = file_save_destination
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] Current routine changed: " +
              f"freq={frequency_min:.3f}m, dur={duration_hr:.3f}hr, stocks={self.stocks}")

    def run(self):
        """
        Continuous process that does the following:
            tracks time and frequency of loop
            manages calls based on account usage
            gets stock data like winners and desired ticker info
            sends notification messages
        """
        self.running_time_t = 0
        self.routine_iter = 0
        self.start_time_t = t.time()
        print(f"[SS]-[ROUTINE] Beginning routine at {dt.datetime.fromtimestamp(self.start_time_t)}")

        print(f"rt:{self.running_time_t}t, dur{self.duration_s}s")

        # todo add acct call check here-API
        while self.running_time_t < self.duration_s:
            # Do stuff here
            last_week_df = self.get_last_workweek_data()
            print(last_week_df)
            plot_stock(last_week_df, self.file_save_destination)

            # winners = self.get_winners()
            # print(winners)

            # Delay and notify
            self.routine_iter += 1
            print(f"[SS]-[ROUTINE] Routine has run {self.routine_iter} times.")
            self.notify()
            self.running_time_t = t.time() - self.start_time_t
            t.sleep(self.frequency_s)

    def get_last_workweek_data(self):
        """
        Gets last workweek (m, f) and calls Plot.plot_stock() to plot/save data
        """
        last_monday, last_friday = get_prev_workweek()
        last_week_df = get_historical_data(self.stocks,
                                           last_monday,
                                           last_friday,
                                           token=self.api_key,
                                           close_only=True,
                                           output_format="pandas")
        return StockInfo(last_week_df, last_monday, last_friday)

    def get_winners(self):
        """
        Get winner values:
            ticker
            price
            $ & % change
            volume
        Save to excel
        """
        print("[SS]-[API] Getting winners...")
        winners_df = get_market_gainers(token=self.api_key,
                                        output_format="pandas")
        return StockInfo(winners_df)

    def get_losers(self):
        """
        Get lower values:
            ticker
            price
            $ & % change
            volume
        Save to excel
        """
        print("[SS]-[API] Getting losers...")
        losers_df = get_market_losers(token=self.api_key,
                                      output_format="pandas")
        return StockInfo(losers_df)

    def notify(self):
        """
        
        """
        pass
