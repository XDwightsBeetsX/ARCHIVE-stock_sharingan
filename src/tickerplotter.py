import alpha_vantage as av
import numpy as np
import pandas as pd


class StockInfo:
    ticker = ""
    price = 0.00

    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price


if __name__ == "__main__":
    apple = StockInfo("aapl", 120.71)
    print(apple.ticker, apple.price)
