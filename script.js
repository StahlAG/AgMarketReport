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

    let html = "";

    if (data.ritzville && 
        data.ritzville.cashBids &&
        data.ritzville.cashBids.length > 0) {

        data.ritzville.cashBids.forEach(function(item){

            let arrow = "➖";

            if(item.change.includes("+"))
                arrow = "🟢 ▲";

            if(item.change.includes("-"))
                arrow = "🔴 ▼";

            html += `
            <tr>
                <td>${item.commodity}</td>
                <td>$${item.price}</td>
                <td>${arrow} ${item.change}</td>
            </tr>
            `;

        });

    } else {

        html = `
        <tr>
            <td colspan="3">
                Waiting for live Ritzville bids...
            </td>
        </tr>
        `;

    }

    document.getElementById("ritzville-grain").innerHTML = html;

})
.catch(error => {

    console.log(error);

    document.getElementById("summary").innerHTML =
        "Unable to load market data.";

    document.getElementById("ritzville-grain").innerHTML =
        "<tr><td colspan='3'>Market data unavailable.</td></tr>";

});
