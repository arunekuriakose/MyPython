#
s=input("Enter the string")
c=0
sum=0
t=''
m=''
for i in s:
    if(i>='A' and i<='Z')or(i>='a' and i<='z'):
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            t+='*'+i
            c+=1
        else:
            t+=i
            c+=1
    elif i>='0'and i<='9':
        sum+=int(i)
    elif i==' ':
        if t[0]!='*':
            m+=t[0].upper()+t[1:]+str(sum)+str(c)+' '
        else:
            m+=t[0]+t[1].upper()+t[2:]+str(sum)+str(c)+' '
        t=''
        sum=0
        c=0
if t[0]!='*':
    m+=t[0].upper()+t[1:]+str(sum)+str(c)
else:
    m+=t[0]+t[1].upper+t[2:]+str(sum)+str(c)
print(m)