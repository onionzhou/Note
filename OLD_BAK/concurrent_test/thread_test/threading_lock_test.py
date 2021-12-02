#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/1 9:24
# software: PyCharm

import threading
import time

GL_NUM = 0
# lock =threading.RLock()
lock =threading.Lock()
rlock = threading.RLock()
locka = threading.Lock()
lockb = threading.Lock()

def change_num(num):
    global GL_NUM
    time.sleep(0.1)
    GL_NUM += num
    print(GL_NUM)
def change_num_lock(num):
    lock.acquire()
    global GL_NUM
    time.sleep(0.1)
    GL_NUM += num
    print(GL_NUM)
    lock.release()

def test_no_lock():
    for i in range(6):
        threading.Thread(target=change_num,args=(i,)).start()
    print("main thread end ")
def test_lock():
    for i in range(6):
        threading.Thread(target=change_num_lock,args=(i,)).start()
    print("main thread end")

#一个死锁的例子，两个线程死锁
class dead_lock(threading.Thread):
    def run_a(self):
        locka.acquire()
        print("get locka time {}".format(time.ctime()))
        time.sleep(3)
        lockb.acquire()
        print("get lockb time {}".format(time.ctime()))
        lockb.release()
        locka.release()
    def run_b(self):
        lockb.acquire()
        print("get lockb time {}".format(time.ctime()))
        time.sleep(2)
        locka.acquire()
        print("get locka time {}".format(time.ctime()))
        locka.release()
        lockb.release()
    def run(self):
        self.run_a()
        self.run_b()
def test_dead_lock():
    for i in range(10):
        dead_lock().start()

''' function  run_rlock_a  run_lock_a
用来测试 Lock  和 RLock 的区别，针对于同一个线程的情况
run_lock_a    死锁
run_rlock_a   未出现死锁
'''
def run_rlock_a():
    rlock.acquire()
    print("get rlock a {}".format(time.ctime()))
    rlock.acquire()
    print("get rlcok a again {}".format(time.ctime()))
    rlock.release()
    rlock.release()
    print("run_rlock_a end")
def run_lock_a():
    lock.acquire()
    print("get lock a {}".format(time.ctime()))
    time.sleep(1)
    lock.acquire()
    print("get lcok a again {}".format(time.ctime()))
    lock.release()
    lock.release()
    print("run_lock_a end ")
def test_lock_dead():
    threading.Thread(target=run_lock_a).start()
def test_rlock_dead():
    threading.Thread(target=run_rlock_a).start()

if __name__ == "__main__":
    t1 =time.time()
    # test_lock()
    # test_no_lock()
    #test_dead_lock()
    test_rlock_dead()
    # test_lock_dead()
    print(time.time() -t1)