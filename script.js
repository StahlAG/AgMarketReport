// ===============================
// AgMarketReport
// ===============================

fetch("market-data.json")
.then(response => response.json())
.then(data => {

    document.getElementById("todayDate").innerHTML = data.date;
    document.getElementById("lastUpdated").innerHTML = data.updated;
    document.getElementById("marketMood").innerHTML = data.marketMood;
    document.getElementById("summary").innerHTML = data.coffeeReport;

    function buildTable(id, rows) {

        let html = "";

        rows.forEach(row => {

            html += "<tr>";
            html += `<td>${row.market}</td>`;
            html += `<td>${row.price}</td>`;
            html += `<td>${row.change}</td>`;
            html += "</tr>";

        });

        document.getElementById(id).innerHTML = html;
    }

    buildTable("wheatTable", data.wheat);
    buildTable("cropTable", data.crops);
    buildTable("livestockTable", data.livestock);
    buildTable("financialTable", data.financial);

});

const btn = document.getElementById("darkModeBtn");

btn.onclick = function () {

    document.body.classList.toggle("dark");

    if (document.body.classList.contains("dark")) {
        btn.innerHTML = "☀️ Light Mode";
    } else {
        btn.innerHTML = "🌙 Dark Mode";
    }

};
