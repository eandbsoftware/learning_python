class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)
        
x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
print()

y = Wrapper({'a': 1, 'b': 2})
print(list(y.keys()))
print()

z = Wrapper('jason')
# Operators are not intercepted in 3.X, but are in 2.X
mystr = z.__repr__()
print(mystr)