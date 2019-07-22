#
s=input("Enter the string: ").lower()
c=0
i=0
st=0
ed=0
v=0
c=0
n=0
s=0
sc=0
"""
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
"""
s1=sorted(s)

v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
n={0,1,2,3,4,5,6,7,8,9}
sp={";",",",".","!","/"}


