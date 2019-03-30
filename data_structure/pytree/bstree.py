#!/usr/bin/env python3
class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BSTree(object):
    '''
    unbalance binary search tree
    '''

    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else -1

    def get_tree_max(self, *args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        if not node.right:
            return node.data
        else:
            return self.get_tree_max(node.right)

    def get_tree_min(self, *args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        if node.left:
            return self.get_tree_min(node.left)
        else:
            return node.data

    def find_tree_node(self, data, *args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        if node is None:
            print("\n++++"+str(data) +" not found ++++ ")
            return None

        if data < node.data:
            self.find_tree_node(data, node.left)
        elif data > node.data:
            self.find_tree_node(data, node.right)
        else:
            return node.data

    def _insert(self, data, T):

        if not T:
            T = Node(data)
        elif data < T.data:
            # insert left child
            T.left = self._insert(data, T.left)
        elif data > T.data:
            T.right = self._insert(data, T.right)
        # if data is in the tree .we'll do nothing
        '''
        T.height = max(self.get_height(T.left), \
                     self.get_height(T.right)) + 1
        '''
        return T

    def insert(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError(str(data) + "is not num ")
        else:
            self.root = self._insert(data, self.root)
            # print(data)

    # it is wrong !!!!
    def error_order(self, *args):
        if self.root:
            node = self.root
            if node.left:
                self.error_order(node.left)
            if node.right:
                self.error_order(node.right)

    def preorder_tree(self, *args):

        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        print(node.data, end=' ')

        if node.left:
            self.preorder_tree(node.left)
        if node.right:
            self.preorder_tree(node.right)

    def midorder_tree(self, *args):

        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        if node.left:
            self.preorder_tree(node.left)

        print(node.data, end=' ')

        if node.right:
            self.preorder_tree(node.right)

    def postorder_tree(self, *args):

        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        if node.left:
            self.postorder_tree(node.left)

        if node.right:
            self.postorder_tree(node.right)

        print(node.data, end=' ')

    def _delete_tree(self, data, T):
        if T is None:
            raise KeyError("data not found ")
        elif data < T.data:
            T.left = self._delete_tree(data, T.left)
            #T.height = max(self.get_height(T.left), \
             #              self.get_height(T.right))
        elif data > T.data:
            T.right = self._delete_tree(data, T.right)
            #T.height = max(self.get_height(T.left), \
             #              self.get_height(T.right))
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
        if not isinstance(data, (int, float)):
            raise TypeError(str(data) + "is not num")
        self.root = self._delete_tree(data, self.root)


if __name__ == '__main__':
    num_list = (8, 9, 16, 11, 2, 5, 17, 25, 35, 29, 38)
    tree = BSTree()
    for n in num_list:
        tree.insert(n)

    tree.midorder_tree()
    max_num = tree.get_tree_max()
    min_num = tree.get_tree_min()
    print(max_num, min_num)
    tree.delete_tree(35)
    tree.midorder_tree()
    s = tree.find_tree_node(88)
    print("---")
    print(s)
