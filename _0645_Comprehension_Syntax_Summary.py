lc = [x * x for x in range(10)]
print(lc)
print()

ge = (x * x for x in range(10))
print(ge)
print(list(ge))
print()

sc = {x * x for x in range(10)}
print(sc)
print()

dc = {x : x * x for x in range(10)}
print(dc)
print()

# Scopes and Comprehension Variables
ge = (X for X in range(5))
# NameError
#print(X)

X = 99
lc = [X for X in range(5)]
print(X)

Y = 99
for Y in range(5):
    pass
print(Y)

X = 'aaa'
def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))
func()
print()

# Comprehending Set and Dictionary Comprehensions
sc1 = {x * x for x in range(10)}
print(sc1)
sc2 = set(x * x for x in range(10))
print(sc2)

dc1 = {x : x * x for x in range(10)}
print(dc)
dc2 = dict((x, x * x) for x in range(10))
print(dc2)
print()

res = set()
for x in range(10):
    res.add(x)
print(res)

res = {}
for x in range(10):
    res[x] = x * x
print(res)
print()

G = ((x, x * x) for x in range(10))
print(next(G))
print(next(G))
print()

# Extended Comprehension Syntax for Sets and Dictionaries
# if clause
lc = [x * x for x in range(10) if x % 2 == 0]
print(lc)
sc = {x * x for x in range(10) if x % 2 == 0}
print(sc)
dc = {x : x * x for x in range(10) if x % 2 == 0}
print(dc)
print()

# Nested for loops
lc = [x + y for x in [1, 2, 3] for y in [4, 5, 6]]
print(lc)
sc = {x + y for x in [1, 2, 3] for y in [4, 5, 6]}
print(sc)
dc = {x : y for x in [1, 2, 3] for y in [4, 5, 6]}
print(dc)
print()

# Iterate over any iterable
sc = {x + y for x in 'ab' for y in 'cd'}
print(sc)
dc = {x + y : (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
print(dc)
sc = {k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
print(sc)
dc = {k.upper() : k *2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
print(dc)