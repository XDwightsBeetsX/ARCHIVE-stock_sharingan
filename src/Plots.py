"""
This module handles plotting of stocks and other data
"""
import pandas as pd
from matplotlib import pyplot as plt
from iexfinance.stocks import Stock


def plot_stock(stock_df, start_time, end_time, save_destination="C:\\"):
    filename = f"StockData{start_time} - {end_time}"
    file_path = save_destination + "\\" + filename
    plot_path = file_path + ".png"
    df_path = file_path + ".xlsx"

    print("[SS]-[PLOTS] Making data plot...")
    stock_df.plot()
    plt.show()
    writer = pd.ExcelWriter(df_path)

    print("[SS]-[PLOTS] Saving data to", df_path)
    stock_df.to_excel(writer, sheet_name="StockData")
    writer.save()
    writer.close()
    print("[SS]-[PLOTS] Saved data")

    print("[SS]-[PLOTS] Saving plot to", plot_path)
    plt.savefig(plot_path)
    print("[SS]-[PLOTS] Saved plot")


