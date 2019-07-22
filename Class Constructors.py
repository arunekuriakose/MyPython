#
class Person:
    first_name='Arun'
    last_name='Kuriakose'
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
#    def display(self):
#        print(self.first_name,self.last_name)
    def __str__(self):
        return 'First Name:'+self.first_name+' Last_Name:'+self.last_name
p1=Person('Deepanshu','Rastogi')
p2=Person('Dulquer','Salman')
#p2.display()
print(p1)
print(p2)
 