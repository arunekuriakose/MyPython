s=input()
t=''
l=[]
for i in s:
    if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=='0':
        l.append(int(i))
    elif i==' ':
        t+=str(sum(l))+i
        l.clear()
    elif i==s[-1]:
        t+=i+str(sum(l))
        l.clear()
    else:
        t+=i
print(t)