# print3rd even number within a range
num=list(range(828,929))
print(num)
count=0
k=0
for b in num:
    if b%2==0:
        count+=1
        if count%3==0:
            k+=1
            print(k,".",b)
            if k>20:
                print("Program execution terminated Unsuccessfully")
                break
                
else:
    print("Total count",k)
    print("Successsfully Completed")
    