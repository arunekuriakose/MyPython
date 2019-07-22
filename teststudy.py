
#
#a=list(range(466))
#count=1
#for i in a:
#    if count%10!=0:
#        print(i,sep=' ',end=' ')
#        count+=1
#    else:
#        print(i)
#        count+=1
#year=list(range(1900,2001))
#for y in year:
#    if(y%4==0 and y%100!=0 or y%400==0)and y%7==0:
#        print("Unlucky leap year",end='\n\n\n')
#    elif y%4==0 and y%100!=0 or y%400==0:
#        print("Leap Year",end='\n\n\n')
#    elif y%7==0:
#        print("Unlucky Year")
#    else:
#        print(y,end=' ')
#num=list(range(1,100))
#print(num)
#for i in num:
#    if i%17==0:
#        break
#    else:
#        print(i)
#else:
#    print("Execution completed")


#num=list(range(829,929))
#print(num)
#count=k=0
#for b in num:
#    if b%2==0:
#        count+=1
#        if count%3==0:
#            print(b)
#            k+=1
#    
#else:
#    print("total count",k)


#i=1
#sum=even=0
#while i<=500:
#    if i%2==0:
#        print(i)
#        sum+=i
#    i+=1
#print("sum: ",sum)
        
    
i=4
mul=1
while mul<=10096:
    print("We are inside while loop")
    print(i)
    if mul==64 or mul==4096:
        print("We are inside if condition")
        mul*=i
        continue
    mul*=i
    print(mul,"Outside if loop")
print("While loop finished")
        
        
        