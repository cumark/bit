#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import collections
import datetime
import json
import math
import random
import sys
import time
from pathlib import Path

import requests
from playwright.async_api import async_playwright, Page, Route, Request, BrowserContext

from see import get_proxies,get_proxies_with_retry


async def generate_tokens(page: Page):
    '获取recaptcha v3 token'
    await page.click('#submitLogin')


import urllib.parse

tokens = []


async def intercept_signin(route: Route, request: Request):
    post_data = request.post_data
    s = urllib.parse.unquote(post_data[5:])
    data = json.loads(s)
    global tokens
    tokens.append(data['recaptchaToken'])
    await route.abort()


def generate_ano_token():
    n = 16
    i = lambda t: hex(math.floor(t))
    first = i(int(time.time()))[2:]

    second = [i(random.random() * n) for _ in range(n)]
    t = ''
    for s in second:
        t += s[2:]
    anonymoustoken = f"{first}" + t
    anonymoustoken = anonymoustoken[:-4] + 'anon'
    return anonymoustoken
async def launch_chrome(playwright) -> BrowserContext :
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    context = await browser.new_context()
    await context.route('https://salad.academy/api/signin',
                        intercept_signin)
    return context
async def goto_signin_page(context:BrowserContext):
    sign_in_page = await context.new_page()

    await sign_in_page.goto("https://salad.academy/")
    l = sign_in_page.locator("text=Sign in").first

    await l.click()
    return sign_in_page
async def main(start=1,end=1):
    faild_accouns_txt = 'register_failed.txt'
    success_accouns_dir  = Path('salad_register_success')
    success_accouns_dir.mkdir(exist_ok=True)
    playwright =  await async_playwright().start()
    context:BrowserContext = await launch_chrome(playwright)
    sign_in_page = await context.new_page()

    await sign_in_page.goto("https://salad.academy/")
    l = sign_in_page.locator("text=Sign in").first

    await l.click()

    global signin_end
    global get_token
    global tokens
    max_retry_times = 10
    count_number = 0
    for i in range(start,end+1):
        mail = f'{i}@cgy188.com'
        password = '123123123'
        # print('用浏览器尝试解决中，mail:', mail)
        e = await sign_in_page.query_selector('#submitLogin')
        class_ = 'btn-loading'
        string = await e.get_attribute('class')
        string = string.replace(' btn-loading','')
        evaluate_code = f"x=> x.setAttribute('class','{string}')"
        await e.evaluate(evaluate_code)

        l = sign_in_page.locator("#submitLogin > span").first
        await l.click()
        await asyncio.sleep(1.5)


        recaptchaToken = tokens[count_number]
        url = 'https://salad.academy/api/users'
        anonymoustoken = generate_ano_token()
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'token': '',
            "anonymous-token": anonymoustoken,
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "lw-client": "61de37f84568d5334437bdab",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "referer": "https://salad.academy/"
        }
        data1 =  {"username": str(mail), "email": mail,
            "password": password, "custom_fields": {},
            "avatar": "https://cdn.mycourse.app/v2.0.9/images/empty-avatar.jpg"
               , "account": {"type": "learnworlds"}, "eu_customer": 'false', "recaptchaToken": recaptchaToken}
        data = 'data=' + urllib.parse.quote(
            json.dumps(data1))
        proxies = get_proxies_with_retry()
        try:
            r = requests.post(url, headers=headers, data=data, proxies=proxies,timeout=6)
        except Exception as e:
            s = f'登录邮箱：{mail} 400出错，出错原因：{e}'
            print(s)
            with open(faild_accouns_txt, 'a', encoding='utf8') as f:
                f.write(f"{s} \n")
            continue

        # print(f'状态码:{r.status_code}')
        # print(f'结果{r.text}')
        if r.status_code == 400:
            print(f'注册邮箱：{mail} 400出错，出错原因：未知',r.text)
            #重新启动浏览器生成token
            with open(faild_accouns_txt,'a',encoding='utf8') as f:
                f.write(f"{mail}\n")
            await context.close()
            playwright =  await async_playwright().start()
            context: BrowserContext = await launch_chrome(playwright)

            sign_in_page = await goto_signin_page(context)
            await asyncio.sleep(1)
        if 'success' in r.text:
            print(f'注册邮箱：{mail}, 注册时间{datetime.datetime.now()}')
            with open(success_accouns_dir / f"{mail}.txt", 'w', encoding='utf8') as f:
                f.write(f"{mail}\n")
        await asyncio.sleep(1)
        count_number +=1
    await context.close()


if __name__ == '__main__':
    # python register_salad.py 1 5
    # 注册 1@cgy188.com 到5@cgy188.com的账号
    start = sys.argv[1]
    end = sys.argv[2]
    start = int(start)
    end = int(end)
    try:
        post = sys.argv[3]
    except:
        post = '@liniuniu.top'
    asyncio.run(main(start,end))
