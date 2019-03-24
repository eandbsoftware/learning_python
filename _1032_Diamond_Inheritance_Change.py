# Run in 2.X

'''
# Classic class
class A: attr = 1
class B(A): pass
class C(A): attr = 2
class D(B, C): pass

d = D()
# Fetches 1 for classic class
print(d.attr)

# New-style class
class W(object): attr = 1
class X(W): pass
class Y(W): attr = 2
class Z(X, Y): pass

z = Z()
# Fetches 2 for new-style class
print(z.attr)
'''

# Explicit conflict resolution
# Classic class emulating new-style search order (MRO)
class A: attr = 1
class B(A): pass
class C(A): attr = 2
class D(B, C): attr = C.attr

d = D()
# DFLR would return 1, but explicit assignment lower in tree returns 2
print(d.attr)

# New-style class emulating classic class search order (DFLR)
class A(object): attr = 1
class B(A): pass
class C(A): attr = 2
class D(B, C): attr = B.attr

d = D()
# MRO would return 2, but explicit assignment lower in tree returns 1
print(d.attr)

# Classic class with methods instead of attributes
class A:
    def meth(self): print('A.meth')

class C(A):
    def meth(self): print('C.meth')

class B(A): pass
class D(B, C): pass

d = D()
# DFLR returns A.meth by default
d.meth()

# Emulate MRO
class D(B, C): meth = C.meth
d = D()
d.meth()

# Explicitly implement DFLR
class D(B, C): meth = B.meth
d = D()
d.meth()

# Or just call the desired class explicitly
class D(B, C):
    def meth(self): B.meth(self)
d = D()
d.meth()