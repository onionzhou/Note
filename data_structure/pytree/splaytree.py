#!/usr/bin/env python3

from pytree.bstree import Node
from pytree.bstree import BSTree


class SplayNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.parent = None


class SplayTree(BSTree):
    def __init__(self):
        BSTree.__init__(self)

    def get_height(self, node):
        return BSTree.get_height(self, node)

    def get_tree_max(self, *args):
        return BSTree.get_tree_max(self, *args)

    def get_tree_min(self, *args):
        return BSTree.get_tree_min(self, *args)

    def preorder_tree(self, *args):
        return BSTree.preorder_tree(self, *args)

    def midorder_tree(self, *args):
        return BSTree.midorder_tree(self, *args)

    def postorder_tree(self, *args):
        return BSTree.postorder_tree(self, *args)

    def delete_tree(self, data):
        return BSTree.delete_tree(self, data)

    def _insert(self, data, T):
        if T is None:
            T = SplayNode(data)
        else:
            parent = T

            if data < parent.data:
                # insert left
                if not parent.left:
                    child = SplayNode(data)
                    parent.left = child
                    child.parent = parent
                else:
                    self._insert(data, parent.left)
            elif data > parent.data:
                if not parent.right:
                    child = SplayNode(data)
                    parent.right = child
                    child.parent = parent
                else:
                    self._insert(data, parent.right)
                    # else  do nothing

        return T

    def insert(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError(str(data) + "is not num")
        else:
            self.root = self._insert(data, self.root)

    def _rotate_to_right(self, node):
        # this var node means: search node's parent node or \
        # grandparent node

        '''
                            g
             root(P)       /\         g
            /             p D        /\
          x              /\   --->  x D
                        x  C       /\
                       /\         A p
                      A B          /\
                                  B C
        '''

        x = node.left
        p = node
        g = node.parent
        p.left = x.right  # B
        if x.right:
            x.right.parent = p  # update B node parent info

        x.right = p
        p.parent = x

        # zig
        if not g:
            self.root = x
            self.root.parent = None
        else:
            g.left = x
            x.parent = g

    def _rotate_to_left(self, node):
        x = node.right
        p = node
        g = node.parent
        p.right = x.left  # B
        if x.left:
            x.left.parent = p  # update B node parent info

        x.left = p
        p.parent = x

        # zig
        if not g:
            self.root = x
            self.root.parent = None
        else:
            g.right = x
            x.parent = g

    def _rotate_to_root(self, node, ):
        # p: parent  g:grandparent
        p = node.parent
        if p:
            g = p.parent
            # zig
            if not g:
                if node == p.left:
                    # avl tree single rotate
                    self._rotate_to_right(p)
                else:
                    self._rotate_to_left(p)

            # zig-zag
            elif g.left == p and p.right == node:
                # avl tree double rotate  "LR"
                self._rotate_to_left(p)
                self._rotate_to_right(g)
            elif g.right == p and p.left == node:
                # avl tree double rotate  "RL"
                self._rotate_to_right(p)
                self._rotate_to_left(g)

            # zig-zig
            elif g.left == p and p.left == node:
                self._rotate_to_right(p)
                self._rotate_to_right(g)
            elif g.right == p and p.left == node:
                self._rotate_to_left(p)
                self._rotate_to_left(g)
            # root node is not parent ,
            self._rotate_to_root(node)

    def find_tree_node(self, data, *args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        if node is None:
            print("not found ")
            return None
        if data < node.data:
            self.find_tree_node(data, node.left)
        elif data > node.data:
            self.find_tree_node(data, node.right)
        else:
            # find  and rotate to root
            self._rotate_to_root(node)
            return node.data


if __name__ == '__main__':
    '''
        有问题
    '''
    num_list = (8, 9, 16, 11, 2, 5, 17, 25, 35, 29, 38)
    tree = SplayTree()
    for n in num_list:
        tree.insert(n)

    tree.midorder_tree()
    max_num = tree.get_tree_max()
    min_num = tree.get_tree_min()
    print(max_num, min_num)
    tree.delete_tree(25)
    tree.midorder_tree()
    s = tree.find_tree_node(11)
    print("---")
    tree.midorder_tree()
    print(s)
