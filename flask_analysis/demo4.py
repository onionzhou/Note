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
app.secret_key='dddddd'

USERS ={
    1:{"name":"onion1","age":18},
    2:{"name":"onion2","age":19},
    3:{"name":"onion3","age":12}
}


'''
@app.before_request
def process_request():
    if request.path == '/login':
        return None
    user =session.get('user_info')
    if user:
        return None
    return redirect('./login')
'''
@app.before_first_request
def process_first_request():
    pass

@app.before_request
def process_request1(*args,**kwargs):
    print(" process_request1 请求之前")
    #return 'cut off'

@app.before_request
def process_request2(*args,**kwargs):
    print("process_request2 请求之前")

@app.after_request
def process_response1(response):
    print(' process_response1 请求之后')
    return response

@app.after_request
def process_response2(response):
    print('process_response2 请求之后')
    return response

@app.errorhandler(404)
def error_404(code):
    return '404'

#sesion 装饰器
def seesion_wraps(func):
    functools.wraps(func)
    def inner(*args,**kwargs):
        user = session.get('user_info')
        if not user:
            return redirect('login')
        return func(*args,**kwargs)
    return inner


@app.route("/",methods=['GET'])
@app.route("/index",methods=['GET'])
# @seesion_wraps
def index():
    print('index function')
    return render_template('index.html',user_dict=USERS)

@app.route("/detail/<int:id>",methods=['GET'])
# @seesion_wraps
def detail(id):

    info = USERS.get(id)
    return render_template('detail.html',info=info)


@app.route("/login",methods=['GET','POST'],endpoint='x')
def login():
    if request.method =="GET":
        return render_template('login.html')
    else:
        user =request.form.get('user')
        passwd =request.form.get('passwd')
        if user == "onion" and passwd == "123":
            session['user_info']=user
            return redirect('./index')

        return render_template('login.html',msg="用户名密码错误")

'''
@app.before_request  请求之前执行， 可用用做权限认证等等
@app.after_request  请求之后执行
@app.before_first_request  第一次请求执行的参数， 用于第一请求连接数据库
@app.errorhandler(404) 错误码处理

多个组合
before_request   顺序执行
after_request   倒序执行

如果一个请求在before_request 中拦截了，after_request 仍然全部执行



'''


if __name__ == '__main__':
    app.run(debug=True)