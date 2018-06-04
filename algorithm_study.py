'''
二分查找
'''
def binary_search(list,item):

    low = 0
    high = len(list)-1

    while low <= high:

        mid = int((low + high)/2)

        guess = list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = guess + 1
        else:
            high = guess -1

    return None

def binary_search_test():

    list = [1, 2, 3, 4, 55, 66, 777]

    x = binary_search(list, 66)

    print(x)
# ------------------------------

#递归
def count_num(i):

    print(i)

    if i <= 1:
        return
    else:
        count_num(i-1)

def recursion_test():
    count_num(5)
#--------------------------

'''
    快排
'''
def quickSort(list):

    if len(list) < 2 :
        return list
    else:
        base = list[0] #基准条件

        base_left = [i for i in list[1:] if i<=base] #< 基准条件的子数组

        base_right = [i for i in list[1:] if i>base] #> 基准条件的子数组

        return quickSort(base_left) + [base] + quickSort(base_right)


def quick_sort_test():
    list = [3,5,22,3,1]
    print(quickSort(list))


'''
广度优先搜索
'''
from collections import deque

def person_is_found(name):

    return name[-1] =='e' # 找 u 结尾的人名

def breadthFirstSeach(name, graph=None):

    search_queue = deque()
    search_queue += graph[name]
    searched =[] #记录检查过的人

    while search_queue:

        person = search_queue.popleft()#取出第一个人
        # if  person not in searched:
        if person_is_found(person):
            print('got it %s' %person)
            return True
        else:
            search_queue += graph[person]
            searched.append(person)

    return False


def BFS_test():
    my_dict ={}
    my_dict['my_friend'] = ['onion','zhouzhou','juanjuan']
    my_dict['onion'] =['alice','time']
    my_dict['zhouzhou'] =['tutu','meimei']
    my_dict['juanjuan'] =['tutu','chouchoe']
    my_dict['alice'] =['eee']
    my_dict['tim'] =[]
    my_dict['tutu']=[]
    my_dict['meimei'] =[]
    my_dict['chouchoe']=[]
    my_dict['eee']=[]

    breadthFirstSeach('my_friend',my_dict)







if __name__ =='__main__':

    # binary_search_test()
    # recursion_test()
    # quick_sort_test()
    BFS_test()
