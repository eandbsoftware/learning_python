'''
Main tool: mapattrs() maps all attributes on or inherited by an
instance to the instance or class from which they are inherited.

Assumes dir() gives all attributes of an instance. To simulate
inheritance, uses either the class's MRO tuple, which gives the
search order for new-style classes (and all in 3.X), or a recursive
traversal to infer the DFLR order of classic classes in 2.X.

Also here: inheritance() gives version-neutral class ordering;
assorted dictionary tools using 3.X/2.7 comprehensions.
'''

import pprint

def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)
    
def filterdictvals(D, V):
    '''
    dict D with entries for value V removed.
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b':2}
    '''
    return {K: V2 for K, V2 in D.items() if V2 != V}

def invertdict(D):
    '''
    dict D with values changed to keys (grouped by values).
    Values must all be hashable to work as dict/set keys.
    invertdict(dict(a=1, b=2, c=1)) => {1 : ['a', 'c'], 2 : 'b'}
    '''
    def keysof(V):
        # Returns list of keys of V
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}

def dflr(cls):
    '''
    Classic depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes.
    '''

    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    '''
    Inheritance order sequence: new-style (MRO) or classic (DFRL)
    '''
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)

def mapattrs(instance, withobject=False, bysource=False):
    '''
    dict with keys giving all inherited attributes of instance,
    with values giving the object that each is inherited from.
    withobject: False=remove object built-in class attributes.
    bysource: True=group result by objects instead of attributes.
    Supports classes with slots that preclude __dict__ in instances.
    '''
    attr2obj = {}
    inherits = inheritance(instance)
    attributes = dir(instance)
    for attr in attributes:
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
            # May fail if __slots__ used
            #if attr in obj.__dict__:
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)

def bespoke_climber(instance, with_object=False, inherited_only=False):
    '''
    Returns a tuple containing an object and a list of its attributes. 
    If inherited_only=False, same-named attributes from ALL classes in class
    tree are returned, thus it is equivalent to ListTree. 
    If inherited=True, only unique inherited attributes are returned, 
    thus it is equivalent to mapattrs (which is used in its implementation),
    and similar to dir (but with source attribution).
    
    '''
    def climber(cls):
        # The magic line: either get the inherited attributes or all the attributes in __dict__
        attrs = ([(cls, obj2attr[cls])] if cls in obj2attr else []) if inherited_only else [(cls, list(cls.__dict__.keys()))]
        visited.add(cls)
        for sup in cls.__bases__:
            if sup in visited: continue
            if not with_object and sup is object: continue
            attrs += climber(sup)
        return attrs

    obj2attr = mapattrs(instance, withobject=with_object, bysource=True)
    visited = set()
    attrs = [(instance, dict(instance.__dict__))]
    attrs += climber(instance.__class__)
    return attrs

if __name__ == '__main__':
    import _0988_Multiple_Inheritance.listtree as LT
    class A: attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(LT.ListTree, B, C): pass
    I = D()
    
    # Self-exploration
    print(len(dir(I)), len(mapattrs(I, withobject=True)))
    print(set(dir(I)) == mapattrs(I, withobject=True).keys()); print()
    
    print('All names in class tree:')
    [print(f'{repr(c)}, len={len(names)}\n\t{sorted(names)}') for c, names in bespoke_climber(I)]
    print('\nInherited names only:')
    [print(f'{repr(c)}, len={len(names)}\n\t{sorted(names)}') for c, names in bespoke_climber(I, inherited_only=True)]
    
    print(I)
    
    print('Classic classes in 2.X, new-style in 3.X')    
    print('Py=>%s' %I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')

    print('New-style classes in 2.X and 3.X')
    class A(object): attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass
    I = D()
    print('Py=>%s' %I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, withobject=False, bysource=True), 'OBJS\n')   