#
s=input("Enter the string: ")
sum=0
t=''
for i in s:
    if(i>='A' and i<='Z') or (i>='a' and i<='z'):
        t+=i
    elif i>='0' and i<='9':
        sum+=int(i)
    elif i==' ':
        t+=str(sum)+' '
        sum=0
t+=str(sum)
print(t)
