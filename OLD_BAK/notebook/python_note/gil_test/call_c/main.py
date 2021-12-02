#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 10:52 PM
# @Author  : onion
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from ctypes import cdll
from threading import  Thread


lib = cdll.LoadLibrary("./libloop.so")

Thread(target=lib.test).start()

while True:
    pass