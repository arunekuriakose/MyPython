#
l=[1,5,13,14]
i=iter(l)
#print(next(i))
#print(next(i))
#print(next(i))
#print(next(i))
##print(next(i))
#for i in l:
#    print(i)
ite=iter(l)
while True:
    try:
        print(next(ite))
    except StopIteration:
        break