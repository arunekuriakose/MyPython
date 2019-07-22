#
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
#        return "{0},{1}".format(self.x,self.y)
    def __add__(self,ot):
        x=self.x+ot.x
        y=self.y+ot.y
        return Point(x,y)
P1=Point(5,7)
P2=Point(-2,8)
#print(d1+d2)
print(P1+P2)
