#
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
def guessgame():
    n=int(input("🕴️ Guess the number (1-10) 😇: "))
    if n<a and n>0:
        raise ValueTooSmallError("The Guessed Value Is Less Than Original Value.🙄")
    elif n>a and n<11:
        raise ValueTooLargeError("The Guessed Value Is Greater Than Original Value.🙄")
    elif n==a:
        print("🏆 Congrats!!You Have Guessed The Correct Value.😀")
    else:
        print("Invalid Input.🤯")
        guessgame()   
a=4
print("Guess Game",end="")
try:
    guessgame()
except ValueTooSmallError as s:
    print(s)
except ValueTooLargeError as l:
    print(l)