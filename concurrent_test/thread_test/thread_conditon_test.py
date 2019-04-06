#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/4 19:43
# software: PyCharm

import threading
import time
from random import randint

lock = threading.Condition(threading.Lock())
lock_R = threading.Condition(threading.RLock())
product = []


class Producer(threading.Thread):
    def run(self):
        global product
        while 1:
            if lock.acquire():
                if len(product) < 10:
                    val = randint(0, 100)
                    # print("生产者 {} append {}".format(self.name, val))
                    product.append(val)
                    print("生产者 {} product [{}] list--> {}".format(self.name, val, product))
                    lock.notify()  # 不会释放锁
                    # lock.release()
                else:
                    print("product is full {}--{}".format(len(product), product))
                    lock.wait()
                    lock.notify()
                    # lock.release()
            lock.release()
            time.sleep(3)


class Customer(threading.Thread):
    def run(self):
        global product
        while True:
            if lock.acquire():
                if len(product) > 0:
                    # lock.acquire()
                    # print("消费者 {} del {}".format(self.name, product[0]))
                    print("消费者 {} del {} ".format(
                        self.name,product[0] ),end=" ")
                    del product[0]
                    print("list-->{}".format(product))
                    lock.notify()
                    # lock.release()
                else:
                    print("product is null ... {}".format(product))
                    lock.wait()
                    # lock.release()
            lock.release()
            time.sleep(1)


def main():
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Customer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
