#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 2:38 AM
# @Author  : onion
# @Site    : 
# @File    : blue_1.py
# @Software: PyCharm

from flask import Blueprint

blueblue_2 = Blueprint('blueblue_2',__name__)


@blueblue_2.route('/blue2')
def blue_1():
    return "hello blue_2"