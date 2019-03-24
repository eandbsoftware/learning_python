# Bullet 1: slots in sub but not super
class C: pass
class D(C): __slots__ = ['a']
X = D()
X.a = 1; X.b = 2
print(X.__dict__)
print(D.__dict__.keys())
print()

# Bullet 2: slots in super but not sub
class C: __slots__ = ['a']
class D(C): pass
X = D()
X.a = 1; X.b = 2
print(X.__dict__)
print(C.__dict__.keys())
print()

# Bullet 3: only lowest slot accessible
class C: __slots__ = ['a']
class D(C): __slots__ = ['a']
X = D()
C.a = 'super'
D.a = 'sub'
print(X.a)
print()

# Bullet 4: no class-level defaults
class C: 
    __slots__ = ['a']
    # ValueError: 'a' in __slots__ conflicts with class variable
    a = 99
print()

class C: __slots__ = ['a']
class D(C): __slots__ = ['b']
X = D()
X.a = 1; X.b = 2
#AttributeError: 'D' object has no attribute '__dict__'
#print(X.__dict__)
print(C.__dict__.keys(), D.__dict__.keys())
