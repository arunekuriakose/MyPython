#Star Pattern
#top division
n=int(input())
for i in range(n):
    for j in range(n):
        print("  ",end="")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()
#2nd division
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print('*',end=' ')
    for j in range(n-1):
        print("  ",end="")
    for j in range(n-1):
        print("  ",end="")
    for j in range(n-i):
        print('*',end=' ')
    print()
#3rd division
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n-1):
        print("  ",end="")
    for j in range(n-1):
        print("  ",end="")
    for j in range(i+1):
        print("*",end=" ")
    
    print()
#Bottom
for i in range(n):
    for j in range(n):
        print("  ",end="")
    for j in range(n-i):
        print('*',end=' ')
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print('*',end=' ')
    print()
    
    