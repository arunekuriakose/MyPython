#Local Variable
"""
def demo():
    a=10
    print(a)
    a+=20
    print(a)
demo()
print(a)
#O/p:NameError: name 'a' is not defined
"""
a=10
def demo():
    print(a)
    global a
    a+=20
    y=30
    print(a)
    print(y)
    y+=1
    print(y)
demo()
print(a)
#SyntaxError: name 'a' is used prior to global declaration