#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/24 16:30
#  @Author  : onion
#  @Site    :
#  @File    : example2.py
#  @Software: PyCharm

import pandas as pd
import plotly.graph_objects as go

#点图的画法

'''

        SepalLength  SepalWidth  PetalLength  PetalWidth         Name
    0          5.1         3.5          1.4         0.2  Iris-setosa
    1          4.9         3.0          1.4         0.2  Iris-setosa
    2          4.7         3.2          1.3         0.2  Iris-setosa
    3          4.6         3.1          1.5         0.2  Iris-setosa
    4          5.0         3.6          1.4         0.2  Iris-setosa
    
    
In [13]: data.groupby('Name').count().index
Out[13]: Index(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype='object', name='Name')

In [14]: color_map = {
    ...:         'Iris-setosa': 0,
    ...:         'Iris-versicolor': 1,
    ...:         'Iris-virginica': 2
    ...:
    ...:     }

In [15]: data.head()
Out[15]:
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa

In [16]: data['color'] =data['Name'].map(color_map)

In [17]: data.head()
Out[17]:
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name  color     
0          5.1         3.5          1.4         0.2  Iris-setosa      0
1          4.9         3.0          1.4         0.2  Iris-setosa      0
2          4.7         3.2          1.3         0.2  Iris-setosa      0
3          4.6         3.1          1.5         0.2  Iris-setosa      0
4          5.0         3.6          1.4         0.2  Iris-setosa      0

In [18]:




'''


def markers_graph():
    color_map = {
        'Iris-setosa': 0,
        'Iris-versicolor': 1,
        'Iris-virginica': 2

    }

    data = pd.read_csv('data/iris.csv')
    data['color'] =data['Name'].map(color_map) #追加一行
    # mode='markers'  只需要坐标点，不需要连线
    # marker={'color':data['Name']} 通过颜色来区分 Name
    points = go.Scatter(x=data['SepalLength'], y=data['SepalWidth'],
                        mode='markers', marker={'color': data['color']})
    fig = go.Figure(points)
    fig.show()

# 功能同 markers_graph，代码量更少
import plotly.express as pe
def plotly_express_test():
    data = pd.read_csv('data/iris.csv')
    fig =pe.scatter(data,x='SepalLength',y='SepalWidth',color='Name')
    fig.show()
#画出所有的组合 笛卡尔积 16种
def all_combination():
    data = pd.read_csv('data/iris.csv')
    fig = pe.scatter_matrix(data,color='Name',
                            dimensions=['SepalLength','SepalWidth',
                                        'PetalLength','PetalWidth'])
    fig.show()


if __name__ == '__main__':
    # markers_graph()
    # plotly_express_test()
    all_combination()
