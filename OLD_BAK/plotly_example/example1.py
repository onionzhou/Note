#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/24 15:32
#  @Author  : onion
#  @Site    :
#  @File    : example1.py
#  @Software: PyCharm
import pandas as pd
import plotly.graph_objects as go

'''
In [3]: data.head()
Out[3]:
      DATE  Auckland  Christchurch Dunedin Hamilton  Wellington
0  2000-01     115.4          47.2   174.8     96.2        91.8
1  2000-02       8.4          25.2      41      8.2        35.2
2  2000-03      57.2          60.8    74.2     33.8        53.4
3  2000-04     106.8          58.2      50    129.6       109.8
4  2000-05     128.2          62.0      '-     98.2        78.2

'''


# 曲线图
def line_graph():
    data = pd.read_csv('data/nz_weather.csv')
    # data.head()
    line1 = go.Scatter(x=data['DATE'], y=data['Auckland'], name='Auckland')
    line2 = go.Scatter(x=data['DATE'], y=data['Wellington'], name='Wellington')
    fig = go.Figure([line1, line2])
    fig.update_layout(
        title='新西兰的天气',
        xaxis_title='date',
        yaxis_title='weather'
    )
    fig.show()


'''
In [11]: data[(data['DATE']>='2010-01') & (data['DATE'] <'2011-01')]
Out[11]:
        DATE  Auckland  Christchurch Dunedin Hamilton  Wellington
120  2010-01      44.0          32.6      69    191.6        72.8
121  2010-02       4.6          18.2    36.6     24.4        16.8
122  2010-03       7.6          22.4    22.6     20.2        34.2
123  2010-04      56.0          24.0    50.4     36.6        27.2
124  2010-05     162.8         163.8   159.8    120.4       171.4
125  2010-06     160.8          93.1    63.6    222.6       140.3
126  2010-07      87.0          67.6    26.6     65.8        92.4
127  2010-08     187.4          86.4    68.2    196.1       165.8
128  2010-09     112.0          42.0      51    180.8       151.6
129  2010-10      19.8          22.0    27.6     41.2        71.8
130  2010-11      22.3          53.0    32.8       16        21.4
131  2010-12      94.4          35.2   119.8    120.2        91.0
'''


# 条形图
def bar_graph():
    data = pd.read_csv('data/nz_weather.csv')
    data_2010 = data[(data['DATE'] >= '2010-01') & (data['DATE'] < '2011-01')]
    bar1 = go.Bar(x=data_2010['DATE'], y=data_2010['Auckland'],
                  text=data_2010['Auckland'], textposition='outside')

    bar2 = go.Bar(x=data_2010['DATE'], y=data_2010['Wellington'],
                  text=data_2010['Wellington'], textposition='inside')

    fig = go.Figure([bar1, bar2])
    fig.show()


# 区间范围
def histogram_graph():
    data = pd.read_csv('data/nz_weather.csv')
    # his =go.Histogram(x=data['Auckland'])
    his = go.Histogram(x=data['Auckland'], xbins={'size': 10})
    fig = go.Figure(his)
    fig.update_layout(bargap=0.1)
    fig.show()


if __name__ == '__main__':
    bar_graph()

    # histogram_graph()
