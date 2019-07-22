#
#Custom Exception
#class StringLengthError(Exception):
#    pass
#
#n=input("Enter string with greater than 6:")
#if len(n)<=6:
#    raise StringLengthError("String Length Should Be more than 6")
#print("Program Succesfully completed")



class StringLengthError(Exception):
    pass
try:
    
    n=input("Enter string with greater than 6:")
    if len(n)<=6:
        raise StringLengthError("String Length Should Be more than 6")
except StringLengthError as s:
    print(s)
print("Program Succesfully completed")