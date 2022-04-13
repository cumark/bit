import json
import random
from multiprocessing import Pool

import requests



def cr(i):
    cnt=str(i)
    ipli = ['us', '', 'kr', 'jp', 'hk', 'tw', 'fr', 'gb', 'de', 'lu', 'ca', 'mx', 'br', 'nz', 'au']
    rrr = random.randint(0, len(ipli) - 1)
    mid = ipli[rrr]
    tiqu = 'http://tiqu.ipidea.io:2330/getProxyIp?big_num=710&return_type=json&lb=1&sb=0&flow=1&regions=' + mid + '&protocol=http'

    resp = requests.get(url=tiqu, timeout=5)
    dataBean = json.loads(resp.text)
    code = dataBean["code"]
    if code == 0:
        threads = []
    ran = random.randint(0, len(dataBean["data"]) - 1)
    proxy = dataBean["data"][ran]
    host = proxy['ip']
    port = proxy['port']
    print(host)
    proxies = {
        'http': 'http://{}:{}'.format(host, port),
        'https': 'http://{}:{}'.format(host, port),
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',}
     #'Cookie': 'slim_session=7otEozF8skmAK8pQkdDnGElyyU95Nsw90BBp6Vq7; _ga=GA1.2.480091820.1649407063; _gid=GA1.2.71216230.1649407063; _gat_gtag_UA_68126873_1=1'
    data = {"username": cnt+"@liniuniu.top", "email": cnt + "@liniuniu.top",
            "password": "cumark", "custom_fields": {},
            "avatar": "https://cdn.mycourse.app/v2.0.9/images/empty-avatar.jpg"
               , "account": {"type": "learnworlds"}, "eu_customer": 'false'}
    print(data['username'])
    while 1:
        conment = requests.post('https://salad.academy/api/users', headers=headers,json=data,proxies=proxies)
        if conment.status_code=='200':
            break
if __name__ == '__main__':
    li=[]
    for i in range(4000):
        li.append(i)
    with Pool(1) as p:
        p.map(cr,li)
