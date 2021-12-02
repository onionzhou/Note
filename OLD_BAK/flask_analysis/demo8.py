#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask
from connect_pool import SqlHelper

app = Flask(__name__)
@app.route("/")
def index():
    ret =SqlHelper.fetch_one('select * from  comment',[])
    print(ret)
    return 'hello onion '


if __name__ == '__main__':
    app.run(debug=True)