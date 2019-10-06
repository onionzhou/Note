#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2019/10/6 23:35
#  @Author  : onion
#  @Site    :
#  @File    : serpins.py
#  @Software: PyCharm


'''
谢尔平斯基三角形
'''
from turtle import *


def draw_triangle(points, color, myturle):
    myturle.fillcolor(color)
    myturle.up()
    myturle.goto(points[0])
    myturle.down()
    myturle.begin_fill()
    myturle.goto(points[1])
    myturle.goto(points[2])
    myturle.goto(points[0])
    myturle.end_fill()


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpins(points,degree,myturle):
    colormap = ['blue','red','green','white','yellow','orange','violet']
    draw_triangle(points,colormap[degree],myturle)

    if degree > 0:
        sierpins([points[0],
                  get_mid(points[0],points[1]),
                  get_mid(points[0],points[2])],
                 degree-1,myturle)

        sierpins([points[1],
                  get_mid(points[0], points[1]),
                  get_mid(points[1], points[2])],
                 degree - 1, myturle)

        sierpins([points[2],
                  get_mid(points[2], points[1]),
                  get_mid(points[0], points[2])],
                 degree - 1, myturle)

if __name__ == '__main__':
    myturle= Turtle()
    mywin = myturle.getscreen()
    mypoint=[(-500,-250),(0,500),(500,-250)]
    sierpins(mypoint,5,myturle)
    mywin.exitonclick()