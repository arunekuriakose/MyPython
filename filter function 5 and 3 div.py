#filter function div by 3 AND 5
l=list(range(1,301))
l=list(filter(lambda x:x%3==0 and x%5==0,l))
print(l)

