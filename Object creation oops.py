#
class ABC():
    fname='a'
    lname='z'
    age=0
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def display(self):
        print("First Name: ",self.fname)
        print("Last Name: ",self.lname)
        print("Age: ",self.age)
a=ABC('Gaurav','Sharma',21).display()
b=ABC("Kush","J",22).display()