#Leap year using calendar
import calendar
print(calendar.isleap(2004))
print(calendar.isleap(1975))


#odd or even printing in single line
for j in range(1,11):
    print([f"{j}odd",f"{j}even"][j%2==0])
    
n=5#levels of tree
for level in range(1,n+1):
    print(level*'*')
for level in range(1,n+1):
    print(' '*(n-level)+level*'*')
    
    