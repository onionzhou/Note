#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time

'''线程创建的两种方法
    1.把方法作为参数传给thread构造方法
'''
def test(arg):
    time.sleep(1)
    print("test thread {}".format(arg))
def create_function_thread():
    for i in range(10):
        t =threading.Thread(target=test,args=(i,))
        t.start()

    print("main thread end!!")

'''2.继承thread 重写 run方法
'''
class MyThread(threading.Thread):
    def __init__(self,arg):
        threading.Thread.__init__(self)
        # super(MyThread,self).__init__()
        self.arg =arg
    def test(self):
        print('test')
    def run(self):
        time.sleep(1)

        print("test thread {}".format(self.arg))
def create_class_thread():
    for i  in range(10):
        t=MyThread(i)
        t.start()
    print("main thread end")

if __name__ =="__main__":
    create_class_thread()
