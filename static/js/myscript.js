setInterval(myfunc,500);
var phieutam = document.getElementById('PT');
phieutam.checked = true;
function myfunc(){
    $.get( "/api/danhsach/", function( data ) {
        var DataTable = '';
        data.forEach(element => {
            if (phieutam.checked == true ){
                if(element.statusValue == 'Phiếu tạm' ){
                    var tr =
                    `
                        <tr>
                            <td>${element.customerName}</td>
                            <td>${element.purchaseDate}</td>
                            <td>${element.soldByName}</td>
                            <td>${element.statusValue}</td>
                        </tr>
                    `
                    DataTable += tr
                }
            }
        });
        $( "#tbtamthu" ).html(DataTable);
    });
    $.get( "/api/danhsach/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        if(element.statusValue == 'Đã xác nhận' ){
            var tr =
            `
                <tr>
                    <td>${element.customerName}</td>
                    <td>${element.purchaseDate}</td>
                    <td>${element.soldByName}</td>
                    <td>${element.statusValue}</td>
                </tr>
            `
            DataTable += tr
        }
    });
    $( "#tbxacnhan" ).html(DataTable);
});
    $.get( "/api/danhsach/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        if(element.statusValue == 'Hoàn thành' ){

            var tr =
            `
                <tr>
                    <td>${element.customerName}</td>
                    <td>${element.purchaseDate}</td>
                    <td>${element.soldByName}</td>
                    <td>${element.statusValue}</td>
                </tr>
            `
            DataTable += tr
        }
    });
    $( "#tbhoanthanh" ).html(DataTable);
});

}
//document.getElementById("tbtamthu").innerHTML = myfunc();