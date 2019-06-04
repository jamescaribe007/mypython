#!/usr/local/bin/python3.7

numbers = [1,2,3,4,5,6,7,8,9,10]

def odd(x):
     r = x%2
     if r == 1 :
        return True
     else:
        return False
        
odd_list = list(filter(add,numbers))

print(odd_list)
