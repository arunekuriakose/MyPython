#Global Variable

"""
a=10
def demo():
    print(a)
demo()
print(a)
#O/p:10
     10
     
"""
"""
a=10
def demo():
    a=20
    print(a)
demo()
print(a)
#o/p:20
     10
"""
"""
a=10
def demo():
    print(a)
    a+=10
    print(a)
demo()
print(a)
#Output:UnboundLocalError: local variable 'a' referenced before assignment

"""
a=10
def demo():
    global a
    a+=10
    print(a)
demo()
print(a)
#Output:20
#       20