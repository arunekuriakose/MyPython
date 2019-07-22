#Panagram or not
string1=input("Enter the string: ")
string1=string1.lower()
string1=sorted(string1)
pan="abcdefghijklmnopqrstuvwxyz"
pan=sorted(pan)
string1=set(string1)
pan=set(pan)
panagram=string1.intersection(pan)
pan=set(pan)
if((panagram==pan)==True):
    print("Panagaram")
else:
    print("Not Panagram")