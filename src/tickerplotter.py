import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import re
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

api_key_source_path = "H:\\"
api_key_filename = "alphavantagekey.txt"


def get_api_key(api_key_path):
    api_key = ""
    for root, dirs, files in os.walk(api_key_path):
        if api_key_filename in files:
            with open(os.path.join(root, api_key_filename), "r") as file:
                try:
                    api_key = str(re.split("\n", file.read())[0])
                except TypeError:
                    print("ERROR {file does not contain a key}")
                    quit()
    if api_key == "":
        print("ERROR {file not found}")
        quit()
    else:
        return api_key


if __name__ == "__main__":
    key = get_api_key(api_key_source_path)
    print(f"found api key: {key}")

    ts = TimeSeries(key=key, output_format='pandas')
    data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')

    period = 60

    ti = TechIndicators(key=key, output_format='pandas')
    data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min', time_period=period, series_type='close')

    df1 = data_ti
    df2 = data_ts['4. close'].iloc[period - 1::]

    df2.index = df1.index

    total_df = pd.concat([df1, df2], axis=1)
    print(total_df)

    total_df.plot()
    plt.show()
