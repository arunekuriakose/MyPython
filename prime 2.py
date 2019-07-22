# 
a=list(range(1,301))
k=0
l=1
u=300
for i in range(l,u+1):

    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(i,"is not prime")
            else:
                print(i,"is prime number")

for b in a:
    if b%2==0:
        print(b,"is even")
    else:
        print(b,"is odd")