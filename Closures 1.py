#
def demo(m):
    def inner_demo():
        print(m)
    return inner_demo
d1=demo('Closures')
#del demo
d1()
#demo()
print("Even after deleting demo")
def demo(m):
    def inner_demo():
        print(m)
    return inner_demo
d1=demo('Closures')
del demo
d1()
#demo()