import alpha_vantage as av
import numpy as np
import pandas as pd
import os
import re

av_key_source_path = "H:/dev/"


def get_av_key(av_key_path):
    av_key_filename = "alphavantagekey.txt"
    av_key = ""

    for root, dirs, files in os.walk(av_key_path):
        if av_key_filename in files:
            with open(av_key_path + av_key_filename, "r") as file:
                try:
                    av_key = str(re.split("\n", file.read())[0])
                except TypeError:
                    print("ERROR {file does not contain a key}")
                    quit()
    if av_key == "":
        print("ERROR {file not found}")
        quit()
    else:
        return av_key


if __name__ == "__main__":
    print("found key:", get_av_key(av_key_source_path))
