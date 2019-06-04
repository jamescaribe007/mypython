#!/usr/local/bin/python3.7

def my_gen():
    n=1
    yield n
    
    n+=1
    yield n
    
    n+=2
    yield n

a = my_gen()
print(next(a))
print(next(a))
print(next(a))

for i in mygen() :
    print(i)
