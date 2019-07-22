#
def demo():
    n=1
    print("The value of n: ",n)
    yield n

    n+=1
    print("The value of n: ",n)
    yield n

    n+=1
    print("The value of n: ",n)
    yield n

#a=demo()
#print(next(a))
#print(next(a))
#print(next(a))
for i in demo():
    print(next(i))