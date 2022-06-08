setInterval(myfunc,1000);
function myfunc(){
    $.get( "api/danhsach/", function( data ) {
        var DataTable = '';
        data.forEach(element => {
            var tr =
            `
                <tr>
                    <td>${element.customerName}</td>
                    <td>${element.purchaseDate}</td>
                    <td>${element.soldByName}</td>
                </tr>
            `
            DataTable += tr
        });
        $( "#mytb" ).html(DataTable);
    });
}
//document.getElementById("mytb").innerHTML = myfunc();