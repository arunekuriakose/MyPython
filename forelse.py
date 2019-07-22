# for else
num=list(range(17))
print()
print(num)
print()
for i in num:
    if i%17==0:
        break
    else:
        print(i)
else:
    print("completed...")
