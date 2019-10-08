#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/8 11:11
# software: PyCharm

class BinaryTree():
    def __init__(self, rootobj=None):
        self.key = rootobj
        self.left_child = None
        self.right_child = None

    def get_leftchild(self):
        '''返回当前节点左子树所对应的二叉树'''
        return self.left_child

    def get_rightchild(self):
        '''返回当前节点右子树所对应的二叉树'''
        return self.right_child

    def set_rootval(self, obj):
        '''在当前节点中存储参数val中的对象'''
        self.key = obj

    def get_rootval(self):
        '''返回当前节点存储的对象'''
        return self.key

    def insert_left(self, new_node):
        '''新建一颗二叉树，将其作为当前节点的左子节点'''
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:  # 插入一个节点，并将已有的节点降一层
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        '''新建一颗二叉树，将其作为当前节点的右子节点'''
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t


class TreeNode(object):
    def __init__(self,
                 key,
                 val,
                 left=None,
                 right=None,
                 parent=None
                 ):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def has_leftchild(self):
        return self.leftchild

    def has_rightchild(self):
        return self.rightchild

    def is_leftchild(self):
        return self.parent and \
               self.parent.leftchild == self

    def is_rightchild(self):
        return self.parent and \
               self.parent.rightchild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rightchild or self.leftchild)

    def has_anychildren(self):
        return self.rightchild or self.leftchild

    def replace_nodedata(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc

        if self.has_leftchild():
            self.leftchild.parent = self
        if self.has_rightchild():
            self.rightchild.parent = self


class BinSearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def _put(self, key, val, curnode):
        if key < curnode.key:
            if curnode.has_leftchild():
                self._put(key, val, curnode.leftchild)
            else:
                curnode.leftchild = TreeNode(key, val, parent=curnode)

        elif key > curnode.key:
            if curnode.has_rightchild():
                self._put(key, val, curnode.rightchild)
            else:
                curnode.rightchild = TreeNode(key, val, parent=curnode)
                # if key == curnode.key ,do nothing

    def _get(self, key, curnode):
        if key == curnode.key:
            return curnode
        elif key < curnode.key:
            return self._get(key, curnode.leftchild)
        else:
            return self._get(key, curnode.rightchild)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def get(self, key):
        if self.root:
            ret = self._get(key, self.root)
            if ret:
                return ret.payload
            else:
                return None
        else:
            return None

    def __setitem__(self, key, value):
        '''重载[]，写出mytree['num'] = 123456 这样的语句'''
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __contains__(self, key):
        '''实现 in 方法'''
        if self._get(key,self.root):
            return True
        else:
            return False

