from __future__ import print_function
'''
# Run in 3.X
class C: pass
X = C()
print(type(X), type(C))
print(isinstance(X, object))
print(isinstance(C, object))
# object is not present in a 2.X classic class's __bases__ tuple
print(C.__bases__)
print()

# Same for built-in types
print(type('spam'), type(str))
print(isinstance('spam', object))
print(isinstance(str, object))
print()

print(type(type))
print(type(object))
print(isinstance(type, object))
print(isinstance(object, type))
print(type is object)
print()

# Implications for defaults
# Run in 2.X
print(dir(object))
print()

# Classic classes do NOT inherit from object - despite result of isinstance!
class C: pass
print(C.__bases__)
c = C()
print(isinstance(c, object), isinstance(c, object))
#print(c.__repr__)
print()

# New-style classes inherit object defaults
class D(object): pass
print(D.__bases__)
d = D()
print(isinstance(d, object), isinstance(D, object))
print(d.__repr__)
'''

# Run in 3.X
class E: pass
print(E.__bases__)
print(E().__repr__)