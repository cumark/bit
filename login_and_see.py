#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import collections
import datetime
import json
import math
import os
import random
import sys
import time
import traceback
from pathlib import Path

import requests
from playwright.async_api import async_playwright, Page, Route, Request, BrowserContext

from see import get_proxies, get_proxies_with_retry,see_videos,success,fail

def start_see(mail,proxies):
    try:
        start = time.time()
        r = see_videos(mail, proxies=proxies)
        if r:
            print(f'{mail} see success {time.time() - start:.2f}s')
            success(mail)
        else:
            fail(mail)
    except Exception as e:
        print(f'mail:{mail},see videos error:{e}')
        traceback.print_exc()
        fail(mail)
async def generate_tokens(page: Page):
    '获取recaptcha v3 token'
    await page.click('#submitLogin')


import urllib.parse

tokens = []
last_token = ''
account_done = 0
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
async def run(playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://example.com")
    await page.screenshot(path="screenshot.png")
    await browser.close()
async def launch_chrome(playwright,proxies=None,chrome=False) -> BrowserContext :
    proxy = None
    if proxies:
        proxy = {'server': proxies['http']}

    firefox = False
    if firefox:
        engine = playwright.firefox
        context = await engine.launch_persistent_context(user_data_dir='firefox_data',headless=False, proxy=proxy)
    else:
        engine = playwright.chromium
        context = await engine.launch_persistent_context(user_data_dir='chrome_data',headless=False, proxy=proxy, channel='chrome')
    await context.route('https://salad.academy/api/signin',
                        intercept_signin)
    return context
async def goto_signin_page(context:BrowserContext):
    sign_in_page = await context.new_page()

    await sign_in_page.goto("https://salad.academy/")
    l = sign_in_page.locator("text=Sign in").first

    await l.click()
    return sign_in_page
def random_select_box_point(start_x, start_y, width, height,margin_ratio=0.05):
    """
    margin_ratio: The ratio of margin of the box
    """

    end_x = start_x + width
    end_y = start_y + height
    x_margin = width*margin_ratio
    y_margin = height*margin_ratio
    x = random.uniform(start_x+x_margin, end_x-x_margin)
    y = random.uniform(start_y+y_margin, end_y-y_margin)
    return x, y
async def main(start=1,end=1,proxy_abled=True,see=True):
    faild_accouns_txt = 'login_failed.txt'
    success_accouns_dir  = Path('salad_login_success')
    success_accouns_dir.mkdir(exist_ok=True)
    playwright =  await async_playwright().start()
    proxies = get_proxies_with_retry()
    # proxies = None
    context:BrowserContext = await launch_chrome(playwright,proxies=proxies)
    sign_in_page = await context.new_page()

    # await sign_in_page.route("**/*", lambda route: route.abort()
    # if route.request.resource_type == "image"
    # else route.continue_())
    await sign_in_page.goto("https://salad.academy/")
    l = sign_in_page.locator("text=Sign in").first

    await l.click()

    global tokens
    global last_token
    global account_done
    count_number = 0
    for i in range(start, end + 1):
        count_number +=1
        mail = f'{i}@cgy188.com'
        password = '123123123123'

        if os.path.exists(success_accouns_dir / f"{mail}.txt"):
            print(f'{mail}账号已登录')
            account_done +=1
            continue

        print('正在产token，mail:', mail)
        e = await sign_in_page.query_selector('#submitLogin')
        class_ = 'btn-loading'
        string = await e.get_attribute('class')
        string = string.replace(' btn-loading','')
        evaluate_code = f"x=> x.setAttribute('class','{string}')"
        await e.evaluate(evaluate_code)

        l = sign_in_page.locator("#submitLogin > span").first
        # await l.click()
        box = await l.bounding_box()
        x,y = random_select_box_point(box['x'], box['y'], box['width'], box['height'])

        await sign_in_page.mouse.click(x,y,delay=5)
        await asyncio.sleep(3)
        recaptchaToken = None
        for i in range(5):
            if len(tokens)>=1 and last_token != tokens[-1]:
                recaptchaToken = tokens[-1]
                last_token = recaptchaToken
                print('产token成功，mail:', mail)
                break
            else:
                await asyncio.sleep(2)
        else:
            print(f'没有 token..{mail}')
            continue
        url = 'https://salad.academy/api/signin'
        anonymoustoken = generate_ano_token()
        # server
        ua = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        # local
        # ua =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
        headers = {
            'user-agent': ua,
            'token': '',
            "anonymous-token": anonymoustoken,
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "lw-client": "61de37f84568d5334437bdab",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "referer": "https://salad.academy/"
        }
        data = 'data=' + urllib.parse.quote(
            json.dumps({"email": mail, "password": password, "recaptchaToken": recaptchaToken}))

        try:

            r = requests.post(url, headers=headers, data=data, proxies=proxies,timeout=6)
        except Exception as e:
            s = f'登录邮箱：{mail}出错，出错原因：{e}'
            print(s)
            with open(faild_accouns_txt, 'a', encoding='utf8') as f:
                f.write(f"{s} \n")
            continue

        print(f'状态码:{r.status_code} 结果{r.text}')
        if r.status_code == 400:
            print(f'登录邮箱：{mail} 400出错，出错原因：未知',r.text)
            #重新启动浏览器生成token
            with open(faild_accouns_txt,'a',encoding='utf8') as f:
                f.write(f"{mail} 400 \n")
            await context.close()
            proxies = get_proxies_with_retry()
            playwright =  await async_playwright().start()
            context: BrowserContext = await launch_chrome(playwright,proxies=proxies)

            sign_in_page = await goto_signin_page(context)
            await asyncio.sleep(1)
        if '{"errors":[], "success":true}' in r.text:
            print(f'登录邮箱成功：{mail}, 登录时间{datetime.datetime.now()}')
            with open(success_accouns_dir / f"{mail}.txt", 'w', encoding='utf8') as f:
                f.write(json.dumps(r.cookies.get_dict()))
            if see:
                start_see(mail,proxies)
        await asyncio.sleep(1)
    await context.close()


def login_account_done(start, end):
    done = 0
    for i in range(start, end + 1):
        mail = f'{i}@cgy188.com'
        success_dir = Path('salad_login_success')

        if os.path.exists(success_dir / f"{mail}.txt"):
            print(f'{mail}账号已观看完成')
            done += 1
    print('还需要登录账号：',end+1-start-done, ' 个')
    if done == end + 1 - start:
        return True
    else:
        return False
if __name__ == '__main__':
    # python login_salad.py 1 5
    # 登录 1@cgy188.com 到5@cgy188.com的账号

    start = sys.argv[1]
    end = sys.argv[2]
    start = int(start)
    end = int(end)

    post = '@liniuniu.top'
    if not login_account_done(start, end):
        while True:
            asyncio.run(main(start, end,proxy_abled=True,see=False))
            print('等待20分钟...')
            if login_account_done(start,end):
                break
            time.sleep(1200)
    print('完成任务！')