# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:33:39 2022

@author: manov
"""

# l1 = [5, 2, 7, 1, 12, 44, 2, 1, 55, 6, 65, 44, 98, 88, 90]

l2 = [1, 1, 2, 2, 5, 6, 7, 12, 44, 44, 55, 65, 88, 90, 98]


def binary_search(list_input, value):
    found = False
    first = 0
    last = len(list_input)-1
    
    while first <= last and found == False:
        midpoint = (first + last)//2
        if list_input[midpoint] == value:
            found = True
        else:                     
            if list_input[midpoint] < value:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found        
            
binary_search(l2, 2)


def linear_search(list_input, value):
    i = 0 
    found = False
    
    while i < len(list_input) and found == False:
        if list_input[i] == value:
            found = True
        else:
            i = i + 1
    return found  