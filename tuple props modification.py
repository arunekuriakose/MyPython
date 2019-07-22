#tuple cannot be modified
l=(1,2,3,4,5)
l[1]=20
print(l)


#list inside tuple can be modified
l=(1,2,3,[4,5,6],7,8,9)
l[3][1]=15
print(l)