#
with open("lorem.txt",'r',encoding='utf-8') as f:
    s=f.read()
vc=cc=wc=sp=c=p=0
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        if i in 'aeiouAEIOU':#=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vc+=1
        else:
            cc+=1
    elif not(i>='0' and i<='9'):
        if i=='\n':
            c+=1
            if c%2==0:
                wc+=1
                p+=1
        elif i==' ':
            wc+=1
        sp+=1
    
print("Vowel count: ",vc)
print("Consonents Count: ",cc)
print("Word count: ",wc)
print("Special Characters count: ",sp)
print("Paragraph: ",p+1)