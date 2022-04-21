import datetime
import sys

from twocaptcha import TwoCaptcha

config = {
    'server': '2captcha.com',
    # 填写你在2captcha注册的账号apikey
    'apiKey': 'a2178d431f25780d999c1e5d27e5b9c6',
    'softId': 3370,
    'defaultTimeout': 120,
    'recaptchaTimeout': 600,
    'pollingInterval': 10,
}
solver = TwoCaptcha(**config)


def get_token():
    try:
        saladurl = 'https://salad.academy/'
        sitekey = '6LeQqWkfAAAAACpO9DVBCYse9HQ7JkLnWWwmb587'
        action = 'submit'
        result = solver.recaptcha(sitekey=sitekey,
                                  url=saladurl,
                                  version='v3', action=action, score=0.3
                                  )
        return result['code']
    except:
        get_token()



import requests


def login(i):
    while 1:
        recaptchaToken = get_token()

        print(recaptchaToken)
        #with open('token.txt', 'w', encoding='utf8') as f:
        #    f.write(recaptchaToken)
        # recaptchaToken = None
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            #'token': '',
            #"anonymous-token": "6257a9a0d99914e4faa6anon",
            #"x-requested-with": "XMLHttpRequest",
            #"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            #"lw-client": "61de37f84568d5334437bdab",
            #"accept": "application/json, text/javascript, */*; q=0.01",
            #"accept-language": "en-US,en;q=0.9",
        }
        mail = f"{i}@liniuniu.top"
        url = 'https://salad.academy/api/users'

        r = requests.post(url, headers=headers, json={"username":mail,
                                                        "email": mail,
                                                      "password": "cumark",
                                                      "recaptchaToken": recaptchaToken})
        print(r.status_code)
        if r.status_code==200:
            print(mail)
            break


if __name__ == '__main__':
    start = sys.argv[1]
    end = sys.argv[2]
    start = int(start)
    end = int(end)
    for i in range(start,end):
        login(i)