"""
This module handles any api aspects such as:
    obtaining the key
    verifying the key
"""
import os
import pandas as pd
import datetime as dt
from iexfinance.refdata import get_symbols
from iexfinance.stocks import get_historical_data, get_market_gainers, get_market_losers
from iexfinance.account import get_usage, disallow_pay_as_you_go


def get_api_key(api_path, api_filename, get_references=False):
    """
    Searches through directories and files of api_path for api_filename and returns the api_key
    api_key is run through verify_api_key to ensure validity
    if fails, throws error caught in main
    """
    print("[SS]-[API] Looking for API key in " + api_path + "\\" + api_filename)
    try:
        for root, _dirs, files in os.walk(api_path):
            for file in files:
                if file.endswith(api_filename):
                    print("[SS]-[API] Found api file:", os.path.join(root, file))
                    try:
                        with open(os.path.join(root, file), "r") as api_file:
                            api_key = api_file.read().splitlines()[0]
                            print(f"[SS]-[API] Attempting to verify key: [{api_key}]")
                            if verify_api_key(api_key, root, get_references):
                                print("[SS]-[API] Key verified.")
                                # disallow_pay_as_you_go(token=api_key)
                                return api_key
                            else:
                                print("[SS]-[API]-[ERROR] Key was found, but is not valid.")
                    except Exception:
                        print("[SS]-[API]-[ERROR] Encountered error while reading/verifying key.")
        raise Exception

    except Exception:
        print("[SS]-[API]-[ERROR] Make sure the only contents of the file is your key.")
        print("[SS]-[API]-[ERROR] Exiting... ")
        exit()


def verify_api_key(api_key, api_key_path, get_references=False):
    """
    Used by get_api to ensure the key is valid
    Does this by attempting a call to get stock_references or AAPL price
    """
    try:
        if get_references:
            stock_references = get_symbols(output_format="pandas", token=api_key)
            writer = pd.ExcelWriter(api_key_path + "\\stock_references_iexcloud.xlsx") # pylint: disable=abstract-class-instantiated
            stock_references.to_excel(writer, sheet_name="Stock References")
            writer.save()
            writer.close()
            print("[SS]-[API] Wrote stock references to api filepath.")
        else:
            verify_datetime = dt.datetime(2020, 9, 1)
            get_historical_data("AAPL", verify_datetime, close_only=True, token=api_key)
    except Exception as e:
        print(e)
        return False
    return True


def print_acct_usage(api_key):
    """
    TODO get this working. currently error w key or something
    """
    print("[SS]-[API] Getting usage information...")
    usage = get_usage(quota_type="messages", token=api_key)
    print(usage)
