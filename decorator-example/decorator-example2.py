#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: decorator-example1.py
@time: 2022/3/29 10:14
"""

from functools import wraps

# 类装饰器,__init__  传函数本体， __call__ 执行函数装饰
'''

用类作为装饰器装饰函数来对函数添加一些额外的属性或功能时，
一般会在类的__init__()方法中记录传入的函数，
再在__call__()调用修饰的函数及其它额外处理

'''


class entryExit(object):
    def __init__(self, f):
        self.f = f
        print(self.f)
        f()  # 证明函数定义已完成

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)


@entryExit
def func1():
    print("inside func1()")


@entryExit
def func2():
    print("inside func2()")


if __name__ == '__main__':
    func1()
    func2()
