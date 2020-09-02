"""
Stock Sharinagan
<Using Data from IEX Cloud>

Steps to activate your sharingan:
    1. Get an API key
    2. Save the key to a iex_key.txt file
    3. Set up the api_path variable
    4. Use the Sharingan (@) (@)
"""
import src.Api as Api

api_path = "C:\\dev\\"
api_filename = "iex_key.txt"

if __name__ == "__main__":
    print("[SS] Running stock-sharingan...")
    try:
        print("[SS]-[API] Looking for API key in " + api_path + api_filename)
        api_key = Api.get_api(api_path, api_filename)
    except RuntimeError:
        print("[SS]-[API] Could not locate/validate your key.")
        print("[SS]-[API] Make sure the only contents of the file is your key.")
        print("[SS]-[API] Path checked: " + api_path + api_filename)

    # some things to consider:
    #   how to implement requests
    #       terminal commands
    #       setup.txt parsing
    #       (get email)

else:
    print("error finding the project")
