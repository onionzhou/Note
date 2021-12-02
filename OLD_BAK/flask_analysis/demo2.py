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
@seesion_wraps
def index():
    #换成装饰器
    #user = session.get('user_info')
    #print(user)
    #if not user:
    #    return redirect('login')

    return render_template('index.html',user_dict=USERS)

@app.route("/detail/<int:id>",methods=['GET'])
def detail(id):

    user =session.get('user_info')
    if not user:
        return  redirect('login')

    info = USERS.get(id)
    return render_template('detail.html',info=info)


@app.route("/login",methods=['GET','POST'],endpoint='x')
def login():
    if request.method =="GET":
        return render_template('login.html')
    else:
        # request.query_string
        user =request.form.get('user')
        passwd =request.form.get('passwd')
        if user == "onion" and passwd == "123":
            session['user_info']=user
            return redirect('index')

        return render_template('login.html',msg="用户名密码错误")

'''

session 对象,它允许你在不同请求间存储特定用户的信息。
是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名要使用会话，你需要设置一个密钥。

app.secret_key='dddddd'

设置:session['username'] ＝ 'xxx'

删除:session.pop('username', None)

'''


if __name__ == '__main__':
    app.run(debug=True)