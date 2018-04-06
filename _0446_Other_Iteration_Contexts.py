path = r'.\resources\script2_0433.py'
for line in open(path):
    print(line.upper(),end='')
print()

uppers = [line.upper() for line in open(path)]
print(uppers)
print()

map_result = map(str.upper, open(path))
print(map_result)
print(list(map_result))
print()

# Functions that accept iterables are iteration contexts
s = sorted(open(path))
print(type(s), s)

z = zip(open(path), open(path))
print(type(z), list(z))

e = enumerate(open(path))
print(type(e), list(e))

f = filter(bool, open(path))
print(type(f), list(f))

import functools, operator
r = functools.reduce(operator.add, open(path))
print(type(r), repr(r))
print()

# Constructors are contexts too
l = list(open(path))
print(l)
t = tuple(open(path))
print(t)

j = '&&'.join(open(path))
print(repr(j))
print()

# Tools you might not expect use the iteration protocol
# Sequence assignment
a, b, c, d = open(path)
print(repr(a), repr(d))

# Extended sequence assignment
a, *b = open(path)
print(repr(a), repr(b))

# in membership test
print('y = 2\n' in open(path))
print('x = 2\n' in open(path))

# Slice assignment
L = [11, 22, 33, 44]
L[1:3] = open(path)
print(L)

# list.extend method
L = [11]
L.extend(open(path))
print(L)

# list.append adds the entire iterable without iterating it
L = [11]
L.append(open(path))
print(L)
print(list(L[1]))
print()

# set and dictionary constructors/comprehensions
s = set(open(path))
print(s)

s = {line for line in open(path)}
print(s)

d = {ix: line for ix, line in enumerate(open(path))}
print(d)
print()

# set and dictionary extended comprehension syntax
s = {line for line in open(path) if line[0] == 'p'}
print(s)

d = {ix: line for (ix, line) in enumerate(open(path)) if line[0] == 'p'}
print(d)
print()

# Generators
g = (line.upper() for line in open(path))
print(type(g), g, list(g))
for l in g:
    print(l, end=' ')
print()

# Reducers
print(sum([3, 2, 4, 1, 5, 0]))
print(any(['spam', '', 'ni']))
print(all(['spam', '', 'ni']))
print(max([3, 2, 4, 1, 5, 0]))
print(min([3, 2, 4, 1, 5, 0]))
print()

print(repr(max(open(path))))
print(repr(min(open(path))))
print()

# Argument unpacking
def f(a, b, c, d):
    print(a, b, c, d, sep='&')

f(1, 2, 3, 4)
f(*[1, 2, 3, 4])
f(*open(path))

# Using argument-unpacking syntax to unzip
X = 1, 2
Y = 3, 4
print(list(zip(X, Y)))
A, B = zip(*zip(X, Y))
print(A, B)