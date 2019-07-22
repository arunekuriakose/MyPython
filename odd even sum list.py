#Odd and Even sum from list
l=[25,27,16,4,5,2,8,7]
odd=0
even=0
for a in l:
    if a%2==0:
        even=even+a #even+=a
    else:
        odd=odd+a  #odd+=a
print("Odd Sum :",odd)
print("Even Sum :",even)
    