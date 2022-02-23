# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 08:17:06 2022

@author: manov
"""

''' 1. Write a Python program to calculate the sum of a list of numbers: '''

just_list = [1, 2, 3, 4, 5, 6]

def list_sum(list_data):
    if len(list_data) == 1:
        return list_data[0]
    else:
        return list_data[0] + list_sum(list_data[1:])
        
print(list_sum(just_list))       


''' 2. Convert a number to and from base B: '''

def numbers(input_string):
    strings = [str(integer) for integer in input_string]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer


list_result = []
def num_base(num,num2):
    if num == 0:
        return numbers(list_result)
    else:
        list_result.insert(0,num%num2) 
        return num_base(num//num2,num2) 

 