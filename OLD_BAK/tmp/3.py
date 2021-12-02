#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: 3.py
@time: 2020/11/18 17:42
"""
import  random
import time
import string
while True:
    print(random.random())
    time.sleep(1)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print (ran_str)
    time.sleep(1)
    print(random.choice(['剪刀', '石头', '布','年轻人,你不讲武德','耗子为汁']))
    time.sleep(1)
