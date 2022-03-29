#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: decorator-example1.py
@time: 2022/3/29 10:14
"""

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def test2(func):
    print('test2')
    return func


def test3(func):
    def inner():
        print('test3')
        return func()

    return inner

@test2
@test3
def hello():
    print('hello world ')

# @decorator1
# @test2
def add(x, y):
    print(x + y)
    return x + y


if __name__ == '__main__':
    print(hello())
    # add(1, 2)
    # say_hello(2)(add(1,2))
