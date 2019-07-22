#use of continue in for loop
l=list(range(1,11))
for v in l:
    print("We are in the loop")
    print(v)
    if v%2==0:
        print("We are inside if condition")
        continue
    print("If loop condition is false")
print("for loop finished...")