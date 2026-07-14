import json
from datetime import datetime

today = datetime.now()

# Simple rule-based market summary
summary = (
    "Markets are mixed this morning. "
    "Watch wheat, canola, cattle, and weather forecasts throughout the day."
)

# Default market data (we'll replace these with live prices later)
data = {
    "date": today.strftime("%A, %B %d, %Y"),
    "updated": today.strftime("%I:%M %p"),
    "marketMood": "Bullish",
    "coffeeReport": summary,

    "wheat": [
        {"market": "Portland HRS", "price": 6.45, "change": 0.09},
        {"market": "Portland HRW", "price": 6.12, "change": -0.03},
        {"market": "Montana HRS", "price": 6.70, "change": 0.12},
        {"market": "Montana HRW", "price": 6.25, "change": 0.08},
        {"market": "Chicago HRW", "price": 5.75, "change": 0.07},
        {"market": "Kansas City HRW", "price": 6.05, "change": -0.04}
    ],

    "crops": [
        {"market": "Canola", "price": 585.50, "change": 2.30},
        {"market": "Barley", "price": 4.95, "change": 0.10},
        {"market": "Corn", "price": 4.48, "change": 0.03},
        {"market": "Lentils", "price": 0.38, "change": 0.01},
        {"market": "Peas", "price": 6.40, "change": 0.05},
        {"market": "Timothy Hay", "price": 235.00, "change": 5.00},
        {"market": "Alfalfa", "price": 210.00, "change": 4.00}
    ],

    "livestock": [
        {"market": "Live Cattle", "price": 204.25, "change": 1.10},
        {"market": "Feeder Cattle", "price": 288.50, "change": 2.35},
        {"market": "Lean Hogs", "price": 96.75, "change": -0.25}
    ],

    "financial": [
        {"market": "S&P 500", "value": 5912.17, "change": 0.42},
        {"market": "Dow Jones", "value": 42215.73, "change": 0.28},
        {"market": "Nasdaq", "value": 19175.87, "change": 0.39},
        {"market": "US Dollar", "value": 104.25, "change": -0.22},
        {"market": "Crude Oil", "value": 77.91, "change": 0.76}
    ],

    "weather": {
        "location": "Central Plains",
        "temp": "78°F",
        "conditions": "Sunny"
    }
}

with open("market-data.json", "w") as f:
    json.dump(data, f, indent=4)

print("market-data.json updated successfully.")
