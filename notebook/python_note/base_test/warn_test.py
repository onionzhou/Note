#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/26 16:44
# software: PyCharm
import warnings


# warnings 库测试

def example(warn=False):
    if warn:
        warnings.warn('warning test ......')
    print("dddd")


#  命令行 使用
# python3 -W all example.py
# python3 -W error example.py
# python3 -W ignore example.py

if __name__ == '__main__':
    example(True)
