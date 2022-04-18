import json
import os
import random
import sys
import time
import traceback
import urllib.parse
from pathlib import Path

import requests
import requests.utils


def get_proxies():
    ipli = ['us', '', 'kr', 'jp', 'hk', 'tw', 'fr', 'gb', 'de', 'lu', 'ca', 'mx', 'br', 'nz', 'au']
    rrr = random.randint(0, len(ipli) - 1)
    mid = ipli[rrr]
    tiqu = 'http://tiqu.ipidea.io:2330/getProxyIp?big_num=710&return_type=json&lb=1&sb=0&flow=1&regions=' + mid + '&protocol=http'
    timeout = 5
    resp = requests.get(url=tiqu, timeout=timeout)
    dataBean = json.loads(resp.text)
    if dataBean['msg'] == '请添加白名单':
        print('白名单配置出错')
        return None
    code = dataBean["code"]
    ran = random.randint(0, len(dataBean["data"]) - 1)
    proxy = dataBean["data"][ran]
    host = proxy['ip']
    port = proxy['port']
    proxies = {
        'http': 'http://{}:{}'.format(host, port),
        'https': 'http://{}:{}'.format(host, port),
    }
    print(f"get proxies:{proxies}")
    return proxies
def get_proxies_with_retry():
    proxies_try_time = 3
    try_time = 0
    proxies = None
    while try_time < proxies_try_time:
        try:
            proxies = get_proxies()
            break
        except:
            try_time += 1
            time.sleep(0.5)
    return proxies
def data_to_new_data(dict_data):
    """
    old json version to new form data
    :return:
    """
    data = 'data=' + urllib.parse.quote(
        json.dumps(dict_data))
    return data


