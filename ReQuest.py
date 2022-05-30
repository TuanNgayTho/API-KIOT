import requests

urlToken = 'https://id.kiotviet.vn/connect/token'
urlStatus = 'https://public.kiotapi.com/orders'
myobj = {'scopes': 'PublicApi.Access',
         'grant_type': 'client_credentials',
         'client_id': '6378e360-8136-458d-8eae-e9a882e84caa',
         'client_secret': '44E20528CABF2FC8D0CBDC02C8886688B2F316C1',
         }
myStatus = {
            'status': input('1: Phiếu tạm\n'
                            '2: Đang giao hàng\n'
                            '3: Hoàn thành\n'
                            '4: Đã hủy\n'
                            '5: Đã xác nhận\n'
                            'Vui lòng chọn trạng thái đơn hàng: ')
            # 'status': 2
            }

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
g = f[0]

print(len(f))
for h in f:
    print(h)
# print(g["statusValue"])
