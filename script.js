const bids = [

["Soft White Wheat","5.85","+0.02"],
["White Wheat 12%","6.35","+0.01"],
["Hard Red Winter","6.69","-0.03"],
["Dark Northern Spring","6.48","+0.04"]

];

let html="";

bids.forEach(row=>{

html+=`

<div>${row[0]}</div>

<div class="bid">$${row[1]}</div>

<div class="change">${row[2]}</div>

`;

});

document.getElementById("ritzville-grid").innerHTML=html;
