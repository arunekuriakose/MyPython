#
class person():
    first_name="Superman"
    last_name="Sreenivas"
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def disp(self):
        print(self.first_name,self.last_name)
d=person("Spider","Reddy").disp()