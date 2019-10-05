#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask


app1 = Flask("app1")
app2 = Flask("app2")

@app1.route("/")
def index():
    return 'hello app1 '

@app2.route("/index2")
def index():
    return "hello app2"




if __name__ == '__main__':
    app.run(debug=True)