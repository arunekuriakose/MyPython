#
class Student:
    def __init__(self):
        self.__grade='A+'
    def display(self):
        print("Ram grade: ",self.__grade)
    def sets(self,a):
        self.__grade=a
c1=Student()
c1.display()
c1.__grade='C+'
c1.display()
c1.sets('D-')
c1.display()
        