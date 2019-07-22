#
s=input("Enter the string: ").lower()
t=''
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        t+="*"+i
        
    else:
        t+=i

print(t)