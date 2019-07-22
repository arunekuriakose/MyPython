#
name=''
b=True
while b:
    name=input("Enter your name:")
    if name=='':
        print("Invalid input")
    else:
        print("Welcome")
        b=False
