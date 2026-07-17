fetch("market-data.json")
.then(response => response.json())
.then(data => {
    alert("Script Loaded");
    console.log(data);

    if (data.ritzville &&
        data.ritzville.cashBids &&
        data.ritzville.cashBids.length >= 4) {

        const bids = data.ritzville.cashBids;

        document.getElementById("softWhite").innerHTML = "$" + bids[0].price;
        document.getElementById("white12").innerHTML = "$" + bids[1].price;
        document.getElementById("hrw").innerHTML = "$" + bids[2].price;
        document.getElementById("dns").innerHTML = "$" + bids[3].price;
    }

})
.catch(error => console.log(error));
