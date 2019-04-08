#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/8 20:24
# software: PyCharm

#thread.Timer test
import time
import  threading
def print_hello():
    print("hello world")
def main():
    t =threading.Timer(10,print_hello)
    t.start() # 10s后，打印hello world
    time.sleep(1)
    #t.cancel()   取消定时线程执行
if __name__ == '__main__':
    main()