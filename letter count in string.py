#
s=input("Enter the string: ")
t=''
c=0
for i in s:
    if i!=' ':
        t+=i
        c+=1
    else:
        t+=str(c)+' '
        c=0
t+=str(c)
print(t)