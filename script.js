fetch("market-data.json")
.then(response => response.json())
.then(data => {
if (data.ritzville && data.ritzville.cashBids){

    let html = "";

    data.ritzville.cashBids.forEach(item=>{

        html += `
        <tr>
            <td>${item.commodity}</td>
            <td>$${item.price}</td>
            <td>${item.change}</td>
        </tr>
        `;

    });

    document.querySelector("#ritzville-table tbody").innerHTML = html;

}

})
.catch(error => console.log(error));
