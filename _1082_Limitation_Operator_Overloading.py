class C:
    def __getitem__(self, ix):
        print('C index')
    
class D(C):
    def __getitem__(self, ix):
        print('D index')
        C.__getitem__(self, ix)
        super().__getitem__(ix)
        #  TypeError: 'super' object is not subscriptable
        #super()[ix]

X = C()
X[99]
print()

X = D()
X[99]


class Fucker:
    def fuck(self, n):
        print('fuck' * n)
class Catcher(Fucker):
    def __getattr__(self, name):
        print(f'caught {name}')
        return lambda x: x

c = Catcher()
getter = c.__getitem__
print(getter(69))
Catcher.fuck(c, 9)
type(c).__getitem__(c, 0)
c[0]