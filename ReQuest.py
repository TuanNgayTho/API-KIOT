import requests
from datetime import date
import time
import random


starttime = ''
endtime = ''
xacnhan = ''
phieutam = ''
hoanthanh = ''

today = date.today()
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
            'status': [1, 3, 5],
            'lastModifiedFrom': today,
            'toDate': endtime,
            }


def run():
    while True:
        global f
        time.sleep(random.randint(1, 2))

        x = requests.post(urlToken, data=myobj)
        a = x.json()
        b = a["access_token"]
        c = str(b)

        header = {
            'Retailer': 'tmktek',
            'Authorization': 'Bearer ' + c,
        }

        d = requests.get(urlStatus, params=myStatus, headers=header)
        e = d.json()
        f = e['data']
        return e['data']


f = run()

