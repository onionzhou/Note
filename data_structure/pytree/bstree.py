#!/usr/bin/env python3
import queue
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
            return self.find_tree_node(data, node.left)
        elif data > node.data:
            return self.find_tree_node(data, node.right)
        else:
            print("---"+str(node.data))
            return node.data

    def find_tree_node_non_recursive(self,data,*args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                print("find _no "+ str(node.data))
                return node.data
        print("fuk")
        return None

    def _insert(self, data, T):

        if not T:
            T = Node(data)
        else:
            if data < T.data:
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
            self.midorder_tree(node.left)
        print(node.data, end=' ')
        if node.right:
            self.midorder_tree(node.right)

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
    def mid_order_tree_non_recursive(self,*args):
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        s = queue.LifoQueue()
        while node or not s.empty():
            while node :
                s.put(node)
                # print(node.data, end=" ")
                node = node.left
            if not s.empty():
                node = s.get()
                print(node.data,end=" ")
                node =node.right
    def pre_order_tree_non_recursive(self,*args):
        '''
        先序非递归操作
        :param args:
        :return:
        '''
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        s = queue.LifoQueue()
        while node or not s.empty():
            while node :
                s.put(node) #第一次访问结点
                print(node.data, end=" ")
                node = node.left
            if not s.empty():
                node = s.get()#第二次访问结点
                node =node.right

    def levelorder_tree(self,*args):
        q = queue.Queue()
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        q.put(node)
        while (not q.empty() ):
            node =q.get()
            print(node.data,end=" ")
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def post_order_tree_non_recursive(self,*args):
        '''
        后序非递归操作
        :param args:
        :return:
        '''
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]
        pass


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

def main():
    '''
         8
        / \
       2   9
          / \
         5  16
            / \
           11 17
    '''
    # num_list = (8, 9, 16, 11, 2, 5, 17)
    # num_list = (10,15,6,4,2,3,11,16,13)
    num_list = (3,4,2,6,7,1,8,5)
    tree = BSTree()
    for n in num_list:
        tree.insert(n)

    # print("\n中序递归")
    # tree.midorder_tree()
    # print("\n中序非递归")
    # tree.mid_order_tree_non_recursive()
    # print("\n先序非递归")
    # tree.pre_order_tree_non_recursive()
    # print("\n先序递归")
    # tree.preorder_tree()
    # print("\n后序非递归")
    # tree.post_order_tree_non_recursive()
    # print("\n后序递归")
    # tree.postorder_tree()
    # print("\n层次")
    # tree.levelorder_tree()
    # print("\n--")
    # max_num = tree.get_tree_max()
    # min_num = tree.get_tree_min()
    # print(max_num, min_num)
    # tree.delete_tree(35)
    # tree.midorder_tree()

def test_find():
    num_list = (30,15,41,33,50,35)
    tree = BSTree()
    for n in num_list:
        tree.insert(n)
    tree.levelorder_tree()
    print("\n")
    find_data = tree.find_tree_node(35)
    find2=tree.find_tree_node_non_recursive(35)
    max_num = tree.get_tree_max()
    print(max_num,find_data,find2)
    print("---")


if __name__ == '__main__':
   main()
    # test_find()