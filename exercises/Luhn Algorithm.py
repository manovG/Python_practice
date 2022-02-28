'''
Luhn Algorithm
Check validity of number
'''



def card_validator(num):
    #conver card number into list
    converted_list = [int(x) for x in str(num)]
    i = 1
    sum1 = 0
    b = 0
    sum2 = 0
    #iterate over every second element 
    while i < len(converted_list):
        sum1 += converted_list[i]
        i += 2
    while b < len(converted_list):
        sum2 += converted_list[b]
        b += 2
    if (sum1+sum2) % 10 == 0:
        print(input('Thank you! Your Credit Card is accepted'))
    else:
        print(input('Your Credit Card is not accepted!'))
          


card_validator(371449635398431)