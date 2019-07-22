# Leap year or not
l=[2004,2003,2016,2017,2019,1996,1998,1999]

for a in l:
    if a%4==0 and a%100!=0 or a%400==0:
        print("{} is Leap Year".format(a))
    else:
        print(a,"is Not Leap Year")