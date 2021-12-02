#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: p1.py
@time: 2020/9/2 16:19
"""
from locust import HttpUser, task, between, TaskSet
from lxml import etree
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    ctoken = None

    def on_start(self):
        # self.client.post("/login", json={"username":"foo", "password":"bar"})
        # 到登陆页面
        with self.client.get("/", catch_response=True, verify=False) as re:
            htmlElement = etree.HTML(re.text.encode('utf-8'))
            ctoken_list = htmlElement.xpath('//input[@id="ctoken"]/@value')
            self.ctoken = ctoken_list[0]
        # 登陆

        self.client.post('/login/aut')


def main():
    import os
    os.system('locust  -f locustfile.py')


if __name__ == '__main__':
    import requests
    import json

    url = 'https://10.0.80.34/index.php'
    session = requests.session()
    ret = session.get(url, verify=False)

    htmlElement = etree.HTML(ret.text.encode('utf-8'))

    ctoken = htmlElement.xpath('//input[@id="ctoken"]/@value')
    print(ret.text)
    print(ctoken[0])
    print(type(str(ctoken[0])))

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'X-Requested-With': 'XMLHttpRequest',
        'charset':'utf-8',
        'DNT':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    payload = {
        'username': 'admin',
        'pwd': '%241.fKf5wXwzx6mWasr2b0sSYF2G',
        'method': 'pwd',
        'ctoken': str(ctoken[0]),
        "captcha": "undefined",
        "method": "pwd",
        "thirdinfo": "undefined"

    }


    print(payload)
    ret = session.post(url + '/login/auth3', verify=False, data=payload)
    print(ret.text)

    ret =session.get(url+'/dashboard',verify=False)

    # print(ret.text)
