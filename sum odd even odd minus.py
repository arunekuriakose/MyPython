#Even - Odd from list
l=[25,27,16,4,5,2,8,7]
sum=0
for a in l:
    if a%2==0:
        sum=sum+a
    else:
        sum=sum-a  
print("Sum :",sum)
