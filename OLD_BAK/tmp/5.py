#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 5.py
@time: 2020/12/3 17:57
"""


def what(*args):

    for i  in args:
        print(i)
    print(args[0],args[1])
    print(type(args))
    args=args[:-1]
    print(args)


if __name__ == '__main__':
    what(1,2,3,4,5)