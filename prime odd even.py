
a=int(range(1,301))
k=0
for i in a:
    d=i//2+1
for b in a:
    b=int(range(2,d))
    for c in b:
        if a%i==0:
            k+=1
    if k<=0:
        print(b,"is prime number")
    else:
        print(b,"is not prime")
        
       