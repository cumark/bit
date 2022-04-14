import time
import requests
from pypasser import reCaptchaV3
ssr://NDMuMTU2LjgzLjg0OjIzMzM6YXV0aF9hZXMxMjhfbWQ1OmFlcy0xMjgtY3RyOnBsYWluOk5USXdNekF4WVdF 

from twocaptcha import TwoCaptcha

""" 
YESCAPTCHA验证码DEMO Requests版本
目标网站 https://www.google.com/recaptcha/api2/demo
这是谷歌官方的演示
谷歌官方是reCaptcha V2
这里只是演示简单的处理
不同的网站需要针对性的提交
参考这个思路即可
不要生搬硬套
"""


import datetime

url='https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQqWkfAAAAACpO9DVBCYse9HQ7JkLnWWwmb587&co=aHR0cHM6Ly9zYWxhZC5hY2FkZW15OjQ0Mw..&hl=zh-CN&v=6pQzWaE1NP-gB4FrqRViKjM-&size=invisible&cb=96h3ll1suwk7'

reCaptcha_response = reCaptchaV3(url)


def login(i):
    while 1:
        url = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQqWkfAAAAACpO9DVBCYse9HQ7JkLnWWwmb587&co=aHR0cHM6Ly9zYWxhZC5hY2FkZW15OjQ0Mw..&hl=zh-CN&v=6pQzWaE1NP-gB4FrqRViKjM-&size=invisible&cb=96h3ll1suwk7'

        reCaptcha_response = reCaptchaV3(url)
        recaptchaToken = reCaptcha_response
        print(recaptchaToken)
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
    for i in range(10,200):
        login(i)
