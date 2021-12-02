#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/8 11:11
# software: PyCharm

class BinaryTree(object):
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
                 parent=None,
                 balancefactor=None
                 ):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
        self.balancefactor = balancefactor

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

    def has_bothchildren(self):
        return self.rightchild and self.leftchild

    def replace_nodedata(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc

        if self.has_leftchild():
            self.leftchild.parent = self
        if self.has_rightchild():
            self.rightchild.parent = self

    def find_min(self):
        current = self
        while current.has_leftchild():
            current = current.leftchild
        return current

    def find_successor(self):
        '''找后继节点
        1.如果节点有右节点，那么后继节点就是右子树的中最小的节点
        2.如果节点没有右节点，并且 其本身是父节点的左子节点，那么后继节点就是父节点
        3.如果节点是父节点的右节点，且其本身没有右子节点，那么后继节点就是除其本身外父节点的后继节点
        '''
        suc = None
        if self.has_rightchild():
            suc = self.rightchild.find_min()
        else:
            if self.parent:
                if self.is_leftchild():
                    suc = self.parent
                else:
                    self.parent.rightchild = None
                    suc = self.parent.find_sucfind_successor()
                    self.parent.rightchild = self
        return suc

    def spliceout(self):
        '''移除后继节点'''
        if self.is_leaf():
            if self.is_leftchild():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
        elif self.has_anychildren():
            if self.has_leftchild():
                if self.is_leftchild():
                    self.parent.leftchild = self.leftchild
                else:
                    self.parent.rightchild = self.leftchild
                self.leftchild.parent = self.parent
            else:
                if self.is_leftchild():
                    self.parent.leftchild = self.rightchild
                else:
                    self.parent.rightchild = self.rightchild
                self.rightchild.parent = self.parent

    def __iter__(self):
        '''此处用的 先序遍历，递归操作'''
        if self:
            yield self.key
            if self.has_leftchild():
                for elem in self.leftchild:
                    yield elem
            if self.has_rightchild():
                for elem in self.rightchild:
                    yield elem


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

    def remove(self, curnode):
        '''
        当找到待删除的结点,3种情况
        1.删除结点没有叶子结点
        2.删除结点只有一个子节点
        3.删除结点右两个子节点
        :param curnode: 待删除结点
        :return:
        '''
        if curnode.is_leaf():  # 情况1， 没有叶子结点
            if curnode == curnode.parent.left_child:
                curnode.parent.left_child = None
            else:
                curnode.parent.right_child = None
        elif curnode.has_bothchildren():  # 情况3  有两个子节点
            '''删除该节点需要找一个候选节点替代该位置，该节点要能够保持
            二叉搜索树的关系， 这个候选节点也叫后继节点
            '''
            suc = curnode.find_successor()
            suc.spliceout()
            curnode.key = suc.key
            curnode.payload = suc.payload

        else:  # 情况2 只有一个子节点
            '''
            1.如果当前节点 是一个左子节点，那
                (curnode.leftchild.parent = curnode.parent):当前节点的左子节点对父节点的引用改为指向当前节点的父节点
                (curnode.parent.left_child = curnode.leftchild):父节点对当前节点的引用改为指向当前节点的左子节点

            2.当前节点 是一个右子节点，   curnode的right_childnode 的引用指向 curnode的parent_node
            父节点对当前节点的引用改为指向当前节点的右子节点

            3. 当前节点 没有父节点，那它肯定是根节点，调用replace_nodedata 方法，替换根节点的key,payload
             leftchild rightchild

            4，5，6. 如果当前节点 是一个右孩子,思路类似123
            '''
            if curnode.has_leftchild():  # 当前节点左孩子
                if curnode.is_leftchild():
                    curnode.leftchild.parent = curnode.parent
                    curnode.parent.leftchild = curnode.leftchild

                elif curnode.is_rightchild():
                    curnode.leftchild.parent = curnode.parent
                    curnode.parent.rightchild = curnode.rightchild
                else:
                    curnode.replace_nodedata(
                        curnode.leftchild.key,
                        curnode.leftchild.payload,
                        curnode.leftchild.leftchild,
                        curnode.leftchild.rightchild
                    )
            else:  # 右孩子
                if curnode.is_rightchild():
                    curnode.rightchild.parent = curnode.parent
                    curnode.parent.rightchild = curnode.rightchild
                elif curnode.if_leftchild():
                    curnode.rightchild.parent = curnode.parent
                    curnode.parent.leftchild = curnode.rightchild
                else:
                    curnode.replace_nodedata(
                        curnode.rightchild.key,
                        curnode.rightchild.payload,
                        curnode.rightchild.leftchild,
                        curnode.rightchild.rightchild
                    )

    def delete(self, key):
        if self.size > 1:
            node_toremove = self._get(key, self.root)
            if node_toremove:
                self.remove(node_toremove)
                self.size = self.size - 1
            else:
                raise KeyError('Error,key not in tree!')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,key not in tree!')

    def __delitem__(self, key):
        self.delete(key)

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
        if self._get(key, self.root):
            return True
        else:
            return False

#未验证
class Avltree(BinSearchTree):
    def __init__(self):
        super().__init__()

    def put(self, key, val):
        pass

    def _put(self, key, val, curnode):
        if key < curnode.key:
            if curnode.has_leftchild():
                self._put(key, val, curnode.leftchild)
            else:
                curnode.leftchild = TreeNode(key, val, parent=curnode)
            # 更新平衡因子
            self.update_balance(curnode.leftchild)

        elif key > curnode.key:
            if curnode.has_rightchild():
                self._put(key, val, curnode.rightchild)
            else:
                curnode.rightchild = TreeNode(key, val, parent=curnode)
                # if key == curnode.key ,do nothing
            # 更新平衡因子
            self.update_balance(curnode.rightchild)

    def update_balance(self, node):
        '''
        balancefactor = height(leftsubtree) - height(rightsubtree)
        >0 左倾  balancefactor +1
        =0 平衡  balancefactor  0
        <0 右倾  balancefactor -1

        插入父节点
        :param node:
        :return:
        '''
        if node.balancefactor > 1 or node.balancefactor < -1
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_leftchild():
                node.parent.balancefactor += 1
            elif node.is_rightchild():
                node.parent.balancefactor -= 1
            if node.parent.balancefactor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balancefactor < 0:
            if node.rightchild.balancefactor > 0:
                self.rotate_right(node.rightchild)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balancefactor > 0:
            if node.leftchild.balancefactor < 0:
                self.rotate_left(node.leftchild)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rotroot):
        '''
             'A|-2'
                \                       'B|0'
                'B|-1'       --->        / \
                    \                'A|0'  'C|0'
                    'C|0'

        左旋：、
        1.将右节点（B） ---> 子树的根节点
        2.将旧根节点（A）--> 作为新根的左节点
        3.如果新根节点（B）有左节点，将其添加到新左节点（A）的右节点
            <因为,A节点的右节点以前是链接B节点的，所以左旋后，A肯定没有右节点>
        :return:
        '''
        newroot = rotroot.rightchild
        rotroot.rightchild = newroot.leftchild
        if newroot.leftchild != None:
            newroot.leftchild.parent = rotroot
        newroot.parent = rotroot.parent

        if rotroot.is_root():
            self.root = newroot
        else:
            if rotroot.is_leftchild():
                rotroot.parent.leftchild = newroot
            else:
                rotroot.parent.rightchild = newroot

        newroot.leftchild = rotroot
        rotroot.parent = newroot

        rotroot.balancefactor = rotroot.balancefactor + 1 - min(newroot.balancefactor, 0)
        newroot.balancefactor = newroot.balancefactor + 1 - max(rotroot.balancefactor, 0)

    def rotate_right(self):
        pass


if __name__ == '__main__':
    alist = [17, 5, 25, 2, 11, 35, 9, 16, 29, 38, 7]
    t = BinSearchTree()
    for i in alist:
        t.put(i, i)
    print(t.get(25))
    for i in t:
        print(i, end=' ')
    print(" ")
    t.delete(25)
    for i in t:
        print(i, end=' ')
