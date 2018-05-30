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



if __name__ =='__main__':

    # binary_search_test()
    # recursion_test()
    quick_sort_test()
