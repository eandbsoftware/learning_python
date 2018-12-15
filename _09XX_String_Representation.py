# The default display is not very useful or pretty
class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other

x = adder()
print(x)
print(repr(x))
print()

# __repr__ is a fallback when for print and str
class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data

x = addrepr(2)
x + 1
# Obviously calls __repr__
print(x.__repr__())
# Also runs __repr__ since no __str__
print(x)
# Both call __repr__
print(str(x), repr(x))
print()

# __str__ is never a fallback
class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data

x = addstr(3)
x + 1
print(x.__repr__())
print(x)
print(str(x), repr(x))
print()

# In effect, __str__ overrides __repr__ for user-friendly contexts
class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data

x = addboth(4)
x + 1
print(x.__repr__())
print(x)
print(str(x), repr(x))
print()

# __str__ might not be called for nested objects
class Printer:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)

objs = [Printer(2), Printer(3)]
for x in objs: print(x)
print(objs)
print()

# But __repr__ is called in all contexts
class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)

objs = [Printer(2), Printer(3)]
for x in objs: print(x)
print(objs)