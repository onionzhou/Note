#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/25 14:05
#  @Author  : onion
#  @Site    :
#  @File    : china_gdp.py
#  @Software: PyCharm

import pandas as pd
import plotly.graph_objects as go

'''
全国1999 2018 年 GDP 增长，动态图
'''


#返回每列的数值  1999 2000 ... 2018
def get_per_columns(data):
    data =data.columns[1::]

    for i in data[::-1]:
        yield i

#准备每一帧数据
def construct_frames(data):
    frames=[]
    colors = ['IndianRed', 'SandyBrown', 'MediumVioletRed', 'Gold', 'LightSeaGreen',
              'DeepSkyBlue', 'SlateBlue', 'LightPink', 'BurlyWood', 'MediumSeaGreen',
              'IndianRed', 'SandyBrown', 'MediumVioletRed', 'Gold', 'LightSeaGreen',
              'DeepSkyBlue', 'SlateBlue', 'LightPink', 'BurlyWood', 'MediumSeaGreen',
              'DeepSkyBlue', 'SlateBlue', 'LightPink', 'BurlyWood', 'MediumSeaGreen',
              'DeepSkyBlue', 'SlateBlue', 'LightPink', 'BurlyWood', 'MediumSeaGreen','MediumSeaGreen']

    for index in get_per_columns(data):
        data.sort_values(by=[index], ascending=1, inplace=True)
        data['colors']=colors
        bar = go.Bar(x=data[index], y=data['地区'],orientation= 'h',
                 text=data[index],textposition='inside',marker_color=data['colors'])
        frame = go.Frame(data=bar, layout=go.Layout(title_text='GDP'))
        frames.append(frame)

    return frames

def test(data):
    colors = ['IndianRed', 'SandyBrown', 'MediumVioletRed', 'Gold', 'LightSeaGreen',
              'DeepSkyBlue', 'SlateBlue', 'LightPink', 'BurlyWood', 'MediumSeaGreen']
    data.sort_values(by=[2008],ascending=1,inplace=True)
    bar = go.Bar(x=data[2008],y=data['地区'],orientation= 'h',textposition='outside')
    fig=go.Figure(bar)
    fig.show()

def main():
    data = pd.read_excel('data/GDP20.xls')
    init_num=data.columns[-1]
    data.sort_values(by=[init_num], ascending=1, inplace=True)
    init_bar = go.Bar(x=data[init_num], y=data['地区'], orientation='h', textposition='outside')
    frames =construct_frames(data)

    buttons = {
        "type": "buttons",
        "direction": "right",
        "pad": {"r": 80, "t": 0},
        "buttons": [{"label": "Play", "method": "animate", "args": [
            None,
            dict(frame=dict(duration=600, redraw=True),
                 transition=dict(duration=1800, easing="linear-in-out"),
                 fromcurrent=True,
                 mode='immediate')
        ]}]
    }

    fig = go.Figure(
        data=[init_bar],
        layout=go.Layout(
            title="GDP",
            titlefont={"size": 36},
            font={"family": 'monospace', "size": 15},
            width=2100, height=1000,
            updatemenus=[buttons],
            xaxis=dict(showgrid=True, zeroline=False, automargin=True),
            yaxis=dict(showgrid=True, zeroline=False, automargin=True),
        ),
        frames=frames,
    )

    fig.show()

if __name__ == '__main__':
    main()





