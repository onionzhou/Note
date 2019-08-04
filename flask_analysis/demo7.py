#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask,request

app = Flask(__name__)
@app.route("/")
def index():
    print(request)
    print(app.__call__)
    return 'hello onion '


if __name__ == '__main__':
    print(app)
    print(app.__call__)
    app.request_class
    request.method
    app.run(debug=True)