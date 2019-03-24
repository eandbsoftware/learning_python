'''
# Slot basics
class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
# AttributeError, must assign before reference
#print(x.age)
x.age = 40
print(x.age)
# AttributeError, illegal: not in __slots__
#x.ape = 1000

# Slots and namespace dictionaries
# When slots are used, instances do not normally have an attribute dictionary
class C:
    __slots__ = ['a', 'b']
X = C()
X.a = 1
print(X.a)
#  AttributeError: 'C' object has no attribute '__dict__'
#print(X.__dict__)

# We can still fetch and set slot-based attributes by name string using storage-
# neutral tools like getattr and setattr and dir
print(getattr(X, 'a'))
setattr(X, 'b', 2)
print(X.b)
print('a' in dir(X))
print('b' in dir(X))

# Without an attribute namespace dictionary it's not possible to
# assign new names to instances that are not names in the slots list
class D:
    __slots__ = ['a', 'b']
    def __init__(self):
        # AttributeError: 'D' object has no attribute 'd'
        self.d = 4
X = D()
'''

# We can still accomodate extra attributes though, by including __dict__
# explicitly in __slots__
class D:
    __slots__ = ['a', 'b', '__dict__']
    # Class attributes work normally
    c = 3
    def __init__(self):
        # d stored in __dict__, a is a slot
        self.d = 4
X = D()
import _1039_Mapping_Attributes_to_Inheritance_Sources as mapper
print(mapper.bespoke_climber(X))
print(X.d)
print(X.c)
# Undefined until assigned
#print(X.a)
X.a = 1
X.b = 2

print(X.__dict__)
print(X.__slots__)
# getattr fetches all three forms from: __slots__, class, and __dict__ 
print(getattr(X,'a'), getattr(X,'c'), getattr(X,'d'))
print()

# Wrong: either may be omitted
for attr in list(X.__dict__) + X.__slots__:
    print(attr, '=>', getattr(X, attr))
print()

# Less wrong
for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))