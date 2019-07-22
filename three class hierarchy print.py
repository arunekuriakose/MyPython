#
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        print("In Rectangle")
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
class Square1(Rectangle):
    def __init__(self,s):
        super().__init__(s,s)
        print("In square 1")
        #super(Square,self).__init__(s,s)
        #Rectangle.__init__(self,s,s)
class Square2(Square1):
    def __init__(self,s):
        super().__init__(s)
        print("In square 2")
s1=Square2(10)

print(s1.area())
print(s1.perimeter())
s2=Square1(5)
print(s2.area())
print(s2.perimeter())
s3=Rectangle(10,20)
print(s3.area())
print(s3.perimeter())