import alpha_vantage as av
import numpy as np
import pandas as pd
import os
import re

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
