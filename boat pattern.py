#Sailing Boat
#Boom
n=5
for i in range(n):
    for j in range(10):
        print(" ",end="")
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print("+",end=" ")
    for j in range(1):
        print("|",end="")
    for j in range(i):
        print("+",end=" ")     
    print()

#Mast
for i in range(1):
    for j in range(20):
        print(" ",end="")
    for j in range(20,21):
        print('|',end=' ')
    print()

#Boat
for i in range(3):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print('*',end=' ')
    for j in range(8):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=' ')
    print()
    
#Water    
for i in range(3):
    for j in range(29):
        print("~",end=" ")