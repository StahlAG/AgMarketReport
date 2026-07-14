// ===============================
// AgMarketReport Version 1
// ===============================

// Today's Date
const today = new Date();

document.getElementById("todayDate").innerHTML =
today.toLocaleDateString("en-US",{
weekday:"long",
year:"numeric",
month:"long",
day:"numeric"
});

document.getElementById("lastUpdated").innerHTML =
today.toLocaleString();

// ----------------------
// Market Mood
// ----------------------

document.getElementById("marketMood").innerHTML="🟢 Bullish";

// ----------------------
// Morning Summary
// ----------------------

document.getElementById("summary").innerHTML=
"Wheat is slightly higher this morning. Canola remains strong while cattle markets continue to trade higher. Markets are watching weather and export demand.";


// ----------------------
// Tables
// ----------------------

const wheat=[

["Portland HRS","6.45","▲ 0.09"],
["Portland HRW","6.12","▼ 0.03"],
["Montana HRS","6.70","▲ 0.12"],
["Montana HRW","6.25","▲ 0.08"],
["Chicago HRW","5.75","▲ 0.07"],
["Kansas City HRW","6.05","▼ 0.04"]

];

const crops=[

["Canola","585.50","▲ 2.30"],
["Barley","4.95","▲ 0.10"],
["Corn","4.48","▲ 0.03"],
["Lentils","0.38","▲ 0.01"],
["Peas","6.40","▲ 0.05"],
["Timothy Hay","235.00","▲ 5.00"],
["Alfalfa","210.00","▲ 4.00"]

];

const livestock=[

["Live Cattle","204.25","▲ 1.10"],
["Feeder Cattle","288.50","▲ 2.35"],
["Lean Hogs","96.75","▼ 0.25"]

];

const financial=[

["S&P 500","5912","+0.42%"],
["Dow Jones","42215","+0.28%"],
["NASDAQ","19175","+0.39%"],
["Dollar Index","104.25","-0.22%"],
["Crude Oil","77.91","+0.76%"]

];

function buildTable(id,data){

let html="";

data.forEach(function(row){

html+="<tr>";

row.forEach(function(col){

html+="<td>"+col+"</td>";

});

html+="</tr>";

});

document.getElementById(id).innerHTML=html;

}

buildTable("wheatTable",wheat);

buildTable("cropTable",crops);

buildTable("livestockTable",livestock);

buildTable("financialTable",financial);

// ----------------------
// Dark Mode
// ----------------------

const btn=document.getElementById("darkModeBtn");

btn.onclick=function(){

document.body.classList.toggle("dark");

if(document.body.classList.contains("dark")){

btn.innerHTML="☀️ Light Mode";

}
else{

btn.innerHTML="🌙 Dark Mode";

}

};
