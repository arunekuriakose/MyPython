# 
num=list(range(466))
count=1
for n in num:
    if count%10!=0:
        print(n,end=" ")
        count+=1
    else:
        print(n)
        count+=1