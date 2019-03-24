class Slotful:
    __slots__ = ('a', 'b', '__dict__')
    def __init__(self, data):
        self.c = data

I = Slotful(3)
print(list(Slotful.__dict__.keys()))
print(list(I.__dict__.keys()))
I.a, I.b = 1, 2
print(I.a, I.b, I.c)

# Exists and contains only c
print(I.__dict__)
# Use dir to access both __dict__ and __slots__ storage
print([x for x in dir(I) if not x.startswith('__')])

# __dict__ is only one attribute source
print(I.__dict__['c'])
print(getattr(I, 'c'), getattr(I, 'a'))

# dir+getattr is brader than dict and applies to
# slots, properties and descriptors
for a in (x for x in dir(I) if not x.startswith('__')):
    print(a, getattr(I, a))