#
class Over:
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "{}".format(self.x)
    def __add__(self,ot):
        return self.x+ot.x
    def __sub__(self,ot):
        return self.x-ot.x      
    def __mul__(self,ot):
        return self.x*ot.x
O1=Over(3)
O2=Over(4)
print(O1+O2)
print(O1-O2)
print(O1*O2)
        
