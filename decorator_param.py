#!/usr/local/python3.7

def deco(*args, **kwargs):
    def toUpper(func):
        def inside(name):
            for i in range(args[0]):
                func(name.upper())
            return
        return inside
     return toUpper
    
 @deco(3)
 def greeting(name):
     print("Hello "+name)
     
 greeting("beauty!")    
