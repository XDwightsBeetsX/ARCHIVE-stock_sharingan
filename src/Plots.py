"""
This module handles plotting of stocks and other data
"""
import pandas as pd
from matplotlib import pyplot as plt
from iexfinance.stocks import Stock


def plot_stock(stock_df, start_time, end_time, save_destination="C:\\"):
    filename = f"StockData{start_time} - {end_time}"
    file_path = save_destination + "\\" + filename

    stock_df.plot()
    plt.show()
    writer = pd.ExcelWriter(file_path + ".xlsx")
    stock_df.to_excel(writer, sheet_name="StockData")

    writer.save()
    writer.close()
    plt.savefig(file_path + ".png")

