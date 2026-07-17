import requests
from bs4 import BeautifulSoup

URL = "https://www.ritzwhse.com/cash-bids"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_ritzville_cash_bids():

    try:

        response = requests.get(URL, headers=HEADERS, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.find_all("tr")

        bids = []

        for row in rows:

            cols = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]

            if len(cols) < 2:
                continue

            commodity = cols[0]

            if "$" not in " ".join(cols):
                continue

            price = ""

            for col in cols:
                if "$" in col:
                    price = col
                    break

            bids.append({
                "commodity": commodity,
                "cashBid": price,
                "change": "",
                "trend": ""
            })

        return bids

    except Exception as e:

        print(e)

        return []
