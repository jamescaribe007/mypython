#!/usr/local/bin/python3.7

def greet(name, msg="Hakuna Matata!!!"):
    print("Hello", name + ", "+ msg)
    
def test(a="One", b="Two", c="Three"):
    print(a, b, b)
 
greet("Selina")
greet("Bruce","Are you Batman?")

test()
test(1)
test(1,2)
test(1,2,3)

test(a="X")
test(b="Y")
test(c="Z")
