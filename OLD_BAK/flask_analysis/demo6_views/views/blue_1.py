#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 2:38 AM
# @Author  : onion
# @Site    : 
# @File    : blue_1.py
# @Software: PyCharm

from flask import  Blueprint

#蓝图名 不要跟下面的函数名一样
# blueblue_1 = Blueprint('blueblue_1',__name__)

#每个蓝图可以设置自己的模板和静态文件
#http://127.0.0.1:5000/b1/blue1
blueblue_1=Blueprint('blue1',__name__,url_prefix="/b1",template_folder="b1",static_folder='sb1')

@blueblue_1.before_request
def process_request():
    print('blue1   before request ')


@blueblue_1.route('/blue1')
def blue_1():

    return "hello blue_1"