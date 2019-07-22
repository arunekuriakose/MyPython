#Raising AN Exception
try:
    a=int(input("Enter a Positive Number: "))
    if a<0:
        raise ValueError("Entered value is not a positive number")
except ValueError as v:
    print(v)