import pandas as pd
from matplotlib import pyplot as plt


class StockPlotter:
    stock_data = []
    file_name = ""
    directory = ""

    def __init__(self, stock_data, file_name="stockPlots", directory="C:\\"):
        self.stock_data = stock_data
        self.file_name = file_name
        self.directory = directory

    def plot_stocks(self):
        with open(self.file_name, 'w') as out:
            for stock_info in self.stock_data:
                stock_info.plot(out)

            plt.plot()
