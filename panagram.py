#Panagram or not
string1=input("Enter the string: ")
string1=string1.lower()
#print(string1)
#string1=string1.casefold()
#print(string1)
string2=sorted(string1)
#print("string2=",string2)
pan="abcdefghijklmnopqrstuvwxyz"
pan1=sorted(pan)
#print("pan1=",pan1)
string3=set(string2)
#print(string3)
pan2=set(pan1)
#print(pan2)
panagram=string3.intersection(pan2)
pan3=set(pan)
if((panagram==pan3)==True):
    print("Panagaram")
else:
    print("Not Panagram")
    