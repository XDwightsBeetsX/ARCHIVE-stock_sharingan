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
from iexfinance.stocks import Stock
from Time import get_prev_workday, get_prev_workweek
from Plots import plot_stock
from Stocks import get_last_workweek_data, get_losers, get_winners


class Routine:
    """
    API key and Stock obj are required to make a Routine

    Time properties use the time module and are in seconds
    For conversions, use datetime.fromtimestamp()
    """
    api_key = ""
    stocks = []
    frequency = 0
    start_time = 0
    running_time = 0
    duration = 0
    file_save_destination = ""
    notify_email = ""
    notify_sms = ""

    def __init__(self, api_key, stocks, frequency=60, duration=60, file_save_destination="", notify_email="",
                 notify_sms=""):
        self.api_key = api_key
        self.stocks = stocks
        self.frequency = frequency
        self.duration = duration
        self.file_save_destination = file_save_destination
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] New routine created: freq={self.frequency}, dur={self.duration}, stocks={self.stocks}")


    def setup(self, stocks=stocks, frequency=frequency, duration=duration, file_save_destination=file_save_destination,
              notify_email=notify_email, notify_sms=notify_sms):
        self.stocks = stocks
        self.frequency = frequency
        self.duration = duration
        self.file_save_destination = file_save_destination
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] Current routine changed: freq={self.frequency}, "
              f"dur={self.duration}, stocks={self.stocks}")


    def run(self, frequency=frequency, duration=duration):
        """
        Continuous process that does the following:
            tracks time and frequency of loop
            manages calls based on account usage
            gets stock data like winners and desired ticker info
            sends notification messages
        """
        self.frequency = frequency
        self.duration = duration
        self.start_time = t.time()
        self.running_time = 0
        print(f"[SS]-[ROUTINE] Beginning routine at {dt.datetime.fromtimestamp(self.start_time)}")

        # todo add acct call check here-API
        while self.running_time < self.duration:
            # Do stuff here
            last_week_df = get_last_workweek_data(self)
            plot_stock(last_week_df, self.file_save_destination)

            # Delay
            self.running_time = t.time() - self.start_time
            t.sleep(self.frequency)
