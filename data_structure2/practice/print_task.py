#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/6 20:26
#  @Author  : onion
#  @Site    :
#  @File    : print_task.py
#  @Software: PyCharm

'''
在任何给定的一个小时内，实验室里都有约10个学生。
他们在这一个小时内最多打印2次 ，并且打印的页数1到20 不等，
打印机 每分钟 低质量 打印10页， 高质量 5页/mins

每小时 20 个任务， --> 1个任务 180 s
'''
import random
from data_structure2.basic.my_queue import Queue


class Printer(object):
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        '''
        减量计时，执行完任务之后将打印机设置为空闲状态
        :return:
        '''
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining < 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)  # 模拟1-20页

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


def new_print_task():
    '''
    随机数正好为180  证明一个任务创建
    ps: 可能出现多个任务被创建，也可能很长时间没有任务创建
    :return:
    '''
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

'''
1.创建一个打印任务队列，每个任务到来时有一个时间戳
2.针对每一秒（cursecond），执行以下操作
    A.是否创建一个新的打印任务，如果是，以cursecond 作为其时间戳并将该任务加入队列中
    B.如果打印机空闲，并正在等待执行任务
        * 从队列中取出第一个任务并提交给打印机
        * 用cursecond 减去该任务的时间戳，以此计算其等待时间
        * 将该任务的等待时间存入一个列表，
        * 根据任务的页数，计算执行时间
    C. 打印机进行1秒打印，同时从该任务的执行时间中减1s
    D.如果打印任务执行完成，或者任务需要的时间减到0，说明打印机为空闲状态
3.模拟完成后，根据等待时间列表中的值计算平均等待时间
'''
def simulation(numseconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    print_queue = Queue()
    wait_time_list= []
    for cursecond in range(numseconds):
        if new_print_task():
            task = Task(cursecond)
            print_queue.enqueue(task)
        if (not printer.busy()) and \
                (not print_queue.is_empty()):

            nexttask = print_queue.dequeue()
            wait_time_list.append(nexttask.wait_time(cursecond))
            printer.start_next(nexttask)
        printer.tick()

    avetime_wait =sum(wait_time_list) / len(wait_time_list)

    print("average time {:6.2f} .secs, {:3d} tasks  remaing "\
          .format(avetime_wait,print_queue.size()))


if __name__ == '__main__':
    for i in range(10):
        simulation(3600,5)#模拟60分钟(3600s)内打印速度为每分钟5页，进行10次这样的模拟