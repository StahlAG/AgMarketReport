import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

today = datetime.now()

url = "https://www.ritzwhse.com/cash-bids"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

prices = []

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")

    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all(["td","th"])]

        if len(cols) >= 2:
            prices.append(cols)

else:
    print("Unable to download Ritzville bids")

wheat = []

for row in prices:

    text = " ".join(row)

    if "10-SWH" in text:
        wheat.append({"market":"10 SWH","price":row[-1],"change":"-"})

    elif "12-WHC" in text:
        wheat.append({"market":"12 WHC","price":row[-1],"change":"-"})

    elif "20-HRW" in text:
        wheat.append({"market":"20 HRW","price":row[-1],"change":"-"})

    elif "30-DNS" in text:
        wheat.append({"market":"30 DNS","price":row[-1],"change":"-"})

marketMood = "Neutral"

coffeeReport = (
    f"Good morning! Local cash wheat bids were updated automatically from "
    f"Ritzville Warehouse at {today.strftime('%I:%M %p')}. "
    f"Additional grain and livestock markets will be added next."
)

data = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": marketMood,
    "coffeeReport": coffeeReport,

    "wheat": wheat,

    "crops": [
        {"market":"Canola","price":"Coming Soon","change":"-"},
        {"market":"Corn","price":"Coming Soon","change":"-"}
    ],

    "livestock":[
        {"market":"Live Cattle","price":"Coming Soon","change":"-"},
        {"market":"Feeder Cattle","price":"Coming Soon","change":"-"}
    ],

    "financial":[],

    "weather":{
        "location":"Washington",
        "temp":"--",
        "conditions":"Updating..."
    }
}

with open("market-data.json","w") as f:
    json.dump(data,f,indent=4)

print("Market report updated successfully.")
