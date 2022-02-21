# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:05:50 2022

@author: manov
"""

'''
Function tower of Hanoi
'''

# https://en.wikipedia.org/wiki/Tower_of_Hanoi

count = 0
def towers_of_hanoi(A,B,C,n):
    global count 
    
    if n == 1:
        disk = A.pop()
        C.append(disk)
        count +=1    
    else:
        
        towers_of_hanoi(A,C,B,n-1)
        
        towers_of_hanoi(A,B,C,1)
        
        towers_of_hanoi(B,A,C,n-1)
    return count   
       