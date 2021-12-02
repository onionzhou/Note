#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 6.py
@time: 2021/3/15 15:51
"""
import threading
import asyncio


import asyncio
import time
from functools import partial
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"

def callback(future): #这里默认传入一个future对象
    print("send email to bobby")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.imooc.com"))
    task.add_done_callback(callback)
    loop.run_until_complete(task)
    print(task.result())


