'''
Run in Python 2.X
'''

'''
# In a more realistic delegation scenario, built-in operations no longer
# work the same as their traditional direct-call equivalents 
class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)

X = C()

print(X.__getitem__(1))
# TypeError: 'C' object does not support indexing
#print(X[1])
# AttributeError: type object 'C' has no attribute __getitem__
print(type(X).__getitem__(X, 1))

print(X.__add__('eggs'))
# TypeError: unsupported operand type(s) for +: 'C' and 'str'
#print(X + 'eggs')
# AttributeError: type object 'C' has no attribute __add__
print(type(X).__add__('eggs'))
'''

# Proxy coding pattern for 3.X
class D():
    data = 'spam'
    def __getattr__(self, name):
        if name == '__iter__' or name == '__repr__': return
        print('getattr: ' + name)
        return getattr(self.data, name)
    # Returns result, rather than method in redefined operator methods
    def __getitem__(self, i):
        print('getitem: ' + str(i)) 
        return self.data[i]
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)

X = D()
# Intercepted by __getattr__
print(X.upper)
print(X.upper())
print ''

# All calls now CALL redefined __getitem__
print(X[1])
print(X.__getitem__(1))
print(type(X).__getitem__(X, 1))
print ''

print(X + 'eggs')
print(X.__add__('eggs'))
print(type(X).__add__(X, 'eggs'))
