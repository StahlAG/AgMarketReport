// =====================================
// AgMarketReport
// Reads market-data.json
// =====================================

fetch("market-data.json")
    .then(response => response.json())
    .then(data => {

        // Header
        document.getElementById("todayDate").textContent = data.date;
        document.getElementById("marketMood").textContent = data.marketMood;
        document.getElementById("summary").textContent = data.coffeeReport;
        document.getElementById("lastUpdated").textContent = data.updated;

        // Build any table
        function buildTable(tableId, rows) {

            const table = document.getElementById(tableId);

            if (!table) return;

            table.innerHTML = "";

            if (!rows || rows.length === 0) {
                table.innerHTML =
                    "<tr><td colspan='3'>No data available</td></tr>";
                return;
            }

            rows.forEach(row => {

                table.innerHTML += `
                    <tr>
                        <td>${row.market}</td>
                        <td>${row.price}</td>
                        <td>${row.change}</td>
                    </tr>
                `;

            });

        }

        buildTable("wheatTable", data.wheat);
        buildTable("cropTable", data.crops);
        buildTable("livestockTable", data.livestock);
        buildTable("financialTable", data.financial);

        // Weather
        if (data.weather) {

            document.getElementById("weather").innerHTML = `
                <p>${data.weather.location}</p>
                <h3>${data.weather.temp}</h3>
                <p>${data.weather.conditions}</p>
            `;

        }

    })

    .catch(error => {

        console.error(error);

        document.getElementById("summary").textContent =
            "Unable to load market data.";

    });


// =====================================
// Dark Mode
// =====================================

const btn = document.getElementById("darkModeBtn");

btn.addEventListener("click", () => {

    document.body.classList.toggle("dark");

    btn.textContent =
        document.body.classList.contains("dark")
            ? "☀️ Light Mode"
            : "🌙 Dark Mode";

});
