#set :How to change a aset in Python?
s={1,2,3,14,16,12}
#print(s[s])

#add single element to set
s.add(16)
print(s)

s.add(25)
print(s)


#cannot add more than one element using add()
#s.add(28,26)
#print(s)

#s.add([24,55,66])
#print(s)

#add multiple elemts from list to set
s.update([24,55,66])
print(s)