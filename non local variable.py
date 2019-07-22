#Non Local Variable
"""
def demo():
    x=10
    def demo2():
        print(x)
    demo2()
demo()
op:10
"""
"""
def demo():
    x=10
    def demo2():
        x+=20
        print(x)
    demo2()
demo()
#op:UnboundLocalError
"""

def demo():
    x=10
    def demo2():
        nonlocal x
        x+=20
        print(x)
    demo2()
demo()
#op:30
