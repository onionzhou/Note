#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:onion
# datetime:2019/4/9 20:40
# software: PyCharm

import threading
import  time
event = threading.Event()
class Producer(threading.Thread):
    def run(self):
        print("包子熟了")
        event.set() #true
        time.sleep(5)
        print("油条熟了")
        event.set() # true
class Customer(threading.Thread):
    def run(self):
        event.wait()
        print("{} 吃包子".format(self.name))
        time.sleep(1)
        event.clear() #false
        event.wait()
        print("{} 吃油条".format(self.name))
def main():
    thread_list = []
    for _ in range(5):
        thread_list.append(Customer())
    thread_list.append(Producer())

    for t in thread_list:
        t.start()
if __name__ == '__main__':
    main()
