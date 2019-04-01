#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/3/31 11:11
# software: PyCharm
import threading
import time


def action(args):
    time.sleep(1)
    print("sub thread running, current thread name is {0}".format(
        threading.current_thread().getName()
    ))
    print("args is {}".format(args + 1))
    time.sleep(1)


def join_test():
    thread_list = [None] * 4
    for i in range(4):
        t = threading.Thread(target=action, args=(i,))
        # t.setDaemon(True)
        # t.start()
        thread_list[i] = t
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

    print("join main thread end")


def no_join_test():
    thread_list = [None] * 4
    for i in range(4):
        t = threading.Thread(target=action, args=(i,))
        # t.setDaemon(True)
        thread_list[i] = t

    for t in thread_list:
        t.start()
    # for t in thread_list:
    #     t.join()
    print("no join main thread end ")


def mul_to_single_thread():
    for i in range(4):
        t = threading.Thread(target=action, args=(i,))
        # t.setDaemon(True)
        t.start()
        t.join()
    print("mul-->single ,main thread end ")

def test_list():
    members = [None] * 100000000
    for i in range(100000000):
        members[i] = i
        # members.append(i)


def test_list_1():
    # 直接报内存错误
    member = []
    for i in range(100000000):
        member.append(i)


if __name__ == "__main__":
    t1 = time.time()
    # join_test()
    # no_join_test()
    mul_to_single_thread()
    print(time.time() - t1)
