#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 12:19
# @Author  : onion
# @Site    : 
# @File    : example3.py
# @Software: PyCharm

#3d 图的画法  xyz
import pandas as pd
import plotly.graph_objects as go

'''
data.head()
<bound method NDFrame.head of               x          y          z  color
0    100.000000   0.613222   0.734706      0
1     99.238875   0.589852   0.781320      0
2     99.559608   0.599743   0.762566      0
3     97.931425   0.549296   0.859966      0
4     96.837832   0.515613   0.927150      0
5     98.545804   0.568832   0.826330      0
'''
def test():
    data = pd.read_csv('data/3d-line1.csv')
    #mode='markers' 只要点不要线
    # lines  只要线不要点
    line = go.Scatter3d(x=data['x'],y=data['y'],z=data['z'],mode='markers',marker={'size':3})
    fig = go.Figure(line)
    fig.show()

import plotly.express as pe
#功能同test
def test1():
    data = pd.read_csv('data/3d-line1.csv')
    fig = pe.scatter_3d(data,x='x',y='y',z='z',color='color')
    fig.show()