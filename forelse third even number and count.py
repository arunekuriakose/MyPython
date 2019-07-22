# for else print 3rd even number and even count
num=list(range(828,929))
print(num)
count=0
k=0
for b in num:
    if b%2==0:
        count+=1
        if count%3==0:
            print(b)
            k+=1
else:
    print("Total count",k)
        
        