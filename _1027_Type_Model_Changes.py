'''
# Run in 2.X

# Classic class
class C: pass

I = C()
print(type(I), I.__class__)
print(type(C))
#print(C.__class__)

# Built-in type for comparison
print(type([]), [].__class__)
print(type(list), list.__class__)
print ''

# New-style class
class D(object): pass

d = D()
print(type(d), d.__class__)
print(type(D), D.__class__)
'''

# Run in 3.X
# All classes are new-style
class E: pass

e = E()
print(type(e), e.__class__)
print(type(E), E.__class__)
print(type([]), [].__class__)
print(type(list), list.__class__)