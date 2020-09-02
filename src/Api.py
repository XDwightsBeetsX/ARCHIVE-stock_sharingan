"""
This module handles any api aspects such as:
    obtaining the key
    verifying the key

    all calls???
"""
import os


def get_api(api_path, api_filename):
    for root, dirs, files in os.walk(api_path):
        for file in files:
            if file.endswith(api_filename):
                print("[SS] Found api file:", os.path.join(root, file))
                try:
                    with open(os.path.join(root, file), "r") as api_file:
                        api_key = api_file.read().splitlines()[0]
                        if verify_api_key(api_key):
                            print("[SS] Found api key:", api_key)
                            return api_key
                        else:
                            return ""
                except (RuntimeError, TypeError):
                    return ""


def verify_api_key(api_key):
    # make call w key and see if error thrown
    return True
