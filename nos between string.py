#nos between String

s=input("Enter the string: ")
c=0
i=0
st=0
ed=0
t=''
while i<len(s):
    if s[i]!=" ":
        st=i
        break
    else:
        i+=1
i=len(s)-1
while i>=0:
    if s[i]!=" ":
        ed=i
        break
    else:
        i-=1
s=s[st:ed+1]
i=0 
while i<len(s):
    if s[i]==" " and s[i+1]!=" ": 
        c+=1
        
        i+=1  
    else:
        i+=1
print("No of words: ",(c+1))
print("Empty String" )  