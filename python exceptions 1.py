#python exception

#a=4
#if a<5
#    print("Hello World")

#compile time error
#i=10
#while i<100:
#print("hello")
#i+=1
#print("End of program")

#runtime error
n1=int(input())
n2=int(input())
print(n1/n2)
print("end of program")
#error:10/0=error
#op:ZeroDivisionError: division by zero

with open("demo1.txt",'r',encoding='utf-8') as f:
    f.read()
print("End")
#op:FileNotFound

import pyfight
print("Hello World")
print("End of program")
#op:ImportError