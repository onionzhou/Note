#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: p1.py
@time: 2020/9/1 15:11
"""

import time
from locust import HttpUser, task, between,HttpLocust

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})

class WebsiteTasks(TaskSet):
    def on_start(self):   #进行初始化的工作，每个Locust用户开始做的第一件事
        payload = {
            "username": "test_user",
            "password": "123456",
        }
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        self.client.post("/login",data=payload,headers=header)#self.client属性使用Python request库的所有方法，调用和使用方法和requests完全一致；

    @task(5)    #通过@task()装饰的方法为一个事务，方法的参数用于指定该行为的执行权重，参数越大每次被虚拟用户执行的概率越高，默认为1
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    host     = "https://github.com/" #被测系统的host，在终端中启动locust时没有指定--host参数时才会用到
    task_set = WebsiteTasks          #TaskSet类，该类定义用户任务信息，必填。这里就是:WebsiteTasks类名,因为该类继承TaskSet；
    min_wait = 5000  #每个用户执行两个任务间隔时间的上下限（毫秒）,具体数值在上下限中随机取值，若不指定默认间隔时间固定为1秒
    max_wait = 15000