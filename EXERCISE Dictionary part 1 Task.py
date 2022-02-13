# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

# dic = {'France' : 'Paris', 
#         'Germany' : 'Berlin',
#         'Bulgaria' : 'Sofia',
#         'Greece' : 'Athens'}

# unpack1,unpack2 = zip(*dic.items())

# print(unpack1, unpack2)


# country_input = input('Please enter a country: ')

# if country_input in dic:
#     print(dic[country_input])
# else:
#     print('The country you looking for is not in the dictionary!')
#     print('Please try again')


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''


# fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# letter_list = ['a','b','c','d','e','f','g','j','j','k','l','m']

# combine_list = list(zip(fib_list,letter_list))

# # print(combine_list)

# list1,list2 = zip(*combine_list)
# print(list2) 

# dic = {} 


# for i in range(len(fib_list)): 
#     dic[i+1] = fib_list[i]
    
# print(dic)



'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

# dic_stocks = {'PyhonDS':{'Open':'12.87','High':'13.23','Low':'11.42','Close':'13.10'},
#         'PythonSoft':{'Open':'23.54','High':'25.76','Low':'21.87','Close':'22.33'},
#         'Pythazon':{'Open':'98.99','High':'102.34','Low':'97.21','Close':'100.065'},
#         'Pybook':{'Open':'203.63','High':'207.54','Low':'202.43','Close':'205.24'}}

# dic_stocks = {'PyhonDS':{'Open':12.87,'High':13.23,'Low':11.42,'Close':13.10},
#         'PythonSoft':{'Open':23.54,'High':25.76,'Low':21.87,'Close':22.33},
#         'Pythazon':{'Open':98.99,'High':102.34,'Low':97.21,'Close':100.065},
#         'Pybook':{'Open':203.63,'High':207.54,'Low':202.43,'Close':205.24}}
                 

# for key in dic_stocks.keys():
#     # print('\n',key,sep='')
#     for values in dic_stocks[key].keys():
#         print(values, end=' ')




'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
# import pandas as pd
# import matplotlib.pyplot as plt


# df = pd.DataFrame(dic_stocks)
# print(df)

# df.transpose().plot.bar()


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
import random
import string
import matplotlib.pyplot as plt


list_letters = []
list_num = []

for letter in string.ascii_uppercase:
    list_letters.append(letter)

for number in range(len(string.ascii_uppercase)):
    n = float("{:.2f}".format(random.random()))
    list_num.append(n)
    
dic_rnd_letters = dict(zip(list_letters, list_num))

plt.bar(list_letters, list_num)


print(list_letters)
print(list_num)


# n = random.random()
# print(n)

# import random
# randomlist = []
# for i in range(0,5):
#     n = random.randint(1,30)
#     randomlist.append(n)
# print(randomlist)





'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
