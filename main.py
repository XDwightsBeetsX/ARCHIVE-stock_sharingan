"""
Stock Sharinagan
<Using Data from IEX Cloud>

Steps to activate your sharingan:
    0. Make an IEX Cloud account
    1. Get your API key
    2. Save the key to a iex_key.txt file
    3. Set up the api_path variable
    4. Unleash the Sharingan (@) (@)
"""
from src import Api, Routine

api_path = "C:\\dev"
api_filename = "iex_key.txt"

if __name__ == "__main__":
    print("[SS] Running stock-sharingan...")
    """RETRIEVE API KEY"""
    # api_key = Api.get_api(api_path, api_filename)

    """RUN ROUTINE"""
    routine = Routine.Routine("AAPL")
    routine.run(1, 10)


else:
    print("[SS]-[SYS]-[ERROR] Error running the project")
