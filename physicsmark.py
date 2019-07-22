#
l=[]
n=int(input())
j=0
while j<n:
    name=input()
    physics=float(input())
    l.append([name,physics])
    j+=1
g=[]
for i in l:
    g.append(i[1])
    sbig=0
    g.sort()
    j=0
    while j<=len(g):
        if g[j]!=g[j+1]:
            sbig=g[j+1]
            break
        j+=1
g.clear()
for i in l:
    if i[1]==sbig:
        g.append(i[0])
        g.sort()
for i in g:
    print(i)