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
                print("[SS]-[API] Found api file:", os.path.join(root, file))
                try:
                    with open(os.path.join(root, file), "r") as api_file:
                        api_key = api_file.read().splitlines()[0]
                        if verify_api_key(api_key):
                            print("[SS]-[API] Found valid key:", api_key)
                            return api_key
                        else:
                            print("[SS]-[API] Key was found, but is not valid.")
                            return ""
                except e:
                    print("[SS]-[API] Encountered error while searching for key: " + e)
                    return ""
    raise RuntimeError


def verify_api_key(api_key):
    # make call w key and see if error thrown

    return True
