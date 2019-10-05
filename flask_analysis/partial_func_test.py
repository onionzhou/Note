#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 2:37 PM
# @Author  : onion
# @Site    : 
# @File    : partial_func_test.py
# @Software: PyCharm

import functools


def func(a,b):
    print(a,b)

# 偏函数
# 生成一个新的函数，完成了第一个参数的传递
if __name__ == '__main__':
    new_func = functools.partial(func,44)
    new_func(88)