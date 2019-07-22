#Use of continue in while
i=4
mul=1
while mul<=10096:
    print("We are inside while loop")
    print(i)
    if mul==64 or mul==4096:
        print("We are inside if loop")
        mul*=i
        continue
    mul*=i
    print(mul,"outside if loop")
print("While loop is finished....")