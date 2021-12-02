#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 10:36 PM
# @Author  : onion
# @Site    : 
# @File    : two_thread_deadloop.py
# @Software: PyCharm
import threading


def test():
    while True:
        pass

#子线程
threading.Thread(target=test).start()
#主线程
while True:
    pass
