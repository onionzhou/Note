#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 2:38 AM
# @Author  : onion
# @Site    : 
# @File    : blue_1.py
# @Software: PyCharm

from flask import Blueprint

blueblue_3 = Blueprint('blueblue_3', __name__)


@blueblue_3.route('/blue3')
def blue_3():
    return "hello blue_3"