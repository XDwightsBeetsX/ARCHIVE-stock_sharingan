"""
This module handles plotting of stocks and other data
"""
import pandas as pd
from iexfinance.stocks import Stock
from matplotlib import pyplot as plt
from Stocks import StockInfo


def plot_stock(stockInfo, save_destination="C:\\"):
    filename = f"StockData({stockInfo.start_dateTime.date()} - {stockInfo.end_dateTime.date()})"
    file_path = save_destination + "\\" + filename
    plot_path = file_path + ".png"
    df_path = file_path + ".xlsx"

    stockInfo.df.plot()
    writer = pd.ExcelWriter(df_path)  # pylint: disable=abstract-class-instantiated

    print("[SS]-[PLOTS] Saving data to", df_path)
    stockInfo.df.to_excel(writer, sheet_name="StockData")
    writer.save()
    writer.close()
    print("[SS]-[PLOTS] Saved data.")

    print("[SS]-[PLOTS] Saving plot to", plot_path)
    plt.savefig(plot_path)
    plt.show()
    print("[SS]-[PLOTS] Saved plot.")
