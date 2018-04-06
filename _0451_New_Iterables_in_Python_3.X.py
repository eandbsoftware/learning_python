'''
# Impacts on 2.X Code
# Must convert to list to print all at once
z = zip('abc', 'xyz')
print(z)
print(list(z))

# Must convert to list to perform sequence operations
z = zip((1, 2), (3, 4))
#print(z[0])

# Must convert to list for multiple pass iterations
m = map(lambda x: 2 ** x, range(3))
for i in m:
    print(i)
for i in m:
    print(i)
print()

# The range Iterable
R = range(10)
print(R)
I = iter(R)
print(next(I))
print(next(I))
print(next(I))
print(list(R))
print()

# Can perform some sequence operation on a range object
# (i.e., len, indexing an concatenation)
print(len(R))
print(R[0])
print(R[-1])
print(next(I))
print(I.__next__())
print()

# The map, zip, and filter Iterables
# map
M = map(abs, (-1, 0, 1))
print(M)
# It's its own iterator!
print(iter(M) == M)
print(next(M))
print(next(M))
print(next(M))
#print(next(M))
print()

# M is exhausted
for x in M:
    print(x)

M = map(abs,(-1, 0, 1))
for x in M:
    print(x)
print(list(map(abs, (-1, 0, 1))))
print()

# zip
Z = zip((1, 2, 3), (10, 20, 30))
print(Z)
print(list(Z))
print()

# Exhausted after one pass
for pair in Z:
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))
for pair in Z:
    print(pair)
print()

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))
print(next(Z))
print()

# filter
f = filter(bool, ['spam', '', 'ni'])
print(f)
print(list(f))
print(list(f))
print()

# Emulate with comprehension with if clause
c1 = [x for x in ['spam', '', 'ni'] if bool(x)]
print(c1)
c2 = [x for x in ['spam', '', 'ni'] if x]
print(c2)
print()
# Multiple Versus Single Pass Iterators
R = range(3)
# range object supports multiple iterators, 
# but is not its own iterator
#print(next(R))
I1 = iter(R)
print(next(I1))
print(next(I1))
I2 = iter(R)
print(next(I2))
print(next(I1))
print()

# map, zip and filter do NOT support multiple active iterators
Z = zip((1, 2, 3), (10, 11, 12))
print(iter(Z) == Z)
I1 = iter(Z)
I2 = iter(Z)
print(next(I1))
print(next(I1))
print(next(I2))
print()

M = map(abs, (-1, 0, 1))
I1 = iter(M); I2 = iter(M)
print(next(I1), next(I1), next(I1))
#print(next(I2))
print()

R = range(3)
I1, I2 = iter(R), iter(R)
print(next(I1), next(I1), next(I1))
print(next(I2))
print()
'''
# Dictionary View Iterables
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()
print(K)
# keys are not iterators themselves
#print(next(K))

# Instead, views have an iterator
I = iter(K)
print(next(I))
print(next(I))

for k in D.keys():
    print(k, end='')
print()
print()

K = D.keys()
print(list(K))
print()

# values is also a view
V = D.values()
print(V)
print(list(V))
print()
# values doesn't support indexing
#print(V[0])
print(list(V)[0])
print()

print(list(D.items()))
for k,v in D.items():
    print(k, v, end=' ')
print(); print()

# Dictionaries themselves produce an iterator,
# that returns the next key
print(D)
I = iter(D)
print(next(I))
print(next(I))
for k in D:
    print(k, end=' ')
print(); print()

print(D)
for k in sorted(D.keys()):
    print(k, end=' ')
print()
for k in sorted(D):
    print(k, end=' ')