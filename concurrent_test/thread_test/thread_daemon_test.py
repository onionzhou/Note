#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/3/31 10:50
# software: PyCharm
import threading
import time
def action(args):
    time.sleep(1)
    print("sub thread running, current thread name is {0}".format(
        threading.current_thread().getName()
    ))
    print("args is {}".format(args))
    time.sleep(1)
def no_daemon_test():
    for i in range(4):
        threading.Thread(target=action,args=(i,)).start()
    print("no daemon main thread end")

def daemon_test():
    for i in range(4):
        threading.Thread(target=action,args=(i,),daemon=True).start()
    print("daemon main thread end")
#以前的写法，功能更daemon_test 一样的
def daemon_old_test():
    for i in range(4):
        t =threading.Thread(target=action,args=(i,))
        t.setDaemon(True) #设置后台进程
        t.start()
    print("daemon main thread end ")
if __name__ == "__main__":
    # no_daemon_test()
    # daemon_test()
    daemon_old_test()