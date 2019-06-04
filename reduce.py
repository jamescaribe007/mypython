#!/usr/local/bin/python3.7

from functools import reduce

numbers = [1,2,3,4,5,6]

def multiply(prev, next):
    return prev * next

product = reduce(multiply, numbers)

print(product)
