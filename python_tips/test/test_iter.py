#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/11/26 11:25
# software: PyCharm

# import python_tips.iter_gen as it
from python_tips.iter_gen import *


# 问题1
def test_iter_reversed_function():
    a = [1, 2, 3, 4, 5]
    example1.list_reversed(a)


def test_iter_reversed_class():
    n = example1.Numrevesed(5)
    for i in n:
        print(i)
    print("*" * 30)
    for i in reversed(n):
        print(i)


# 问题2
import itertools


def test_iter_lice():
    n = example1.my_count(0)
    # print(n[20:30]) #TypeError: 'generator' object is not subscriptable
    for i in itertools.islice(n, 20, 30):
        print(i)  # 20 21 ... 29


# 问题3
def test_dropwhile():

    # with open('test_data/nginx.conf.default') as f :
    #     for line in f :
    #         print(line)

    #startwith 只能处理文本开头为'#'的行数

    # with open('test_data/nginx.conf.default') as f:
    #     for line in itertools.dropwhile(lambda line: line.startswith('#'), f):
    #         print(line, end='')

    with open('test_data/nginx.conf.default') as f:
        lines = (line for line in f if not line.startswith('#'))
        for line in lines:
            print(line)




if __name__ == '__main__':
    # test_iter_reversed_class()
    # test_iter_lice()
    test_dropwhile()
