#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 12:30
# @Author  : onion
# @Site    : 
# @File    : wrap_test.py
# @Software: PyCharm
def wrapClass(cls):
    def inner(a):
        print('class name:', cls.__name__)
        return cls(a)
    return inner


@wrapClass
class Foo():
    def __init__(self, a):
        self.a = a

    def fun(self):
        print('self.a =', self.a)


m = Foo('xiemanR')
m.fun()