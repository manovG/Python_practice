

'''
Write a function to determine whether a string of brackets is balanced
It should return True if balanced. 
[[({})]] is an example of balanced brackets. [({)})] is not balanced.
'''

import pdb

def balanced_brackets(s):
    pdb.set_trace()   
    
    stack = []  # adding or removing elements | brackets[stack.pop()] != char
    brackets = {'(' : ')',
                '[' : ']',
                '{' : '}'}
    
    for char in s:
        
        if char in brackets.keys():
            
            stack.append(char)
            
        else:
            
            if len(stack) == 0 or brackets[stack.pop()] != char:    
                
                # brackets[stack.pop()] != char ==> execute stack.pop() if the last element of stack not equals (!=) char (current element)
               
                return False
            
    return len(stack) == 0
    