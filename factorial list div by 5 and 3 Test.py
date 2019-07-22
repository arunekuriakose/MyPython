#Generate List
l2=list(map(lambda x:x*2,list(filter(lambda x:x%3==0 and x%5==0,list(range(1,51))))))
l3=[]
fact=1
for i in l2:
    for j in range(1,i+1):
        fact*=i
    l3.append(fact)
print(l3)