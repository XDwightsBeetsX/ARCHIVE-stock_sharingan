"""
Stock Sharinagan
<Using Data from IEX Cloud>

Steps to activate your sharingan:
    0. Make an IEX Cloud account
    1. Get your API key
    2. Save the key to a iex_key.txt file
    3. Set up the api_path variable below
    4. Unleash the Sharingan (@) (@)
"""
from src.Routine import Routine
from src.Api import get_api_key


api_path = "C:\\dev"
api_filename = "iex_key.txt"

if __name__ == "__main__":
    print("[SS] Running stock-sharingan...")
    
    api_key = get_api_key(api_path, api_filename)

    stock_tickers = ["AAPL", "MSFT", "NVDA"]

    routine = Routine(api_key,
                    stock_tickers,
                    frequency_min=1,
                    duration_hr=1/60,
                    file_save_destination="C:\\dev")
    routine.run()

else:
    print("[SS]-[SYS]-[ERROR] Error running the project")
