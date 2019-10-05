#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask,render_template,request,redirect,session
import functools
app= Flask(__name__)





@app.route("/",methods=['GET'])
def index():

    return render_template('index.html')

'''
对象加() ---> 调用器__call__ 方法

app.run --调用--> run_simple(host, port, self, **options)----> app.__call__--->wsgi_app(environ, start_response)


'''

class MiddleWare():

    def __init__(self,wsgi_app):
        self.wsgi_app =wsgi_app
    def __call__(self, environ, start_response):
        print('加点料')
        ret = self.wsgi_app(environ, start_response)
        print('来点酒')
        return ret


if __name__ == '__main__':
    app.wsgi_app=MiddleWare(app.wsgi_app)
    # app.run()