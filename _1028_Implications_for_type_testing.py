'''
# Run in 3.X
# New-style classes
class C: pass
class D: pass

c,d = C(), D()
# For classic classes, this will evaluate to true because all instances are of type instance,
# For new-style classes it evaluates to false because an instance's type is it's class
print(type(c) == type(d))

# For classic classes the type of an instance is <type 'instance'>
# For new-style classes the type of an instance is the class from which it was made
print(type(c), type(d))
print(c.__class__, d.__class__)

c1, c2 = C(), C()
# Evaluates to True in both 2.X and 3.X
print(type(c1) == type(c2))
'''

# Run in 2.X
# Classic classes
class C: pass
class D: pass

c, d = C(), D()
# Useless in 2.X because all instances ahve the same 'instance' type
print(type(c) == type(d))
# Must compare __class__ attribute of instance for meaningful type comparison
print(c.__class__ == d.__class__)
print(type(c), type(d))
print(c.__class__, d.__class__)
print ''

# New-style classes
class E(object): pass
class F(object): pass

e, f = E(), F()
print(type(e) == type(f))
print(type(e), type(f))
print(e.__class__, f.__class__)