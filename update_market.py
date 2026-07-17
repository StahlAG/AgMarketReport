import json
from datetime import datetime

from ritzville_grain import get_ritzville_cash_bids

print("Getting Ritzville cash bids...")

bids = get_ritzville_cash_bids()

data = {
    "ritzville": {
        "cashBids": bids
    },

    "futures": {},
    "financialMarkets": {},
    "exchangeRates": {},
    "potatoes": {},
    "cropMarkets": {},
    "livestock": {},
    "weather": {},

    "marketMood": "",
    "coffeeReport": "",
    "updated": datetime.now().strftime("%Y-%m-%d %H:%M")
}

with open("market-data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Done.")
print(data)
