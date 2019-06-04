#!/usr/local/bin/python3.7

numbers = [1,2,3,4,5,6]

def square(num):
    return num**2

new_list = list(map(square,numbers))

print(new_list)
