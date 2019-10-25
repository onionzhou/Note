#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:onion
# datetime:2019/10/16 16:40
# software: PyCharm

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
'''
    思路:
    1.建立一个字典，将列表里的数插入形成k-v，
    2.在查找字典中是否有相关的值，返回相应的下标
    注意键值对的选择
'''


def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        # hashmap[num] = i
        if hashmap.get(target - num) is not None:
            return [hashmap.get(target - num), i]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


def twoSum1(nums, target):
    my_dict = {}
    for k, v in enumerate(nums):
        my_dict[v] = k

    for k, v in enumerate(nums):
        # tmp = target - v
        tmp = my_dict.get(target - v)
        if tmp is not None:
            return [k, tmp]


if __name__ == '__main__':
    alist = [2, 5, 5, 11]
    print(twoSum(alist, 10))
