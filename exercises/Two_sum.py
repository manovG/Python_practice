# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:16:16 2022

@author: manov
"""

'''

You have an list of integers, return the indices of the pair of integers that add up to a given target

Each input has one solution
'''

# import pdb

numbers = input('Please add a numbers for TWO SUM task: ')
numbers_list = numbers.split(',')

num_list = [int(i) for i in numbers_list]

def two_sum(nums,target):
    d = {}
    # pdb.set_trace()
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            print(d)
            return [d[target-nums[i]],i]
        
        d[nums[i]] = i
    return -1

