import datetime


class StockInfo:
    ticker = ""
    timeStamp = datetime.datetime.now()
    openPrice = 0
    closePrice = 0
    volume = 0

    def __init__(self, ticker, timestamp, open_price, close_price, volume):
        self.ticker = ticker
        self.timeStamp = timestamp
        self.openPrice = open_price
        self.closePrice = close_price
        self.volume = volume


    def export_to_excel(self, sheet, start_row, start_col):
        return

    def