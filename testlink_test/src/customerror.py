#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/12/17 10:21
# software: PyCharm

class AutotestError(Exception):
    pass

class AtArgError(AutotestError):
    def __init__(self,msg):
        self.msg =msg
    def __str__(self):
        return 'this is{}'.format(self.msg)