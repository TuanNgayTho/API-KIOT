setInterval(myfunc,500);
var phieutam = document.getElementById('PT');
var daxacnhan = document.getElementById('DXN');
var hoanthanh = document.getElementById('HT');
var thismonth = document.getElementById('thismonth');
var luachonkhac = document.getElementById('luachonkhac');
var starttime = document.getElementById('lastModifiedFrom');
var endtime = document.getElementById('toDate');
phieutam.checked = true;
daxacnhan.checked = true;
hoanthanh.checked = true;
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
        if (daxacnhan.checked == true ){
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
        }
    });
    $( "#tbxacnhan" ).html(DataTable);
});
    $.get( "/api/danhsach/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        if (hoanthanh.checked == true ){
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
        }
    });
    $( "#tbhoanthanh" ).html(DataTable);
});
    $.get( "/api/chedotimkiem/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        var tr =
        `
            <tr>
                <td>${element.CheDoTimKiem}</td>
                <td>${element.ThoiGianBatDau}</td>
                <td>${element.THoiGianKetThuc}</td>
            </tr>
        `
        DataTable += tr
    });
    $( "#tbtrangthai" ).html(DataTable);
});
}
$.get( "/api/chedotimkiem/", function( data ) {
    data.forEach(element => {
        if(element.CheDoTimKiem == 'True'){
            thismonth.checked = true;
            luachonkhac.checked = false;
        } else{
            thismonth.checked = false;
            luachonkhac.checked = true;
            starttime = element.ThoiGianBatDau;
            alert(thismonth);
        }
    });
});
