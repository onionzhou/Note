#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/8 20:05
# software: PyCharm

# threading.Semaphore test
import threading
import  time
MAX_CONNECT = 3 #每次最多执行3个线程
lock_sem = threading.Semaphore(value=MAX_CONNECT)

def print_hello(args):
    lock_sem.acquire()
    print("Hello world {}".format(args))
    time.sleep(3)
    lock_sem.release()

def main():
    thread_list = []
    for i in range(10):
        t =threading.Thread(target=print_hello,args=(i,))
        thread_list.append(t)

    for t in thread_list:
        t.start()
    print("main thread end !!")

if __name__ == '__main__':
    main()