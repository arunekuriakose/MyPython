#Remove duplicate characters from given string without using set.
s=input("Enter the string: ").lower()
s=sorted(s)
t=''
i=0
while i<len(s)-1:
   if s[i]!=s[i+1]:
       t+=s[i]
       i+=1
   else:
       i+=1

if t[-1]!=s[-1]:
    t+=s[-1]
else:
    t+=0
print(s)
        
    
