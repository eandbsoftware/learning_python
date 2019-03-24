# Diamond: order differs for new-style classes
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
# D, B, C, A, object
print(D.__mro__)
print()

# Non-diamond: the search order is still as it has been
class A: pass
class B(A): pass
class C: pass
class D(B, C): pass
# D, B, A, C, object
print(D.__mro__)
print()

# Non-diamond with same MRO as first diamond
class A: pass
class B: pass
class C(A): pass
class D(B, C): pass
# D, B, C, A, object
print(D.__mro__)
print()
# object shows up only once in MRO, eventhough it is an automatic base class of multiple toplevel classes
print(f'A.__bases__: {A.__bases__}')
print(f'B.__bases__: {B.__bases__}')
print(f'C.__bases__: {C.__bases__}')
print(f'D.__bases__: {D.__bases__}')
print()

# Technically, implied object superclass always creates a diamond in multiple inheritance,
# but the inheritance search order is effectively as before, but with object searched last
class X(): pass
class Y(): pass
class A(X): pass
class B(Y): pass
class D(A, B): pass
# D, A, X, B, Y
print(D.__mro__)
print()

print(X.__bases__, Y.__bases__)
print(A.__bases__, B.__bases__)
print()

print(D.mro() == list(D.__mro__))
print([cls.__name__ for cls in D.__mro__])