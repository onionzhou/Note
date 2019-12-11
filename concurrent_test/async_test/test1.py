#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/11 14:32
# software: PyCharm
import requests
import pytest
import aiohttp
import asyncio
import time
base_url = 'http://148.70.174.22:8001'

#request  用于同步请求
#aiohttp  用于异步请求

# 花费时间装饰器
def spend_time(func):
    def inner(*args):
        t1 = time.time()
        func(*args)
        print('耗时{}'.format(time.time() - t1))

    return inner


# 同步请求
def sync_get_request():
    return requests.get(base_url + '/ip').status_code


@spend_time
def test2():
    # 11.856250047683716
    for i in range(20):
        r = sync_get_request()
        print(r)


def test_2000_request():
    for i in range(2000):
        http_code = sync_get_request()
        assert http_code == 200
    # 4 passed in 155.94s (0:02:35)


# =========================================
# 假异步，因为request
async def get_request():
    return requests.get(base_url + '/ip').status_code


async def main():
    r = await get_request()
    print(r)


def test1():
    # 9.493656158447266
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(20):
        task = asyncio.ensure_future(main())
        tasks.append(task)
    print(tasks)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


# =========================================
# 异步请求示例
async def hello():
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + '/ip') as resp:
            print(resp.status)
            print(await resp.text())


@spend_time
def test3():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()


# ======================
sem = asyncio.Semaphore(50)


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with sem:  # 信号量用于限制并发数
            async with session.get(base_url + '/ip') as resp:
                return resp.status


async def run(num):
    # num =20 耗时2.270932674407959
    tasks = []
    for i in range(num):
        task = asyncio.ensure_future(fetch())
        tasks.append(task)
    resp = await  asyncio.gather(*tasks)
    return resp


@spend_time
def test4(num):
    loop = asyncio.get_event_loop()
    # future = asyncio.ensure_future(run(num))
    future = asyncio.ensure_future(run(num))
    r = loop.run_until_complete(future)
    print(r)
    loop.close()


async def run1(num):
    # num =20 耗时2.270932674407959
    tasks = []
    for i in range(num):
        task = asyncio.ensure_future(fetch())
        tasks.append(task)
    return tasks


@spend_time
def test6(num):
    loop = asyncio.get_event_loop()
    r = loop.run_until_complete(run(num))
    print(r)


# ===========================


if __name__ == '__main__':
    test4(2000)
