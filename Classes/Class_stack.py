# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 14:12:31 2022

@author: manov
"""

class Stack():
    
    def __init__(self):
        self.list_stack = []
        
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
        
    def push(self,item):
        self.list_stack.append(item)
        
    def pop(self):
        return self.list_stack.pop()
    
    def peek(self):
        
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
        
    def __repr__(self):
        return repr(self.list_stack)