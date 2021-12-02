#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/9 21:06
# software: PyCharm
import threading
import queue, time
from random import randint

q = queue.Queue(10)


class Producer(threading.Thread):
    def run(self):
        while True:
            r = randint(0,5)
            print("包子熟了 {} 个".format(r))
            q.put(r)
            time.sleep(1)

class Customer(threading.Thread):
    def run(self):
        while True:
            eat =q.get()
            print("吃包子 {}".format(eat))

def main():
    thread_list = []
    for _ in range(5):
        thread_list.append(Producer())
    thread_list.append(Customer())
    for t in thread_list:
        t.start()

if __name__ == '__main__':
    main()