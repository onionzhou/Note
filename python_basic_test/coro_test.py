#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/8/18 16:18
# software: PyCharm
#协程测试
"""
>>> coro_avg = averager()  # <1>
    >>> next(coro_avg)  #预激活协程
    >>> coro_avg.send(10)  # <3>
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
"""


def averager1():
    total = 0.0
    count = 0
    average = None
    while True:  # <1>
        term = yield average  # <2>
        total += term
        count += 1
        average = total/count

def coro_avg1():
    coro_avg=averager1()
    next(coro_avg)
    coro_avg.send(1)
    coro_avg.send(2)
#====================================
from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)  # 预激协程
        return gen
    return primer

# BEGIN DECORATED_AVERAGER
"""
A coroutine to compute a running average
    >>> coro_avg = averager()  # <1>
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)  # <2>
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)  # <3>
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
"""

@coroutine  # <5>
def averager():  # <6>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
# END DECORATED_AVERAGER


if __name__ == '__main__':
    coro_avg1()