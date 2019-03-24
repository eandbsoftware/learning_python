import _0988_Multiple_Inheritance.listtree as LT

# Bullet 1:
# If a subclass inherits from a superclass without a __slots__
# the instance __dict__ attribute created for the superclass will
# always be accessible

'''
# Case 1: OK: no __slots__ used
class C(LT.ListTree): pass
X = C()
X.c = 3
print(X)

# Case 2: OK: superclass produces __dict__
# Take away: Side-effect of Bullet 1 means if  a super has no slots
# (but a sub does) instance.__dict__ still exists so can safely be processed
class C(LT.ListTree):
    __slots__ = ['a', 'b']
X = C()
X.c = 3
print(X)

# Case 3: ANY nonslot superclass generates an instance dict,
# even if sibling of super with slots
class A:
    __slots__ = ['a']
class B(A, LT.ListTree): pass

X = B()
X.c = 3
print(X)

# Case 4
class A:
    __slots__ = ['a']
class B(A, LT.ListTree):
    __slots__ = ['b']
X = B()
X.c = 3
print(X)
'''

import _1039_Mapping_Attributes_to_Inheritance_Sources as mapper
class C:
    __slots__ = ('a')
X = C()
mapper.trace(mapper.mapattrs(X, bysource=True))