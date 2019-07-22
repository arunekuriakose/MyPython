#check divisible by 3 ,5 or both
nos=int(input("Enter any number : "))
if nos%3==0 and nos%5==0:
    print("fuzzbuzz")
elif nos%5==0:
    print("buzz")
elif nos%3==0:
    print("fuzz")
else:
    print("Invalid Number")