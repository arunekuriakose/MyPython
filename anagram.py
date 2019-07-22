#Anagram or Not Anagram
string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
string1=string1.lower()
string2=string2.lower()
string1=string1.replace(" ","")
string2=string2.replace(" ","")
l1=len(string1)
l2=len(string2)
if(l1==l2):
    string1=sorted(string1)
    string2=sorted(string2)
    string1=set(string1)
    string2=set(string2)
    if((string1==string2)==True):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")


