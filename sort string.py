#
s=input("Enter the string: ")
l=list(s)
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if l[i]>l[j]:
            a=l[i]
            l[i]=l[j]
            l[j]=a
    s=''.join(l)
print(s)