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

# Save the HTML so we can inspect it if needed
with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print("\n----- PAGE TEXT -----\n")

text = soup.get_text("\n", strip=True)

for line in text.split("\n"):
    if line.strip():
        print(line)

today = datetime.now()

market = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": "Neutral",
    "coffeeReport": "Updating market data...",
    "wheat": [],
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

print("\nDone.")
