import requests
import time
import random
import mysql.connector


f = ''
xacnhan = ''
phieutam = ''
hoanthanh = ''


urlToken = 'https://id.kiotviet.vn/connect/token'
urlStatus = 'https://public.kiotapi.com/orders'
myobj = {'scopes': 'PublicApi.Access',
         'grant_type': 'client_credentials',
         'client_id': '6378e360-8136-458d-8eae-e9a882e84caa',
         'client_secret': '44E20528CABF2FC8D0CBDC02C8886688B2F316C1',
         }
myStatus = {
            # 'status': input('1: Phiếu tạm\n'
            #                 '2: Đang giao hàng\n'
            #                 '3: Hoàn thành\n'
            #                 '4: Đã hủy\n'
            #                 '5: Đã xác nhận\n'
            #                 'Vui lòng chọn trạng thái đơn hàng: '),
            # 'status': [1, 3, 5],
            # 'lastModifiedFrom': starttime,
            # 'toDate': endtime,
            }


def getdata():
    while True:
        global f
        time.sleep(random.randint(1, 2))

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="kiotapi"
        )
        mycursor = mydb.cursor()
        sql = "SELECT * FROM kiotapi_thoigian WHERE id ='1'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        starttime = myresult[2]
        endtime = myresult[3]

        x = requests.post(urlToken, data=myobj)
        a = x.json()
        b = a["access_token"]
        c = str(b)

        header = {
            'Retailer': 'tmktek',
            'Authorization': 'Bearer ' + c,
        }

        d = requests.get(urlStatus, params={'status': [1, 3, 5],
                                            'pageSize': 100,
                                            'lastModifiedFrom': starttime,
                                            'toDate': endtime}, headers=header)
        e = d.json()
        f = e['data']
        for m in f:
            n = m['purchaseDate']
            p = n.replace("T", "  Giờ: ")
            m["purchaseDate"] = p
        return f


def run():
    getdata()
