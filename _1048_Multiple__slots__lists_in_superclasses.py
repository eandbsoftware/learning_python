import _1039_Mapping_Attributes_to_Inheritance_Sources as mapper
class E:
    __slots__ = ['c', 'd']
class D(E):
    __slots__ = ['a', '__dict__']

X = D()
X.a = 1; X.b = 2; X.c = 3
print(X.a, X.c)
[print(f'{repr(c)}, len={len(names)}\n\t{sorted(names)}') for c, names in mapper.bespoke_climber(X, inherited_only=True)]
print()

print(E.__slots__)
print(D.__slots__)
print(X.__slots__)
print(X.__dict__)
print()

# Superclass __slots__ missed!
for attr in list(getattr(X,'__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))
print()

print(dir(X))