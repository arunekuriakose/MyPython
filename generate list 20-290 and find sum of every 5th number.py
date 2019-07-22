#generate list 20-290 and find sum of every 5th number
n=list(range(20,291))
i=1
sum=0
for b in n:
    if i%5==0:
        sum+=b
    i+=1
print(sum)