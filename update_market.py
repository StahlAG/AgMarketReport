import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://www.ritzwhse.com/cash-bids"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

today = datetime.now()

wheat = []

# ---------- Find every table row ----------
for row in soup.find_all("tr"):

    cols = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
    print(cols)

    if len(cols) < 3:
        continue

    print(cols)          # <-- TEMPORARY (important)

market = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": "Neutral",

    "coffeeReport":
        "Gathering today's Ritzville grain bids.",

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
    json.dump(market, f, indent=4)

print("Done")
