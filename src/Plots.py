"""
This module handles plotting of stocks and other data
"""
import pandas as pd
from matplotlib import pyplot as plt


def plot_stock(stock_info, save_destination="C:\\"):
    filename = f"StockData({stock_info.start_datetime.date()} - {stock_info.end_datetime.date()})"
    file_path = save_destination + "\\" + filename
    plot_path = file_path + ".png"
    df_path = file_path + ".xlsx"

    stock_info.df.plot()
    writer = pd.ExcelWriter(df_path)  # pylint: disable=abstract-class-instantiated

    print("[SS]-[PLOTS] Saving data to", df_path)
    stock_info.df.to_excel(writer, sheet_name="StockData")
    writer.save()
    writer.close()
    print("[SS]-[PLOTS] Saved data.")

    print("[SS]-[PLOTS] Saving plot to", plot_path)
    plt.savefig(plot_path)
    plt.show()
    print("[SS]-[PLOTS] Saved plot.")
