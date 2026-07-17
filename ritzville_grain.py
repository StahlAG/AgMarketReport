import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.ritzwhse.com/cash-bids"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_ritzville_cash_bids():

    print("Downloading Ritzville cash bids...")

    page = requests.get(URL, headers=HEADERS, timeout=30)

    page.raise_for_status()

    text = BeautifulSoup(page.text, "html.parser").get_text("\n")

    bids = []

    products = [
        ("10-SWH", "Soft White Wheat"),
        ("12-WHC", "White Wheat 12%"),
        ("20-HRW", "Hard Red Winter"),
        ("30-DNS", "Dark Northern Spring")
    ]

    for code, name in products:

        pattern = rf"{re.escape(code)}.*?JUL\s*([0-9]+\.[0-9]+)"

        match = re.search(pattern, text, re.S)

        if match:

            bids.append({

                "commodity": name,

                "price": match.group(1),

                "change": ""

            })

    return bids


if __name__ == "__main__":

    prices = get_ritzville_cash_bids()

    for row in prices:

        print(row)
