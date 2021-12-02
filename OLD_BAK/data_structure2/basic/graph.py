#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/9/30 14:33
# software: PyCharm
class Vertex(object):
    '''图的顶点类'''

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        '''添加一个顶点到另一个的连接'''
        self.connectedTo[nbr] = weight

    def get_connections(self):
        '''返回邻接表的所有顶点'''
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo.get(nbr)

    def __str__(self):
        return str(self.id) + 'connectedTo: ' + \
               str([x.id for x in self.connectedTo])


class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        '''添加一个顶点实例'''
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self,k):
        '''在图中找到名为k的顶点'''
        if k in self.vertList:
            return self.vertList[k]
        else:
            return None

    def add_edge(self, f, t, w=0):
        '''添加一条有向边，连接顶点f 和 条，w为权重'''
        if not f in self.vertList:
            self.add_vertex(f)
        if not t in self.vertList:
            self.add_vertex(t)
        self.vertList[f].add_neighbor(self.vertList[t],w)

    def get_vertices(self):
        '''以列表的形式返回所有的图'''
        return self.vertList.keys()

    def __contains__(self, item):
        return item in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())
