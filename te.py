import requests

for i in range(500,750):
    cnt=str(i)
    proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',}
     #'Cookie': 'slim_session=7otEozF8skmAK8pQkdDnGElyyU95Nsw90BBp6Vq7; _ga=GA1.2.480091820.1649407063; _gid=GA1.2.71216230.1649407063; _gat_gtag_UA_68126873_1=1'
    data = {"username": cnt + "@cgy188.com", "email": cnt + "@cgy188.com",
            "password": "123123123", "custom_fields": {},
            "avatar": "https://cdn.mycourse.app/v2.0.9/images/empty-avatar.jpg"
               , "account": {"type": "learnworlds"}, "eu_customer": 'false'}
    print(data)

    conment = requests.post('https://salad.academy/api/users', headers=headers, json=data)

    print(conment)
    print(i)
# a=requests.get(url="https://salad.academy/start")
# print(a.text)
