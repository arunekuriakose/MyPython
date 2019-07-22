#Lambda filter function
"""
n=list(range(1,201))
m=[]
i=0
def pow(n):
    return n**5
for i in n:
    if i%3==0:
        m.append(pow(i))
print(m)"""

#SINGLE LINE CODE USING MAP AND FILTER 
print(list(map(lambda x:x**5,list(filter(lambda x:x%3==0,list(range(1,201)))))))
