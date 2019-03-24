from _1039_Mapping_Attributes_to_Inheritance_Sources import trace, dflr, inheritance, mapattrs, bespoke_climber
from _0988_Multiple_Inheritance.testmixin0 import Sub

'''
I = Sub()
# 2.X search order: implied object before lister!
trace(dflr(I.__class__))
trace(inheritance(I))
trace(mapattrs(I))
trace(mapattrs(I, bysource=True))
trace(mapattrs(I, withobject=True, bysource=True))
'''

class A(object):
    __slots__ = ['a', 'b']
    x = 1
    y = 2
class B(A):
    __slots__ = ['b', 'c']
class C(A):
    x = 2
class D(B, C):
    z = 3
    def __init__(self):
        self.name = 'holden'

I = D()
trace(mapattrs(I, bysource=True))
print()

print('All names in class tree:')
[print(f'{repr(c)}, len={len(names)}\n\t{sorted(names)}') for c, names in bespoke_climber(I)]
print('\nInherited names only:')
[print(f'{repr(c)}, len={len(names)}\n\t{sorted(names)}') for c, names in bespoke_climber(I, inherited_only=True)]
        