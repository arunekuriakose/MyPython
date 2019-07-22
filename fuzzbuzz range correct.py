#
a=list(range(501))
count=1
for b in a:
    if count%10!=0:
        if b%3==0 and b%5==0:
            print("Fuzz Buzz",end=" ")
            count+=1
        elif b%3==0:
            print("Fuzz",end=" ")
            count+=1
        elif b%5==0:
            print("Buzz",end=" ")
            count+=1
        else:
            print(b,end=" ")
            count+=1
    else:
        """if b%3==0 and b%5==0:
            print("Fuzz Buzz",end=" ")
            count+=1
        elif b%3==0: 
            print("Fuzz",end=" ")
            count+=1
        elif b%5==0:
            print("Buzz",end=" ")
            count+=1"""
        
        print(b)
        count+=1