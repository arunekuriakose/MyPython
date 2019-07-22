#Function DocString
def greetings(name):
    """This function is used to greet the person whose name you are passing during function call"""
    print("Good Morning!",name,"Have a nice Day")
print(greetings('Dheeraj'))
print(greetings.__doc__)