def see_videos(mail='859905874@qq.com', proxies=None):
    success_accouns_dir = Path('salad_login_success')
    try:
        with open(success_accouns_dir / f"{mail}.txt", 'r', encoding='utf8') as f:
            cookies = json.loads(f.read())
    except Exception as e:
        print(f'{mail} cookie not exist')
        return False
    session = requests.Session()

    requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
    # print(session.cookies)
    # time.sleep(555)
    headers = {
        'User-Agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"}

    class2 = 'https://salad.academy/api/user/register/6204be454d1e14096f23305a'
    pag = 'https://salad.academy/course/axie-arena-mastery'
    timeout = 8
    con = session.get(url=pag, headers=headers, timeout=timeout, proxies=proxies)
    lw_tokens = cookies.get("lw_tokens")
    # print('set cookies', con.headers['set-cookie'])
    s = urllib.parse.unquote(lw_tokens)
    s = json.loads(s)
    # print(s)
    cont = s['access_token']

    headers = {
        "Token": cont,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Host':'salad.academy',

    }

    r = session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    print(f'{mail}-go', end='|',flush=True)
    class2 = 'https://salad.academy/api/user/register/6204be8c0ed4966476289783'
    session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    class2 = 'https://salad.academy/api/user/register/6204be2a8a40e85191669bd5'
    session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    class2 = 'https://salad.academy/api/user/register/61de38df3a677f27fc14df89'
    session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    class2 = 'https://salad.academy/api/user/register/6204be7484c1f15d5a408bf8'
    session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    class2 = 'https://salad.academy/api/user/register/620364de22971f2fea0060d6'
    session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    class2 = 'https://salad.academy/api/user/register/623d216c4757b2587008d467'
    r = session.post(url=class2, headers=headers, timeout=timeout, proxies=proxies)
    # print(r.text)
    print('step1',end='|',flush=True)

    iden = ['622ac654667d5c50f458ee6d', '620b159b37d5066ec556c1b8', '622ac6b05ab0be2dc810b20c',
            '620b15b88cc6e032a84414e5', '620b15c13f8a6e00f10e3215', '620b15c7bafd926de86f5176'
        , '620b15d0e765e519b97b4386', '622ac7736d33271d27594d4e', '620b15e7e96f6354c23c041a',
            '622ac77d7bc777304c497d4d', '620b15efc5cc7d74902a4036', '620b15f450792d42e075aa25'
        , '622ac7d4b5f7f8433255825b', '620b16069e429d6f170f5ea6', '620b160c7e930d4e1057c328',
            '620b1624389ff46942245ddd', '620b16339bd59712202f135a', '620b164594b94453812b8e77'
        , '620b164ba381275d2070fb56', '620b1650f073d07aea5f9541', '620b165f657c7401c74fe1f8',
            '624026f190c46068eb246f65', '6253bd7c6a6f0b39e168ec7a']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=axie-arena-mastery&unit=" + i + "Unit",
                "context": ["Axie Arena Mastery, Understanding Anesthetic Bait {embed}", "axie-arena-mastery",
                            "axie-_understanding_bug_parts", i, "path"],
                "previousContext": ["Axie Arena Mastery, Understanding Anesthetic Bait {embed}",
                                    "axie-arena-mastery", "axie-_understanding_bug_parts", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=8, proxies=proxies,
                         data=data_to_new_data(data))
    print('step2', end='|',flush=True)
    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/620b165f657c7401c74fe1f8', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))

    headers = {
        "token": cont,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}

    data = {'maxscore': 35, 'answers': [
        {'qId': 'new1644938251345_0_7505278', 'qIndex': 0, 'optionid': 'new1644938251345_0_7505278opt_1'},
        {'qId': 'new1644938251345_0_5419541', 'qIndex': 1, 'optionid': 'new1644938251345_0_5419541opt_2'},
        {'qId': 'new1644938251345_0_4758803', 'qIndex': 2, 'optionid': 'new1644938251345_0_4758803opt_3'},
        {'qId': 'new1644938251345_0_5146844', 'qIndex': 3, 'optionid': 'new1644938251345_0_5146844opt_1'},
        {'qId': 'new1644938251345_0_5112539', 'qIndex': 4, 'optionid': 'new1644938251345_0_5112539opt_2'},
        {'qId': 'new1644938251345_0_5116870', 'qIndex': 5, 'optionid': 'new1644938251345_0_5116870opt_3'},
        {'qId': 'new1644938251345_0_9176059', 'qIndex': 6, 'optionid': 'new1644938251345_0_9176059opt_0'},
        {'qId': 'new1644938251345_0_4087024', 'qIndex': 7, 'optionid': 'new1644938251345_0_4087024opt_0'},
        {'qId': 'new1644938251345_0_3504548', 'qIndex': 8, 'optionid': 'new1644938251345_0_3504548opt_3'},
        {'qId': 'new1644938251345_0_3894516', 'qIndex': 9, 'optionid': 'new1644938251345_0_3894516opt_2'},
        {'qId': 'new1644938251345_0_8151964', 'qIndex': 10, 'optionid': 'new1644938251345_0_8151964opt_0'},
        {'qId': 'new1644938251345_0_1086099', 'qIndex': 11, 'optionid': 'new1644938251345_0_1086099opt_2'},
        {'qId': 'new1644938251345_0_3318181', 'qIndex': 12, 'optionid': 'new1644938251345_0_3318181opt_2'},
        {'qId': 'new1644938251345_0_5525304', 'qIndex': 13, 'optionid': 'new1644938251345_0_5525304opt_2'},
        {'qId': 'new1644938251345_0_7951755', 'qIndex': 14, 'optionid': 'new1644938251345_0_7951755opt_0'},
        {'qId': 'new1644938251345_0_6919476', 'qIndex': 15, 'optionid': 'new1644938251345_0_6919476opt_0'},
        {'qId': 'new1644938251345_0_7639759', 'qIndex': 16, 'optionid': 'new1644938251345_0_7639759opt_2'},
        {'qId': 'new1644938251345_0_9416962', 'qIndex': 17, 'optionid': 'new1644938251345_0_9416962opt_1'},
        {'qId': 'new1644938251345_0_8825754', 'qIndex': 18, 'optionid': 'new1644938251345_0_8825754opt_2'},
        {'qId': 'new1644938251345_0_124299', 'qIndex': 19, 'optionid': 'new1644938251345_0_124299opt_2'},
        {'qId': 'new1644938251345_0_8438963', 'qIndex': 20, 'optionid': 'new1644938251345_0_8438963opt_2'},
        {'qId': 'new1644938251345_0_6133079', 'qIndex': 21, 'optionid': 'new1644938251345_0_6133079opt_2'},
        {'qId': 'new1644938251345_0_1079268', 'qIndex': 22, 'optionid': 'new1644938251345_0_1079268opt_2'},
        {'qId': 'new1644938251345_0_2012756', 'qIndex': 23, 'optionid': 'new1644938251345_0_2012756opt_0'},
        {'qId': 'new1644938251345_0_8331405', 'qIndex': 24, 'optionid': 'new1644938251345_0_8331405opt_0'},
        {'qId': 'new1644938251345_0_5695330', 'qIndex': 25, 'optionid': 'new1644938251345_0_5695330opt_3'},
        {'qId': 'new1644938251345_0_6043723', 'qIndex': 26, 'optionid': 'new1644938251345_0_6043723opt_2'},
        {'qId': 'new1644938251345_0_3056985', 'qIndex': 27, 'optionid': 'new1644938251345_0_3056985opt_2'},
        {'qId': 'new1644938251345_0_1453249', 'qIndex': 28, 'optionid': 'new1644938251345_0_1453249opt_2'},
        {'qId': 'new1644938251345_0_923275', 'qIndex': 29, 'optionid': 'new1644938251345_0_923275opt_2'},
        {'qId': 'new1644938251345_0_5534922', 'qIndex': 30, 'optionid': 'new1644938251345_0_5534922opt_0'},
        {'qId': 'new1644938251345_0_4859312', 'qIndex': 31, 'optionid': 'new1644938251345_0_4859312opt_1'},
        {'qId': 'new1644938251345_0_7447650', 'qIndex': 32, 'optionid': 'new1644938251345_0_7447650opt_1'},
        {'qId': 'new1644938251345_0_8523207', 'qIndex': 33, 'optionid': 'new1644938251345_0_8523207opt_1'},
        {'qId': 'new1644938251345_0_8273723', 'qIndex': 34, 'optionid': 'new1644938251345_0_8273723opt_2'}]}
    e = session.post(url='https://salad.academy/api//score/certificate/620b165f657c7401c74fe1f8', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.patch(url='https://salad.academy/api/assessment/submission/62509fa4054fa90202635494', data=data_to_new_data(data),
                      headers=headers, timeout=timeout, proxies=proxies)
    iden = ['622ac73aac5d1656ea0f6e87', '62060d2b8b60f733bb6a5c1f', '622ac77056ba790fcb60184a',
            '62060d1ecc40d4704270136e', '622ac7c64ea5b3379140ab49', '62060d87e86f8e2a3a328eba',
            '622ac7fe4c9ee9537c0998fd'
        , '622ac859fd516015257f5b44', '62060da8652d26578530a340', '620a18fa5ba7ad2f5d595e29',
            '6240267dd6d2dd42124a0315', '6253c07fd3458f69e0435b61']
    print('step3', end='|',flush=True)
    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=crabada-basic-tutorial&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    print('step4', end='|',flush=True)
    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/620a18fa5ba7ad2f5d595e29', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))

    data = {'maxscore': 16, 'answers': [
        {'qId': 'new1644857727241_0_9843533', 'qIndex': 0, 'optionid': 'new1644857727241_0_9843533opt_2'},
        {'qId': 'new1644857727241_0_3003858', 'qIndex': 1, 'optionid': 'new1644857727241_0_3003858opt_1'},
        {'qId': 'new1644857727241_0_2940026', 'qIndex': 2, 'optionid': 'new1644857727241_0_2940026opt_1'},
        {'qId': 'new1644857727241_0_7621769', 'qIndex': 3, 'optionid': 'new1644857727241_0_7621769opt_0'},
        {'qId': 'new1644857727241_0_146549', 'qIndex': 4, 'optionid': 'new1644857727241_0_146549opt_2'},
        {'qId': 'new1644857727241_0_4080587', 'qIndex': 5, 'optionid': 'new1644857727241_0_4080587opt_1'},
        {'qId': 'new1644857727241_0_3215516', 'qIndex': 6, 'optionid': 'new1644857727241_0_3215516opt_1'},
        {'qId': 'new1644857727241_0_9935326', 'qIndex': 7, 'optionid': 'new1644857727241_0_9935326opt_1'},
        {'qId': 'new1644857727241_0_2221006', 'qIndex': 8, 'optionid': 'new1644857727241_0_2221006opt_1'},
        {'qId': 'new1644857727241_0_690654', 'qIndex': 9, 'optionid': 'new1644857727241_0_690654opt_2'},
        {'qId': 'new1644857727241_0_4573407', 'qIndex': 10, 'optionid': 'new1644857727241_0_4573407opt_1'},
        {'qId': 'new1644857727241_0_1101684', 'qIndex': 11, 'optionid': 'new1644857727241_0_1101684opt_2'},
        {'qId': 'new1644857727241_0_8468596', 'qIndex': 12, 'optionid': 'new1644857727241_0_8468596opt_3'},
        {'qId': 'new1644857727241_0_6573386', 'qIndex': 13, 'optionid': 'new1644857727241_0_6573386opt_3'},
        {'qId': 'new1644857727241_0_4581413', 'qIndex': 14, 'optionid': 'new1644857727241_0_4581413opt_0'},
        {'qId': 'new1644857727241_0_7606134', 'qIndex': 15, 'optionid': 'new1644857727241_0_7606134opt_1'}]}
    # data={"maxscore":35,"answers":[{"qId":"new1644938251345_0_7505278","qIndex":0,"optionid":"new1644938251345_0_7505278opt_1"},{"qId":"new1644938251345_0_5419541","qIndex":"1","optionid":"new1644938251345_0_5419541opt_1"},{"qId":"new1644938251345_0_5146844","qIndex":"3","optionid":"new1644938251345_0_5146844opt_2"},{"qId":"new1644938251345_0_5112539","qIndex":"4","optionid":"new1644938251345_0_5112539opt_2"},{"qId":"new1644938251345_0_5116870","qIndex":"5","optionid":"new1644938251345_0_5116870opt_2"},{"qId":"new1644938251345_0_3504548","qIndex":"8","optionid":"new1644938251345_0_3504548opt_2"},{"qId":"new1644938251345_0_5525304","qIndex":"13","optionid":"new1644938251345_0_5525304opt_2"},{"qId":"new1644938251345_0_7951755","qIndex":"14","optionid":"new1644938251345_0_7951755opt_2"},{"qId":"new1644938251345_0_6919476","qIndex":"15","optionid":"new1644938251345_0_6919476opt_3"},{"qId":"new1644938251345_0_7639759","qIndex":"16","optionid":"new1644938251345_0_7639759opt_1"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/620a18fa5ba7ad2f5d595e29', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.patch(url='https://salad.academy/api/assessment/submission/62509dd3e2a894018c7e38ee', data=data_to_new_data(data),
                      headers=headers, timeout=timeout, proxies=proxies)
    print('step5', end='|',flush=True)
    iden = ['622ac5523f76077600458023', '620615a63b86f26b1e281e9c', '622ac5b4464d356b682196b3',
            '6206159f247ac32eb67b24d6', '622ac615ed49b14e0b21ad00', '620615cd91f8f5031f1206de',
            '622ac6708c6f89689f4b5b85', '620615c4c6464d0658055dd6', '622ac6cb45974b11a118344e',
            '620615e2272597450d3b434f', '6240278276415659c235c7cd', '62061619f1b643619562807e',
            '6253c01b70b6ee7f71237f08']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=deathroad-basic-drivers-license&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/62061619f1b643619562807e', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))

    data = {'maxscore': 20, 'answers': [
        {'qId': 'new1644599187697_0_875250', 'qIndex': 0, 'optionid': 'new1644599187697_0_875250opt_2'},
        {'qId': 'new1644599187697_0_6377748', 'qIndex': 1, 'optionid': 'new1644599187697_0_6377748opt_1'},
        {'qId': 'new1644599187697_0_8076886', 'qIndex': 2, 'optionid': 'new1644599187697_0_8076886opt_3'},
        {'qId': 'new1644599187697_0_1525085', 'qIndex': 3, 'optionid': 'new1644599187697_0_1525085opt_1'},
        {'qId': 'new1644599187697_0_5434384', 'qIndex': 4, 'optionid': 'new1644599187697_0_5434384opt_2'},
        {'qId': 'new1644599187697_0_7110241', 'qIndex': 5, 'optionid': 'new1644599187697_0_7110241opt_2'},
        {'qId': 'new1644599187697_0_8879047', 'qIndex': 6, 'optionid': 'new1644599187697_0_8879047opt_0'},
        {'qId': 'new1644599187697_0_9868922', 'qIndex': 7, 'optionid': 'new1644599187697_0_9868922opt_3'},
        {'qId': 'new1644599187697_0_6981410', 'qIndex': 8, 'optionid': 'new1644599187697_0_6981410opt_2'},
        {'qId': 'new1644599187697_0_4411808', 'qIndex': 9, 'optionid': 'new1644599187697_0_4411808opt_1'},
        {'qId': 'new1644599187697_0_2133563', 'qIndex': 10, 'optionid': 'new1644599187697_0_2133563opt_0'},
        {'qId': 'new1644599187697_0_7347690', 'qIndex': 11, 'optionid': 'new1644599187697_0_7347690opt_2'},
        {'qId': 'new1644599187697_0_2603989', 'qIndex': 12, 'optionid': 'new1644599187697_0_2603989opt_1'},
        {'qId': 'new1644599187697_0_7594732', 'qIndex': 13, 'optionid': 'new1644599187697_0_7594732opt_2'},
        {'qId': 'new1644599187697_0_6950714', 'qIndex': 14, 'optionid': 'new1644599187697_0_6950714opt_1'},
        {'qId': 'new1644599187697_0_8409269', 'qIndex': 15, 'optionid': 'new1644599187697_0_8409269opt_3'},
        {'qId': 'new1644599187697_0_9148260', 'qIndex': 16, 'optionid': 'new1644599187697_0_9148260opt_1'},
        {'qId': 'new1644599187697_0_2271737', 'qIndex': 17, 'optionid': 'new1644599187697_0_2271737opt_2'},
        {'qId': 'new1644599187697_0_9765698', 'qIndex': 18, 'optionid': 'new1644599187697_0_9765698opt_2'},
        {'qId': 'new1644599187697_0_5740081', 'qIndex': 19, 'optionid': 'new1644599187697_0_5740081opt_1'}]}
    # data={"maxscore":35,"answers":[{"qId":"new1644938251345_0_7505278","qIndex":0,"optionid":"new1644938251345_0_7505278opt_1"},{"qId":"new1644938251345_0_5419541","qIndex":"1","optionid":"new1644938251345_0_5419541opt_1"},{"qId":"new1644938251345_0_5146844","qIndex":"3","optionid":"new1644938251345_0_5146844opt_2"},{"qId":"new1644938251345_0_5112539","qIndex":"4","optionid":"new1644938251345_0_5112539opt_2"},{"qId":"new1644938251345_0_5116870","qIndex":"5","optionid":"new1644938251345_0_5116870opt_2"},{"qId":"new1644938251345_0_3504548","qIndex":"8","optionid":"new1644938251345_0_3504548opt_2"},{"qId":"new1644938251345_0_5525304","qIndex":"13","optionid":"new1644938251345_0_5525304opt_2"},{"qId":"new1644938251345_0_7951755","qIndex":"14","optionid":"new1644938251345_0_7951755opt_2"},{"qId":"new1644938251345_0_6919476","qIndex":"15","optionid":"new1644938251345_0_6919476opt_3"},{"qId":"new1644938251345_0_7639759","qIndex":"16","optionid":"new1644938251345_0_7639759opt_1"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/62061619f1b643619562807e', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.post(url='https://salad.academy/api/assessment/submission/6250931eb3e6eb6c0432fc6e', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)
    print('step6', end='|',flush=True)
    iden = ['622abc3967c500505d0292ac', '62031eadb3880755876af8b9', '622ac0fcd303bd31d255eacc',
            '62031cdd6ccafb1f352bf495', '622ac24c030a3f174429c576', '62031f731bdbe860652cbc3a'
        , '622ac2f388c4a3561f3c8160', '62031fca2a1a676b9903ca68', '622ac5e7a234c9025b622065',
            '62031ff6b6f60b612a06f8d3', '6240273ad503602fd97f37b0', '6203600f8e6ad33b402fd218',
            '6253bfd386cfba552c1612ce']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=happyland-basics&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/6203600f8e6ad33b402fd218', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))
    print('step7', end='|',flush=True)

    data = {"maxscore": 18,
            "answers": [{"qId": "imported_9975794", "qIndex": 0, "optionid": "new1643998017846_0_1158452opt_3"},
                        {"qId": "imported_6595722", "qIndex": "1", "optionid": "new1644414865116_0_3266824opt_3"},
                        {"qId": "imported_3268146", "qIndex": "2", "optionid": "new1644414865116_0_5092346opt_2"},
                        {"qId": "imported_3620899", "qIndex": "3", "optionid": "new1644414865116_0_869469opt_2"},
                        {"qId": "imported_1748371", "qIndex": "4", "optionid": "new1644414865116_0_9707626opt_0"},
                        {"qId": "imported_4208887", "qIndex": "5", "optionid": "new1644414865116_0_5235669opt_0"},
                        {"qId": "imported_1693270", "qIndex": "6", "optionid": "new1644414865116_0_8150141opt_2"},
                        {"qId": "imported_8818594", "qIndex": "7", "optionid": "new1644414865116_0_5853482opt_3"},
                        {"qId": "imported_5219527", "qIndex": "8", "optionid": "new1644414865116_0_738551opt_1"},
                        {"qId": "imported_114785", "qIndex": "9", "optionid": "new1644414865116_0_340543opt_2"},
                        {"qId": "imported_3471694", "qIndex": "10", "optionid": "new1644414865116_0_2199952opt_1"},
                        {"qId": "imported_2391022", "qIndex": "11", "optionid": "new1644414865116_0_4797052opt_1"},
                        {"qId": "imported_5093789", "qIndex": "12", "optionid": "new1644414865116_0_3968560opt_3"},
                        {"qId": "imported_9949300", "qIndex": "13", "optionid": "new1644414865116_0_475972opt_2"},
                        {"qId": "imported_2628643", "qIndex": "14", "optionid": "new1644414865116_0_2436808opt_0"},
                        {"qId": "imported_1799917", "qIndex": "15", "optionid": "new1644414865116_0_6916095opt_1"},
                        {"qId": "imported_6615087", "qIndex": "16", "optionid": "new1644414865116_0_7320296opt_2"},
                        {"qId": "imported_6846830", "qIndex": "17", "optionid": "new1644414865116_0_3145492opt_0"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/6203600f8e6ad33b402fd218', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.post(url='https://salad.academy/api/assessment/submission/6250952b81330d67a55b2ebc', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    iden = ['622ac64efb8ccd66020546c9', '620b0f65835e2d1753000e98', '624027df72bfd61b1f27b1de',
            '620b0f84d7fa2d134a4547f4', '6253bb9300bb4b0c39452fee']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=introduction-to-axie-infinity&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/620b0f84d7fa2d134a4547f4', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))
    print('step8', end='|',flush=True)

    data = {"maxscore": 10, "answers": [
        {"qId": "new1644920853015_0_2600952", "qIndex": 0, "optionid": "new1644920853015_0_2600952opt_0"},
        {"qId": "new1644920853015_0_2061501", "qIndex": "1", "optionid": "new1644920853015_0_2061501opt_2"},
        {"qId": "new1644920853015_0_7878475", "qIndex": "2", "optionid": "new1644920853015_0_7878475opt_2"},
        {"qId": "new1644920853015_0_1854083", "qIndex": "3", "optionid": "new1644920853015_0_1854083opt_2"},
        {"qId": "new1644920853015_0_8665009", "qIndex": "4", "optionid": "new1644920853015_0_8665009opt_1"},
        {"qId": "new1644920853015_0_4536314", "qIndex": "5", "optionid": "new1644920853015_0_4536314opt_3"},
        {"qId": "new1644920853015_0_2954371", "qIndex": "6", "optionid": "new1644920853015_0_2954371opt_2"},
        {"qId": "new1644920853015_0_985839", "qIndex": "7", "optionid": "new1644920853015_0_985839opt_0"},
        {"qId": "new1644920853015_0_1884047", "qIndex": "8", "optionid": "new1644920853015_0_1884047opt_3"},
        {"qId": "new1644920853015_0_9433623", "qIndex": "9", "optionid": "new1644920853015_0_9433623opt_2"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/620b0f84d7fa2d134a4547f4', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.post(url='https://salad.academy/api/assessment/submission/625096de8a7d135507761eba', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    iden = ['622ac490bf558552b3773312', '620368d552577826276edd8a', '622ac4ff667d5c50f458ee66',
            '620368ea37180f4e75365e25', '622ac56038cf0a0d743867b7', '62036931341f2a0ff7193fb5'
        , '622ac5d8c7ce240d0937fcf9', '62402876dce4230f33269e21', '620369a15b07243961031fa6',
            '62525c6b0ec4945d984361ef']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=mines-of-dalarnia-basic-tutorial&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/620369a15b07243961031fa6', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))

    data = {"maxscore": 20, "answers": [
        {"qId": "new1644424079213_0_7566613", "qIndex": 0, "optionid": "new1644424079213_0_7566613opt_1"},
        {"qId": "new1644424079213_0_1585467", "qIndex": "1", "optionid": "new1644424079213_0_1585467opt_1"},
        {"qId": "new1644424079213_0_9684253", "qIndex": "2", "optionid": "new1644424079213_0_9684253opt_2"},
        {"qId": "new1644424079213_0_3400841", "qIndex": "3", "optionid": "new1644424079213_0_3400841opt_3"},
        {"qId": "new1644424079213_0_2645243", "qIndex": "4", "optionid": "new1644424079213_0_2645243opt_2"},
        {"qId": "new1644424079213_0_9228491", "qIndex": "5", "optionid": "new1644424079213_0_9228491opt_1"},
        {"qId": "new1644585920729_0_1639400", "qIndex": "6", "optionid": "new1644585920729_0_1639400opt_0"},
        {"qId": "new1644585920729_0_3291804", "qIndex": "7", "optionid": "new1644585920729_0_3291804opt_2"},
        {"qId": "new1644585920729_0_6991120", "qIndex": "8", "optionid": "new1644585920729_0_6991120opt_2"},
        {"qId": "new1644585920729_0_7302211", "qIndex": "9", "optionid": "new1644585920729_0_7302211opt_0"},
        {"qId": "new1644585920729_0_7170750", "qIndex": "10", "optionid": "new1644585920729_0_7170750opt_2"},
        {"qId": "new1644585920729_0_5345162", "qIndex": "11", "optionid": "new1644585920729_0_5345162opt_1"},
        {"qId": "new1644585920729_0_5449815", "qIndex": "12", "optionid": "new1644585920729_0_5449815opt_1"},
        {"qId": "new1644585920729_0_7189574", "qIndex": "13", "optionid": "new1644585920729_0_7189574opt_1"},
        {"qId": "new1644585920729_0_4930586", "qIndex": "14", "optionid": "new1644585920729_0_4930586opt_3"},
        {"qId": "new1644585920729_0_1532246", "qIndex": "15", "optionid": "new1644585920729_0_1532246opt_3"},
        {"qId": "new1644585920729_0_685409", "qIndex": "16", "optionid": "new1644585920729_0_685409opt_1"},
        {"qId": "new1644585920729_0_5190166", "qIndex": "17", "optionid": "new1644585920729_0_5190166opt_3"},
        {"qId": "new1644585920729_0_6983143", "qIndex": "18", "optionid": "new1644585920729_0_6983143opt_1"},
        {"qId": "new1644585920729_0_8593445", "qIndex": "19", "optionid": "new1644585920729_0_8593445opt_1"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/620369a15b07243961031fa6', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.post(url='https://salad.academy/api/assessment/submission/625099d7e007603fad0c505a', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)
    print('step9', end='|',flush=True)

    iden = ['623d249b39165a44637bbab8', '623d251b738f7d296e058ca9', '623d253e3157944c8f7bde47',
            '623d254dd86c320310434345', '623d25b8b65e261fa904c7f6', '623d25bf3de23e78c75ba252'
        , '623d275301188f5d560b6017', '623d2787e90e126b4c0e60ad', '624026b69ab32072b53b4af0',
            '623d285ab937597726670f0e', '6253c0a7a6378d73c40555ee']

    for i in iden:
        data = {"page": "path-player", "pageId": "null",
                "pageUrl": "/path-player?courseid=monsterra-basic-farmer&unit=" + i + "Unit",
                "context": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}", "crabada-basic-tutorial",
                            "craba_understanding_crabada_stats", i, "path"],
                "previousContext": ["Crabada Basic Tutorial, Understanding Crabada Stats {embed}",
                                    "crabada-basic-tutorial", "craba_understanding_crabada_stats", i, "path"],
                "durationSincePrevious": 9, "hidden": "false", "hiddenDuration": 0, "me": "false",
                "inactive": "false", "siteTemplateId": "null", "courseId": "null", "bundleId": "null",
                "subscriptionId": "null", "additionalData": {"progress": {"unitId": i, "completed": "true"}}}
        e = session.post(url='https://salad.academy/api/notifications', headers=headers, timeout=timeout, proxies=proxies,
                         data=data_to_new_data(data))

    data = {
        "firstname": "cu", "lastname": "cu"

    }
    e = session.get(url='https://salad.academy/api/form/certificate/623d285ab937597726670f0e', headers=headers,
                    timeout=timeout, proxies=proxies, data=data_to_new_data(data))

    data = {"maxscore": 15, "answers": [
        {"qId": "new1648204005321_0_5896132", "qIndex": 0, "optionid": "new1648204005321_0_5896132opt_1"},
        {"qId": "new1648204005321_0_7539899", "qIndex": "1", "optionid": "new1648204005321_0_7539899opt_3"},
        {"qId": "new1648204005321_0_6437022", "qIndex": "2", "optionid": "new1648204005321_0_6437022opt_1"},
        {"qId": "new1648204005321_0_2562559", "qIndex": "3", "optionid": "new1648204005321_0_2562559opt_2"},
        {"qId": "new1648204005321_0_7716013", "qIndex": "4", "optionid": "new1648204005321_0_7716013opt_1"},
        {"qId": "new1648204005321_0_9576676", "qIndex": "5", "optionid": "new1648204005321_0_9576676opt_0"},
        {"qId": "new1648204005321_0_3108431", "qIndex": "6", "optionid": "new1648204005321_0_3108431opt_1"},
        {"qId": "new1648204005321_0_9125013", "qIndex": "7", "optionid": "new1648204005321_0_9125013opt_1"},
        {"qId": "new1648204005321_0_3267401", "qIndex": "8", "optionid": "new1648204005321_0_3267401opt_2"},
        {"qId": "new1648204005321_0_6080685", "qIndex": "9", "optionid": "new1648204005321_0_6080685opt_1"},
        {"qId": "new1648204005321_0_5348817", "qIndex": "10", "optionid": "new1648204005321_0_5348817opt_3"},
        {"qId": "new1648204005321_0_9164677", "qIndex": "11", "optionid": "new1648204005321_0_9164677opt_2"},
        {"qId": "new1648204005321_0_4574221", "qIndex": "12", "optionid": "new1648204005321_0_4574221opt_2"},
        {"qId": "new1648204005321_0_3743964", "qIndex": "13", "optionid": "new1648204005321_0_3743964opt_3"},
        {"qId": "new1648204005321_0_6604040", "qIndex": "14", "optionid": "new1648204005321_0_6604040opt_1"}]}
    e = session.post(url='https://salad.academy/api//score/certificate/623d285ab937597726670f0e', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)

    data = {"answers": [{"blockId": "survey1648400250511_276", "answer": {"value": 5}},
                        {"blockId": "survey1648400250511_283", "answer": {"value": "good"}},
                        {"blockId": "survey1648400250511_285", "answer": {"value": "well"}}],
            "sendAnonymousSubmissionsToEmailLeadsOverride": "false", "status": "submitted"}
    e = session.post(url='https://salad.academy/api/assessment/submission/62509b21aeb5af21f25343ce', data=data_to_new_data(data),
                     headers=headers, timeout=timeout, proxies=proxies)
    print('step10', end='|',flush=True)

    return True

def success(mail):
    success_dir = Path('see_success')
    success_dir.mkdir(exist_ok=True)
    with open(success_dir / f"{mail}.txt", 'w', encoding='utf8') as f:
        f.write(f"{mail}")

def fail(mail):
    faild_accouns_txt = 'see_failed.txt'
    with open(faild_accouns_txt, 'a', encoding='utf8') as f:
        f.write(f"{mail}\n")
def see_account_done(start,end):
    done = 0
    for i in range(start, end + 1):
        mail = f'{i}@cgy188.com'
        success_dir = Path('see_success')

        if os.path.exists(success_dir / f"{mail}.txt"):
            print(f'{mail}账号已观看完成')
            done+=1
    print('还需要观看账号：', end + 1 - start - done, ' 个')
    if done == end+1-start:
        return True
    else:
        return False
if __name__ == '__main__':
    # mail = '859905874@qq.com'
    # proxies = None
    # see_videos(mail)
    # python see.py 1 5
    # 看视频 1@cgy188.com 到5@cgy188.com的账号
    start = sys.argv[1]
    end = sys.argv[2]
    start = int(start)
    end = int(end)
    success_dir = Path('see_success')
    # post = '@cgy188.com'
    while not see_account_done(start,end):
        for i in range(start, end + 1):
            mail = f'{i}@cgy188.com'

            if os.path.exists(success_dir / f"{mail}.txt"):
                print(f'{mail}账号已观看完成')
                continue
            try:
                proxies = get_proxies_with_retry()
                start = time.time()
                r = see_videos(mail,proxies=proxies)
                if r:
                    print(f'{mail} see success {time.time()-start:.2f}s')
                    success(mail)
                else:
                    fail(mail)
            except Exception as e:
                print(f'mail:{mail},error:{e}')
                traceback.print_exc()
                fail(mail)
