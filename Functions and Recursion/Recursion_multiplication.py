# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:30:55 2022

@author: manov
"""


'''
Multiplicaiton table of n with y using recursion:
'''


def multiplication(n,y):
    if n == 1:
        return print(f'{n} x {y} = {n*y}')
    else:
        print(f'{n} x {y} = {n*y}')
        return multiplication(n-1,y)
    

'''
Multiplication table of n from 1 to 10
'''    
def multiplication_2(n):
    if n == 1:
        return print(f'2 x {n} = {2*n}')
    else:
        print(f'2 x {n} = {2*n}')
        return multiplication_2(n-1)
    

'''
Example of Recursion:
'''

def Recursion(i):
    if i == 1:
        return i
    else:
        print(i)
        return Recursion(i-1)
        
# Recursion(100)        
        


