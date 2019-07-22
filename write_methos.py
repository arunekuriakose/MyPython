#
with open("demo.txt",'w',encoding='utf-8')as f:
    f.write("This is my first line\n")
    f.write("This is my second line\n")
    f.write("This is my third line\n")
f=open("demo.txt")
print(f.read())