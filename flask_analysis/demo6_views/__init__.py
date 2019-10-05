#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 2:35 AM
# @Author  : onion
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import  Flask

app =Flask(__name__)


from .views.blue_1 import blueblue_1 as b1
from .views.blue_2 import blueblue_2 as b2
from .views.blue_3 import blueblue_3 as b3

app.register_blueprint(b1)
app.register_blueprint(b2)
app.register_blueprint(b3)