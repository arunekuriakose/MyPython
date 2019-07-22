#
def demo():
    n=1
    print("The value of n:",n)
#    return n
    yield n
    n+=1
    print("The value of n:",n)
#    return n
    yield n
    n+=1
    print("The value of n:",n)
#    return n
    yield n
    n+=1
    print("The value of n:",n)
#    return n
    yield n
#    print("The value of n:",n)
a=demo()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
