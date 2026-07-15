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

# -------------------------
# Find first price after market name
# -------------------------

def find_price(lines, start):
    for j in range(start, start + 15):
        try:
            return float(lines[j])
        except ValueError:
            continue
    return None


# -------------------------
# Wheat Markets
# -------------------------

wheat = []

for i, line in enumerate(lines):

    if line.startswith("10-SWH"):
        price = find_price(lines, i)
        if price is not None:
            wheat.append({
                "market": "Soft White Wheat",
                "price": price,
                "change": "--"
            })

    elif line.startswith("12-WHC"):
        price = find_price(lines, i)
        if price is not None:
            wheat.append({
                "market": "White Wheat 12%",
                "price": price,
                "change": "--"
            })

    elif line.startswith("20-HRW"):
        price = find_price(lines, i)
        if price is not None:
            wheat.append({
                "market": "Hard Red Winter",
                "price": price,
                "change": "--"
            })

    elif line.startswith("30-DNS"):
        price = find_price(lines, i)
        if price is not None:
            wheat.append({
                "market": "Dark Northern Spring",
                "price": price,
                "change": "--"
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
