import sys
l=["hello",1,2,0]
for i in l:
    try:
        r=1/int(i)
    except:
        print(sys.exc_info()[0])
    print(r)