#

def demo(): 
    n=1
    print("First")
    yield n
        
    n+=1
    print("Second")
    yield n
        
    n+=1
    print("Third")     
    yield n

#a=demo()
#print(next(a))
#print(next(a))
#print(next(a))
for i in demo():
    print(next(i))