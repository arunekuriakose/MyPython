#No of words in a string.
s=input("Enter the string: ")
count=1
if s!="":
    s=sorted(s)
    for i in s:
        if i==" ":
            count+=1
    print("No of words= ",count)
else:
    print("Empty")
    