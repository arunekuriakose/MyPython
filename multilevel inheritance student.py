#
class Person:
    def __init__(self):
        self.name=input("Enter the name:")
        self.age=input("Enter the age:")
        self.gender=input("Enter the gender:")
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

class Marks:
    def __init__(self):
        self.m1=int(input("Enter m1 marks: "))
        self.m2=int(input("Enter m3 marks: "))
        self.m3=int(input("Enter m2 marks: "))
    def display(self):
        print("Total: ",(self.m1+self.m2+self.m3))

class Student(Person,Marks):
    def __init__(self):
        #Constructor call(Person)
        Person.__init__(self)
        #Constructor call(Marks)
        Marks.__init__(self)
    def disp(self):
        Person.display(self)
        Marks.display(self)
s1=Student()
s2=Student()
s1.disp()
s2.disp()