import requests
import json
from datetime import datetime

today = datetime.now()

# ---------------------------------------
# SETTINGS
# ---------------------------------------

API_URL = "PUT_DATA_FEED_URL_HERE"

HEADERS = {
    "User-Agent": "AgMarketReport"
}

# ---------------------------------------
# DOWNLOAD DATA
# ---------------------------------------

response = requests.get(API_URL, headers=HEADERS)
response.raise_for_status()

feed = response.json()

# ---------------------------------------
# BUILD RITZVILLE GRAIN TABLE
# ---------------------------------------

wheat = []

for bid in feed:

    grade = bid.get("grade", "").upper()

    if grade in [
        "HRW",
        "HRS",
        "DNS",
        "SOFT WHITE",
        "FEED WHEAT"
    ]:

        wheat.append({
            "market": grade,
            "price": bid.get("cashBid", "--"),
            "change": bid.get("change", "-")
        })

# ---------------------------------------
# MORNING REPORT
# ---------------------------------------

coffeeReport = (
    "Cash grain bids updated directly from Ritzville. "
    "Markets continue to watch weather, export demand, "
    "and protein premiums."
)

# ---------------------------------------
# OUTPUT JSON
# ---------------------------------------

data = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),

    "marketMood": "Bullish",

    "coffeeReport": coffeeReport,

    "wheat": wheat,

    "crops": [],

    "livestock": [],

    "financial": [],

    "weather": {
        "location": "Ritzville, WA",
        "temp": "--",
        "conditions": "Updating..."
    }
}

with open("market-data.json", "w") as f:
    json.dump(data, f, indent=4)

print("AgMarketReport updated.")
