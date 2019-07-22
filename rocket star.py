#
#top Cone
n=5	
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i):
        print(" ",end="")
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(n-1-i):
        print(" ",end="")
    print()
   
#Body cylinder 1
b=9
for i in range(b):
    for j in range(b):
        print(" ",end="")
    for j in range(b):
        print("*",end="")
    print()
#Third
for i in range(n):
    for j in range(5):
        print(" ",end="")
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+4):
        print("*",end="")
    for j in range(n+i):
        print("*",end="")
    print()
#Fourth
for i in range(n):
    for j in range(5):
        print(" ",end="")
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+4):
        print("*",end="")
    for j in range(n+i):
        print("*",end="")
    print()
#Fire
b=9
for i in range(b):
    for j in range(b):
        print(" ",end="")
    for j in range(b):
        print("|",end="")
    print()
    