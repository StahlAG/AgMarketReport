import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://www.ritzwhse.com/cash-bids"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

print("Downloading page...")

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()

print("Page downloaded.")

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text("\n", strip=True)
lines = [line.strip() for line in text.split("\n") if line.strip()]

today = datetime.now()

wheat = []

for i, line in enumerate(lines):

    if line.startswith("10-SWH"):
        wheat.append({
            "market": "Soft White Wheat",
            "price": float(lines[i + 4]),
            "change": "-"
        })

    elif line.startswith("12-WHC"):
        wheat.append({
            "market": "White Wheat 12%",
            "price": float(lines[i + 4]),
            "change": "-"
        })

    elif line.startswith("20-HRW"):
        wheat.append({
            "market": "Hard Red Winter",
            "price": float(lines[i + 4]),
            "change": "-"
        })

    elif line.startswith("30-DNS"):
        wheat.append({
            "market": "Dark Northern Spring",
            "price": float(lines[i + 4]),
            "change": "-"
        })

print("Found wheat bids:")
print(wheat)

market = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": "Neutral",
    "coffeeReport": "Today's Ritzville grain bids have been updated.",
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

print("Done.")
