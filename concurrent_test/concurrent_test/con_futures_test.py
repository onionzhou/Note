#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/10 20:11
# software: PyCharm

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import threading
import time
import os
"""
计算密集型 可使用多进程
"""

def thread_task(n):
    print("{} task running {}".format(threading.current_thread().name,n))
    #time.sleep(2)
def process_task(n):
    print("{} task running {}".format(os.getpid(), n))
    time.sleep(2)

def thread_pool_test():
    t = ThreadPoolExecutor() #默认cpu * 5
    for i in range(1000):
        t.submit(thread_task,i)
    t.shutdown()
    print("main thread func end")

def process_pool_test():

    result_list = []
    p = ProcessPoolExecutor()
    for i in range(100):
        obj =p.submit(process_task, i)
        result_list.append(obj)
    p.shutdown()  #类似于thread join 方法

    # print([i.result() for i in result_list])
    print("main process func end")
#with 写法  省略shutdown()
def process_pool_test2():
    with ProcessPoolExecutor() as p :
        # p_task = [p.submit(process_task,i) for i in range(100)]
        p_task = [p.map(process_task, range(10)) ]   #map 方法使用
    print("main process end ")

if __name__ == '__main__':
    start = time.time()
    # thread_pool_test()
    # process_pool_test()
    process_pool_test2()
    print(time.time() -start)