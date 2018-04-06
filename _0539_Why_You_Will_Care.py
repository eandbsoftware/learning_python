import builtins

path = r'./resources/script2_0433.py'
'''
def makeopen(id):
    original = builtins.open
    def custom(*pargs, **kargs):
        print('Custom open call %r' % id, pargs, kargs)
        return original(*pargs, **kargs)
    builtins.open = custom

F = open(path)
print(F.read())
print()

makeopen('spam')
F = open(path)
print(F.read())
print()

makeopen('eggs')
F = open(path)
print(F.read())
'''

class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *pargs, **kargs):
        print('Custom open call %r:' % self.id, pargs, kargs)
        return self.original(*pargs, **kargs)

my_open = makeopen('spam')
print(my_open.id)

F = open(path)
print(F.read())