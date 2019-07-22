#
class Person:
    first_name='Arun'
    last_name='Kuriakose'
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def display(self):
        print(self.first_name,self.last_name)
p1=Person('Deepanshu','Rastogi')
p2=Person('Dulquer','Salman')
p1.display()
p2.display()
