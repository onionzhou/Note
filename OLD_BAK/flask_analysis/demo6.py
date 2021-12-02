#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 8:02 AM
# @Author  : onion
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

from demo6_views import app


'''
蓝图对象名 和函数名不能同名
eg：错误示范
blue_1 = Blueprint('blueblue_1',__name__)
@blue_1.route('/blue1')
def blue_1():
    return "hello blue_1"
--------------------------------------
blue_1 = Blueprint('blueblue_1',__name__)
app.register_blueprint(blue_1) 蓝图注册

-----------------------------------
每个蓝图可以
设置自己的模板和静态文件  blue_1.py
有自己的请求相关的 <before request  等操作>
批量的url

蓝图：
    每个蓝图的

'''

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)