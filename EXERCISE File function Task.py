# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''


def sum_two(num1,num2):
    print(f'The result of the sum of the two numbers is: {num1 + num2}')
    

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''

def multiply(value1, value2):
    print(f'The result of multiplication is: {2*value1*value2}')


'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''


def power(a,b=2):
    # pdb.set_trace()
    if b != '':
        result = 1
        i = 1
        for i in range(b):
            result*= a
        return(result)   
        
    
def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
        


'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''

f = open('capitals.txt','w')
f.write('Sofia, Skopje, Athens, Berlin, London')
f.close()

f = open('capitals.txt','r')
print(f.read())


'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''

add_capital = input('Please write a capital name to be added in the txt file: ')
f = open('capitals.txt','w')
f.write(add_capital)
f.close()

f = open('capitals.txt','r')
print(f.read())


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

# open both files
with open('capitals.txt','r') as firstfile, open('new_file.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
              # append content to second file
              secondfile.write(line)


'''
Question 7
Remove the incorrectly added capitals from the file or delete some of the capitals in the file 
'''

my_file = open('capitals.txt', 'r')
content = my_file.read()
print(content)
content_list = content.split(',')
my_file.close()

print(content_list)

del content_list[-1]
# # print(content_list)

my_file = open('capitals.txt', 'w')
for list_item in content_list:
    my_file.write(list_item)
my_file.close()

my_file = open('capitals.txt', 'r')
print(my_file.read())
my_file.close()

