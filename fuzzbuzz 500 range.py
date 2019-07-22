# my way..wrong
num=list(range(501))
count=1
for n in num:
    if n%3==0 and n%5==0:
       n=str("FuzzBuzz")
    elif n%3==0:
        n=str("fuzz")
    elif n%5==0:
        n=str("buzz")
    if count%10!=0:
        print(n,end=" ")
        count+=1
    else:
        print(n)
        count+=1