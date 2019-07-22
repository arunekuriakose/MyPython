#PATTERN MODULES
print("BASIC PATTERNS")
print()
print("---------------------------")
print("PATTERN 1")
print()
n=5
#
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 2")
print()
#
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
#   
print()
print("---------------------------")
print("PATTERN 3")
print()
#
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 4")
print()
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
print()
print("---------------------------")
print("PATTERN 5")
print()
#
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 6")
print()
#
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 7")
print()
#
for i in range(n):
    for j in range(n+n-1):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 8")
print()
#
for i in range(n):
    for j in range(1):
        print("*",end=" ")
    print()
#
    
print()
print("---------------------------")
print("PATTERN 9")
print()
#
for i in range(n):
        print("*",end=" ")
print()
#

print()
print("---------------------------")
print("PATTERN 10")
print()
#
for i in range(n):
    print("*",end=" ")
print()
for i in range(n):
    for j in range(1):
        print("*",end=" ")
    for j in range(3):
        print(" ",end=" ")
    for j in range(1):
        print("*",end=" ")
    print()
for i in range(n):
    print("*",end=" ")
#   
print()

