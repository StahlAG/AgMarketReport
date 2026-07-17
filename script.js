// =====================================
// AgMarketReport Dashboard V2
// =====================================

fetch("market-data.json")
.then(response => response.json())
.then(data => {

    // -----------------------------
    // Market Mood
    // -----------------------------

    document.getElementById("marketMood").innerHTML =
        data.marketMood || "Loading...";

    // Optional mood bar
    const moodFill = document.getElementById("moodFill");

    if (moodFill) {

        switch ((data.marketMood || "").toLowerCase()) {

            case "bullish":
                moodFill.style.width = "90%";
                moodFill.style.background = "#2f7d32";
                break;

            case "bearish":
                moodFill.style.width = "30%";
                moodFill.style.background = "#c62828";
                break;

            default:
                moodFill.style.width = "60%";
                moodFill.style.background = "#d4a017";
        }
    }

    // -----------------------------
    // Coffee Report
    // -----------------------------

    document.getElementById("summary").innerHTML =
        data.coffeeReport || "Waiting for today's report...";

    // -----------------------------
    // Last Updated
    // -----------------------------

    document.getElementById("lastUpdated").innerHTML =
        "Last Updated: " +
        (data.updated || "Unknown");

    // -----------------------------
// Ritzville Cash Bids
// -----------------------------

if (data.ritzville &&
    data.ritzville.cashBids &&
    data.ritzville.cashBids.length >= 4) {

    const bids = data.ritzville.cashBids;

    document.getElementById("softwhite").innerHTML = "$" + bids[0].price;
    document.getElementById("white12").innerHTML = "$" + bids[1].price;
    document.getElementById("hrw").innerHTML = "$" + bids[2].price;
    document.getElementById("dns").innerHTML = "$" + bids[3].price;

}

    document.getElementById("ritzville-table").innerHTML = html;

})
.catch(error => {

    console.log(error);

    document.getElementById("summary").innerHTML =
        "Unable to load market data.";

    document.getElementById("ritzville-table").innerHTML =
        "<tr><td colspan='3'>Market data unavailable.</td></tr>";

});
