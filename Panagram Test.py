#Panagram
s=input("Enter the string:").lower()
s=sorted(s)
s=set(s)
a={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s1=s.intersection(a)
if (s1==a)==True:
    print("Panagram")
else:
    print("Not Panagram")