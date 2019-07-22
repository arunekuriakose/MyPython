#
class Demo:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        return self.x<other.x
d1=Demo(5)
d2=Demo(10)
print(d1<d2)
