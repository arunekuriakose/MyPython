#Exam Ques:Hacker Rank:second runner up
l=[]
n=int(input())
j=0
print("Enter",n,"Scores")
while j<n:
    l.append(int(input()))
    j+=1
fbig=-100
sbig=-100
for i in l:
    if fbig<i:
        sbig=fbig
        fbig=i
    elif sbig<i and i!=fbig:
        sbig=i
print("Runner Up: ",sbig)