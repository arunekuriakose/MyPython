#
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(i): #i+1
        print(" ",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i): #n-i-2
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i): #i+1
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
        
    print()
    
    