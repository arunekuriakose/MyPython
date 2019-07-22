#
def demo(x):
    def mul(n):
        return x*n
    return mul
d1=demo(5)
d2=demo(10)
print(d1(4))
print(d2(3))