#Set union
A={1,2,3,4,5,6}
B={7,4,5,6,8,9}
print(A|B)
print(A.union(B))

#Set Intersection
print(A&B)
print(A.intersection(B))

#Set Difference
print(A-B)
print(A.difference(B))
print(B.difference(A))

#Set Symmetric Differnece
print(A^B)
print(A.symmetric_difference(B))

