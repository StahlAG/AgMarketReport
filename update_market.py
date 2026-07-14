import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.ritzwhse.com/cash-bids"

today = datetime.now()

response = requests.get(URL, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

wheat = []

# Find every commodity section
sections = soup.find_all(["h2", "h3"])

for section in sections:

    commodity = section.get_text(strip=True)

    table = section.find_next("table")

    if table is None:
        continue

    rows = table.find_all("tr")

    for row in rows[1:]:

        cols = row.find_all("td")

        if len(cols) < 2:
            continue

        delivery = cols[0].get_text(strip=True)
        bid = cols[1].get_text(strip=True)

        wheat.append({
            "market": f"{commodity} {delivery}",
            "price": bid,
            "change": ""
        })

data = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": "Bullish",
    "coffeeReport": "Cash bids automatically updated from Ritzville Warehouse.",
    "wheat": wheat,
    "crops": [],
    "livestock": [],
    "financial": [],
    "weather": {
        "location": "Ritzville",
        "temp": "--",
        "conditions": "--"
    }
}

with open("market-data.json", "w") as f:
    json.dump(data, f, indent=4)

print("market-data.json updated.")
