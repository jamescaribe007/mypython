#!/usr/local/bin/python3.7

def check(func):
    def inside(a,b):
        if b == 0 :
           print("Can't be divided by 0")
           return
        return func(a,b)
     return inside
    
@check
def div(a,b):
    return a/b

#d = check(div)
#print(d(10,2))
#print(d(10/0))

print(div(10,2))
print(div(10/0))

