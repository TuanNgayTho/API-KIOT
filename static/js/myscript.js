setInterval(myfunc,500);
var phieutam = document.getElementById('PT');
var daxacnhan = document.getElementById('DXN');
var hoanthanh = document.getElementById('HT');
var thisweek = document.getElementById('thisweek');
var luachonkhac = document.getElementById('luachonkhac');
var today = document.getElementById('today');
var thangnay = document.getElementById('thangnay');

phieutam.checked = true;
daxacnhan.checked = true;
hoanthanh.checked = true;
function myfunc(){
    $.get( "/api/phieutam/", function( data ) {
        var DataTable = '';
        data.forEach(element => {
            if (phieutam.checked == true ){
                if(element.statusValue == 'Phiếu tạm' ){
                    var tr =
                    `
                        <tr>
                            <td>${element.customerName}</td>
                        </tr>
                    `
                    DataTable += tr
                }
            }
        });
        $( "#tbtamthu" ).html(DataTable);
    });
    $.get( "/api/xacnhan/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        if (daxacnhan.checked == true ){
            if(element.statusValue == 'Đã xác nhận' ){
                var tr =
                `
                    <tr>
                        <td>${element.customerName}</td>
                    </tr>
                `
                DataTable += tr
            }
        }
    });
    $( "#tbxacnhan" ).html(DataTable);
});
    $.get( "/api/hoanthanh/", function( data ) {
    var DataTable = '';
    data.forEach(element => {
        if (hoanthanh.checked == true ){
            if(element.statusValue == 'Hoàn thành' ){
                var tr =
                `
                    <tr>
                        <td>${element.customerName}</td>
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
var title =
        `
            <tr>
                <th>Tên khách hàng</th>
            </tr>
        `

if (phieutam.checked == true ){
    document.getElementById("mytable1").innerHTML = title;
}else{
    document.getElementById("mytable1").innerHTML = '';
}

if (daxacnhan.checked == true ){
    document.getElementById("mytable2").innerHTML = title;
}else{
    document.getElementById("mytable2").innerHTML = '';
}

if (hoanthanh.checked == true ){
    document.getElementById("mytable3").innerHTML = title;
}else{
    document.getElementById("mytable3").innerHTML = '';
}
}

$.get( "/api/chedotimkiem/", function( data ) {
    data.forEach(element => {
        if(element.ToDay == 'True'){
            today.checked = true;
            thisweek.checked = false;
            thangnay.checked = false;
            luachonkhac.checked = false;
            document.getElementById("lastModifiedFrom").value = element.ThoiGianBatDau;
            document.getElementById('toDate').value = element.THoiGianKetThuc;
        }
        if(element.ThisWeek == 'True'){
            today.checked = false;
            thisweek.checked = true;
            thangnay.checked = false;
            luachonkhac.checked = false;
            document.getElementById("lastModifiedFrom").value = element.ThoiGianBatDau;
            document.getElementById('toDate').value = element.THoiGianKetThuc;
            console.log(element.THoiGianKetThuc)
        }
        if(element.ThisMonth == 'True'){
            today.checked = false;
            thisweek.checked = false;
            thangnay.checked = true;
            luachonkhac.checked = false;
            document.getElementById("lastModifiedFrom").value = element.ThoiGianBatDau;
            document.getElementById('toDate').value = element.THoiGianKetThuc;
            console.log(element.THoiGianKetThuc)
        }
        if(element.CheDoTimKiem == 'True'){
            today.checked = false;
            thisweek.checked = false;
            thangnay.checked = false;
            luachonkhac.checked = true;
            document.getElementById("lastModifiedFrom").value = element.ThoiGianBatDau;
            document.getElementById('toDate').value = element.THoiGianKetThuc;
            console.log(element.THoiGianKetThuc)
        }
    });
});

function myfunc1(){
    if(thisweek.checked == true){
        luachonkhac.checked = false;
        today.checked = false;
        thangnay.checked = false;
    }
}
function myfunc2(){
    if(luachonkhac.checked == true){
        thisweek.checked = false;
        today.checked = false;
        thangnay.checked = false;
    }
}
function myfunc3(){
    if(today.checked == true){
        thisweek.checked = false;
        luachonkhac.checked = false;
        thangnay.checked = false;
    }
}
function myfunc4(){
    if(thangnay.checked == true){
        thisweek.checked = false;
        today.checked = false;
        luachonkhac.checked = false;
    }
}