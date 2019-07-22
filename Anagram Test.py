#Anagram
s1=input("Enter The First String:").lower()
s2=input("Enter The Second String:").lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
l1=len(s1)
l2=len(s2)    
if l1==l2:
    s1=sorted(s1)
    s2=sorted(s2)
    s1=set(s1)
    s2=set(s2)
    if(s1==s2):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")    