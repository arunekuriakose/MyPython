# leap year unlucy leap year disible by 7 
a=list(range(1900,2001))
for b in a:
    if b%7==0 and (b%4==0 and b%100!=0 or b%400==0):
               print("Unlucky Leap Year",end="\n\n\n")
    elif b%4==0 and b%100!=0 or b%400==0:
        print("Leap Year",end="\n\n")
    elif b%7==0:
        print("Unlucky Year")
    else:
        print(b,end=" ")