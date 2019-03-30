#!/usr/bin/env python3

from pytree.bstree import Node
from pytree.bstree import BSTree


class AvlNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.height = 0


class AvlTree(BSTree):
    '''
    balance binary search tree
    '''

    def __init__(self):
        BSTree.__init__(self)

    def get_height(self, node):
        return node.height if node else -1

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
    def _delete_tree(self, data, T):
        if T is None:
            raise KeyError("data not found ")
        elif data < T.data:
            T.left = self._delete_tree(data, T.left)
            T.height = max(self.get_height(T.left), \
                           self.get_height(T.right))
        elif data > T.data:
            T.right = self._delete_tree(data, T.right)
            T.height = max(self.get_height(T.left), \
                           self.get_height(T.right))
        elif T.left and T.right:  # two children
            # replace with smallest in right subtree
            tmp = self.get_tree_min(T.right)

            T.data = tmp
            T.right = self._delete_tree(T.data, T.right)

        else:  # one or zero children
            if T.left:
                T = T.left
            else:
                T = T.right

        return T

    def delete_tree(self, data):
        return self._delete_tree(data,self.root)

    '''
        LL type
    '''

    def single_rotate_with_right(self, k2):
        '''
        right rotate
        :param k2:
        :return:
        '''
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = max(self.get_height(k2.left), \
                        self.get_height(k2.right)) + 1
        k1.height = max(self.get_height(k1.left, ), \
                        self.get_height(k1.right)) + 1

        return k1  # new root

    '''
        RR type
    '''

    def single_rotate_with_left(self, k2):
        '''
        left rotate
        :param k2:
        :return:
        '''
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2
        k2.height = max(self.get_height(k2.left), \
                        self.get_height(k2.right)) + 1
        k1.height = max(k2.height, \
                        self.get_height(k1.right)) + 1
        return k1

    '''
        LR
    '''

    def double_rotate_with_left(self, k3):
        # RR --> LL
        # rotate between k1 and k2
        k3.left = self.single_rotate_with_left(k3.left)
        # rotate between k3 and k2
        return self.single_rotate_with_right(k3)

    '''
    RL
    '''

    def double_rotate_with_right(self, k3):
        # LL --> RR
        # rotate between k1 and k2
        k3.right = self.single_rotate_with_right(k3.right)
        # rotate between k3 and k2
        return self.single_rotate_with_left(k3)

    def insert(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError(str(data) + "is not num ")
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, T):

        # print("insert data {}".format(data))
        if not T:
            T = AvlNode(data)
        elif data < T.data:
            # insert left child
            T.left = self._insert(data, T.left)
            # Judging the height of the tree
            if (self.get_height(T.left) - \
                        self.get_height(T.right)) == 2:

                if data < T.left.data:
                    # LL
                    T = self.single_rotate_with_right(T)
                else:
                    # LR
                    T = self.double_rotate_with_left(T)

        elif data > T.data:
            # insert right
            T.right = self._insert(data, T.right)
            # Judging the height of the tree
            if (self.get_height(T.right) - \
                        self.get_height(T.left)) == 2:

                if data > T.right.data:
                    # RR
                    T = self.single_rotate_with_left(T)
                else:
                    # RL
                    T = self.double_rotate_with_right(T)
        # else data is in the tree ,we will do nothing

        T.height = max(self.get_height(T.left), \
                       self.get_height(T.right)) + 1

        return T


if __name__ == '__main__':
    num_list = (8, 9, 16, 11, 2, 5, 17, 25, 35, 18)
    # num_list = (8, 9, 16, 11, 2, 5, 17, 25, 35, 29, 38)
    # num_list =(12,14,18,16,20,10)
    tree = AvlTree()
    for n in num_list:
        tree.insert(n)
    tree.preorder_tree()
    print("\n====")
    print(tree.get_tree_min())
    print(tree.get_tree_max())
    print('------')
    tree.delete_tree(17)

    tree.preorder_tree()
