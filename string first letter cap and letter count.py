#
#
s=input("Enter the string: ")
t=''
o=''
c=0
for i in s:
    if i!=' ':
        t+=i
        c+=1
    else:
        
        o+=t[0].upper()+t[1:]+str(c)+' '
        t=''
        c=0
o+=t[0].upper()+t[1:]+str(c)
print(o)