#Upper to Lower & Lower to Upper
#
s=input("Enter the string: ")
t=''
o=''
c=0
for i in s:
    if(i>='a' and i<='z'):
        t+=i.upper()
        c+=1
    else:
        
        o+=t[0].upper()+t[1:]+str(c)+' '
        t=''
        c=0
o+=t[0].upper()+t[1:]+str(c)
print(o)