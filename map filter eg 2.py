#
print(list(map(lambda x:x**2,list(filter(lambda x:x%2==0,list(map(lambda x:x**3,list(filter(lambda x:x%3==0 and x%5==0,list(range(1,501)))))))))))