'''
二分查找
'''
def binary_seach(list,item):

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




if __name__ =='__main__':
    list =[1,2,3,4,55,66,777]

    x=binary_seach(list,66)
    print(x)
