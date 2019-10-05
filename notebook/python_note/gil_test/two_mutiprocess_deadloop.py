#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 10:42 PM
# @Author  : onion
# @Site    : 
# @File    : two_mutiprocess_deadloop.py
# @Software: PyCharm

import multiprocessing

def test():
    while True:
        pass
#子进程
multiprocessing.Process(target=test).start()

#主进程
while True:
    pass