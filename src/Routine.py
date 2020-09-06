"""
This module handles the procedural execution of requests over time,
implementing other modules.
Next steps for Routine.py:
    1. set up timed loop to run
    2. make api calls and get data
    3. link to email / sms for updates
    4. make this easily customizable
"""
from src import Stocks, Plots, Sector, Social
import time as t
from datetime import datetime as dt


class Routine:
    # list of stock tickers/objects? to make calls for
    stocks = []
    # frequency is in min
    frequency = 0
    # for future use
    notify_email = ""
    notify_sms = ""
    # time management
    start_time = 0
    running_time = 0
    # duration is in seconds
    duration = 0

    def __init__(self, stocks=[], frequency=60, duration=60, notify_email="", notify_sms=""):
        self.stocks = stocks
        self.frequency = frequency
        self.duration = duration
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] New routine created: freq={self.frequency}, dur={self.duration}m, stocks={self.stocks}")

    def setup(self, stocks=stocks, frequency=frequency, duration=duration,
              notify_email=notify_email, notify_sms=notify_sms):
        self.stocks = stocks
        self.frequency = frequency
        self.duration = duration
        self.notify_email = notify_email
        self.notify_sms = notify_sms
        print(f"[SS]-[ROUTINE] Current routine changed: freq={self.frequency}, dur={self.duration}m, stocks={self.stocks}")

    def run(self, frequency=frequency, duration=duration):
        self.frequency = frequency
        self.duration = duration
        self.start_time = t.time()
        self.running_time = 0
        print(f"[SS]-[ROUTINE] Beginning routine at {dt.fromtimestamp(self.start_time)}")

        while self.running_time < self.duration:
            t.sleep(self.frequency)
            self.call()
            self.running_time = t.time() - self.start_time

    def call(self):
        print("whaddup", self.running_time)
