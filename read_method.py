#
with open("demo1.txt",'r',encoding='utf-8') as f:
    
    print(f.tell())
    
    #op:0
    print(f.read(5))
    print(f.tell())
    print(f.read(7))
    print(f.tell())
    f.seek(0)
    print(f.read(5))
    print(f.tell())
    for i in f:
        print(i,end="")
    print(f.readline())
    print(f.readlines())