#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask,render_template,request,redirect,session,flash,get_flashed_messages
import functools
app= Flask(__name__)
app.secret_key='dddddd'

#访问url
#http://127.0.0.1:5000/?v=onion
@app.route("/",methods=['GET'])
def index():
    value =request.args.get('v')
    if value == "onion":
        return "right "

    # flash("超时错误")
    flash('time out',category='B')

    return redirect('./error') #重新发起了一次请求

@app.route('/error')
def error():
    #value = request.query_string.get('msg')
    # data= get_flashed_messages()
    data= get_flashed_messages(category_filter=['B'])
    if data :
        msg =data[0]
    else:
        msg ='......'

    return  'error info {}'.format(msg)


'''
flash  阅后即焚
flash('time out',category='B')   #设置闪现信息，category 分类
get_flashed_messages(category_filter='B') #获取闪现信息

flash 实现通过session 封装的，不用担心数据错乱问题，session 根据用户隔离开了
一般应用于:对临时数据操作， 如错误信息的显示

'''


if __name__ == '__main__':
    app.run(debug=True)