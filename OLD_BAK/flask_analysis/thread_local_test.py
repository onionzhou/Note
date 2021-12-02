#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm



import threading
import time

'''
threadlocal

'''
#threading.local() 用于每个线程来开辟一个空间来保存他独有的值
local_value =threading.local()
# class Foo(object):
#     def __init__(self):
#         self.name = 0
# local_value=Foo()

def run_func(num):
    local_value.name = num

    time.sleep(1)
    print(local_value.name,threading.current_thread().name)

def main():
    for i in range(10):
        threading.Thread(target=run_func,args=(i,)).start()

'''
上下文管理

单进程单线程    --->全局变量实现
单进程多线程    ---> threading.local 对象
单进程单线程（多个协程）<io请求> ---> 自定义一个类似 threading.local对象 并支持协程

多个线程共享 进程资源
多个协程共享 线程资源
'''
#实现一个类似于threading.local 功能
#

from  _thread import get_ident #线程的唯一标识

class Local(object):
    def __init__(self):
        self.storage={}
        self.get_ident=get_ident

    def set_value(self,k,v):

        ident =self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            origin={k:v}
        else:
            origin[k] = v

        self.storage[ident] = origin

    def get_value(self,k):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            return None
        return origin.get(k)

local_value_test = Local()

def task_local(num):
    local_value_test.set_value('name',num)

    time.sleep(1)
    print(local_value_test.get_value('name'),threading.current_thread().name)


def task(args):
    #获取线程唯一标识
    print(get_ident())

def exce_test():
    for i in range(10):
        threading.Thread(target=task_local,args=(i,)).start()



if __name__ == '__main__':
    exce_test()