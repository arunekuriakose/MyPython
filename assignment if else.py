# Assignment Python if-else 
n=int(input("Enter a positive number between 1 and 100 : "))
if n>=1 and n<=100:
    if n%2==0:
        if n>=2 and n<=5:
            print("Not Weird!")
        elif n>=6 and n<=20:
            print("Weird!")
        elif n>20:
            print("Not Weird!")
    else:
        print("Weird!")
else:
    print("Invalid Constraint")
            
    
    