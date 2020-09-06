"""
This module handles any api aspects such as:
    obtaining the key
    verifying the key
"""
import os
import pandas as pd
from iexfinance.refdata import get_symbols


def get_api(api_path, api_filename):
    """
    Searches through directories and files of api_path for api_filename and returns the api_key
    api_key is run through verify_api_key to ensure validity
    if fails, throws error caught in main
    """
    for root, dirs, files in os.walk(api_path):
        for file in files:
            if file.endswith(api_filename):
                print("[SS]-[API] Found api file:", os.path.join(root, file))
                try:
                    with open(os.path.join(root, file), "r") as api_file:
                        api_key = api_file.read().splitlines()[0]
                        if verify_api_key(api_key, root):
                            print("[SS]-[API] Key verified:", api_key)
                            return api_key
                        else:
                            print("[SS]-[API]-[ERROR] Key was found, but is not valid.")
                            return ""
                except Exception:
                    print("[SS]-[API]-[ERROR] Encountered error while reading key.")
                    return ""
    raise Exception


def verify_api_key(api_key, api_key_path):
    """
    Used by get_api to ensure the key is valid
    Does this by attempting a call to get stock_references
    """
    try:
        stock_references = get_symbols(output_format='pandas', token=api_key)
    except Exception:
        return False
    writer = pd.ExcelWriter(api_key_path + "\\stock_references_iexcloud.xlsx")
    stock_references.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    writer.close()
    print("[SS]-[API] Wrote stock references to api filepath.")
    return True
