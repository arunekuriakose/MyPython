#
n=list(range(1,201))
m=[]
i=0
def pow(n):
    return n**5
for i in n:
    if i%3==0:
        m.append(pow(i))
print(m)

    

        