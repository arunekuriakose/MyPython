#
#
class Demo:
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        nos=self.n
        self.n+=2
        return nos
d=Demo()
a=iter(d)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#print(next(i))            