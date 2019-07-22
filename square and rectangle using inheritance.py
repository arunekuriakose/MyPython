#
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
class Square(Rectangle):
    def __init__(self,s):
        super().__init__(s,s)
        #super(Square,self).__init__(s,s)
        #Rectangle.__init__(self,s,s)
s=Square(10)
print(s.area())
print(s.perimeter())