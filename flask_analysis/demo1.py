#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from flask import  Flask,views

app= Flask(__name__)

#路由通过装饰器实现的但
#添加路由的本质 ----->执行 add_url_rule()方法
'''
源码
 def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
------------------------

1.decorator = app.route("/",methods=['GET','POST'],endpoint='x')
 def route(self, rule, **options):
        #route = /
        #options = {methods=['GET','POST'],endpoint='x'}
        #self ---> app 对象
        def decorator(f):  #f -->index 函数
            #弹出endpoint 如果有，没有为None
            endpoint = options.pop('endpoint', None)
            #执行了此函数，添加路由和视图的对象关系
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

2.@decorator
    decorator(index)
路由通过装饰器实现的但
添加路由的本质 ----->执行 add_url_rule()方法
'''

#endpoint别名，不写 默认是函数名
'''
def add_url_rule(self, rule, endpoint=None, view_func=None,
                     provide_automatic_options=None, **options):
    if endpoint is None:
        endpoint = _endpoint_from_view_func(view_func)

def _endpoint_from_view_func(view_func):
    assert view_func is not None, 'expected view func if endpoint ' \
                                  'is not provided.'
    return view_func.__name__ --->返回传入函数的函数名
'''



#endpoint别名，不写 默认是函数名
@app.route("/",methods=['GET','POST'],endpoint='x')
def index():
    return 'hello world'
#通过add_url_rule  添加路由
def index1():
    return 'hello world add url rule'
app.add_url_rule("/index1",'x1',index1,methods=['GET','POST'])

'''
3.CBV
FBV (function base views) 在视图里使用函数处理请求
CBV (class base views)  在视图里使用类处理请求

FBV就是function,
CBV就是class

FBV简单, 小巧, 当不涉及到复杂的逻辑时可以使用FBV

CBV 灵活, 因为, 类的封装, 继承, 多态, 你说灵活不灵活


'''
#flask cbv
#定义一个类
class LoginView(views.MethodView):
    #methods = ['GET', 'POST']
    def get(self):
        return "LoginView get"

    def post(self):
        return "LoginView post"

#添加路由关系，as_view的参数必须传，
app.add_url_rule('/loginview',
                 view_func=LoginView.as_view(name='loginView'),
                 endpoint = None,
                 methods=['GET', 'POST'] )





if __name__ == '__main__':

    app.run(debug=True)
    print(app.url_map)