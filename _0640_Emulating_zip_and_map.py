S1 = 'abc'
S2 = 'xyz1233'
print(list(zip(S1, S2)))
print()

# zip pairs items, truncates at shortest
print(list(zip((-2, -1, 0, 1, 2))))
print(list(zip([1, 2, 3], [2, 3, 4, 5])))
print()

# map passes paired items to function, truncates
print(list(map(abs, [-2, -1, 0, 1, 2])))
print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))
print()

# map and zip accept arbitrary iterables
print(list(map(lambda x, y: x + y, open('_0055_A_First_Script.py'), open('_0055_A_First_Script.py'))))
print([x + y for (x, y) in zip(open('_0055_A_First_Script.py'), open('_0055_A_First_Script.py'))])
print()

# Coding your own map(func,...)
# Take an arbitrary number of sequences
def mymap(func, *seqs):
    res = []
    # Unpack sequences to pass to zip
    for args in zip(*seqs):
        # Unpack zipped tuples into individual arguments
        res.append(func(*args))
    return res
print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print()

# As a comprehension
def mymap2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]
print(mymap2(abs, [-2, -1, 0, 1, 2]))
print(mymap2(pow, [1, 2, 3], [2, 3, 4, 5]))
print()

# Using generators
# With generator function syntax
def mymap3(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)
print(list(mymap3(abs, [-2, -1, 0, 1, 2])))
print(list(mymap3(pow, [1, 2, 3], [2, 3, 4, 5])))
print()

# With generator expression syntax
def mymap4(func, *seqs):
    return (func(*args) for args in zip(*seqs))        
print(list(mymap4(abs, [-2, -1, 0, 1, 2])))
print(list(mymap4(pow, [1, 2, 3], [2, 3, 4, 5])))
print()

# Coding your own zip(...) and map(None...)
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    #for i in range(min(len(s) for s in seqs)):
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymappad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

s1, s2 = 'abc', 'xyz123'
print(myzip(s1, s2))
print(mymappad(s1, s2))
print(mymappad(s1, s2, pad=99))
print()

def myzipgen(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

def mymappadgen(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

print(list(myzipgen(s1, s2)))
print(list(mymappadgen(s1, s2)))
print(list(mymappadgen(s1, s2, pad=99)))
print()

# Alternative implementations
def myzipalt(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymappadalt(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    return [tuple((S[i] if i < len(S) else pad) for S in seqs) for i in range(maxlen)]

print(myzipalt(s1, s2))
print(mymappadalt(s1, s2))
print(mymappadalt(s1, s2, pad=99))
print()

# Alternative implementation as a generator
def myzipaltgen(*seqs):
    return (tuple(S[i] for S in seqs) for i in range(min(len(S) for S in seqs)))

print(list(myzipalt(s1, s2)))
print()

# Why you will care
def mylastzip(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

i = iter(mylastzip(s1, s2))
print(next(i))
print(next(i))
print(next(i))
print()

for i in (mylastzip(s1, s2)):
    print(i)
