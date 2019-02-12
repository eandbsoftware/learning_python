'''
Run in Python 2.X
attribute fetch for operators skips instances => neither __getattr__ or __getattribute__ intercept calls from operators
'''

# 2.X classic class - operator attribute fetch routed through __getattr__
# because operators fetch attributes as instance.method
class A:
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)

X = A()
print(X[0])
print(X)
print ''

# 3.X new-style class - operator attribute fetch NOT routed through __getattr__
# because operators fetch attributes as class.method
class B(object):
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)

X = B()
# Type error: object does not support indexing because it is not routed through __getattr__
#print(X[0])
# Uses default __str__
print(X)
print ''

# 2.X classic class - attribute fetch beginst with instance (i.e. instance.method)
class C: pass
X = C()
X.normal = lambda: 99
print(X.normal())
# Override __add__ on instance
X.__add__ = lambda(y): 88 + y
print(X.__add__(1))
# __add__ called by operator
print(X + 1)
print ''

# 3.X new-style class - attribute fetch begins with class (i.e., class.method) so override on instance is ignored
class D(object): pass
X = D()
X.normal = lambda: 99
print(X.normal())
# Override __add__ on instance
X.__add__ = lambda(y): 88 + y
print(X.__add__(1))
# __add__ NOT called by operator; in other words, attribute lookup skips the instance
# TypeError exception thrown
#print(X + 1)
print ''

# 3.X new-style class - __getattr__ intercepts normal attributes and direct calls to __X__ names, but not operators
class E(object):
    def __getattr__(self, name):
        print(name)

X = E()
# Normal names still routed throgh __getattr__
X.normal
# Direct calls to operator methods are also routed through __getattr__
# Note that I am just fetching the __add__ attribute, not calling it
X.__add__
# But implicit calls from operators are NOT!
X + 1