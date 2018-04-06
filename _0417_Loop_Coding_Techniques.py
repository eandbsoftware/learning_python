'''
# Counter Loops: range
print(list(range(5)))
print(list(range(2,5)))
print(list(range(0,10,2)))
print()

print(list(range(-5, 5)))
print(list(range(5, -5, -1)))
print()

for i in range(3):
    print(i, 'pythons')
print()

# Sequence Scans: while and range Versus for
# Iterate through a sequence with for
X = 'spam'
for c in X:
    print(c, end=' ')
print()

# Iterate with a while loop
i = 0
while i < len(X):
    print(X[i], end=' ')
    i += 1
print()
print()

# Iterate manually with a for
print(X)
print(len(X))
print(list(range(len(X))))

for i in range(len(X)):
    print(X[i], end=' ')
print()

# Sequence Shufflers: range and len
S = 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end= ' ')
print()

for i in range(len(S)):
    X = S[i:] + S[0:i]
    print(X, end=' ')
print()

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[0:i]
    print(X, end=' ')
print()

# Nonexhaustive Traversals: range Versus Slices
S = 'abcdefghijk'
print(len(S))
print(list(range(0,len(S), 2)))

for i in range(0, len(S), 2):
    print(S[i], end=' ')
print()

for c in S[::2]:
    print(c, end=' ')

# Changing Lists: range Versus Comprehensions
L = [1, 2, 3, 4, 5]
for x in L:
    x += 1
print(L)
print(x)

for i in range(len(L)):
    L[i] += 1
print(L)

i = 0
while i < len(L):
    L[i] += 1
    i += 1
print(L)

c = [x + 1 for x in L]
print(c)

# Parallel Traversals: zip and map
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(zip(L1, L2))
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(T1, T2, T3)))

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))

# map equivalence in Python 2.X
S1 = 'abc'
S2 = 'xyz123'
# Only works in 2.X
print(list(map(None, S1, S2)))

print(list(map(ord,'spam')))
res = []
for c in 'spam':
    res.append(ord(c))
print(res)

# Dictionary construction with zip
D1 = {'spam' : 1, 'eggs' : 2, 'toast' : 3}
print(D1)

D1 = {}
D1['spam'] = 1
D1['eggs'] = 2
D1['toast'] = 3
print(D1)
print()

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
print(list(zip(keys, vals)))

D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D1)
print()

D3 = dict(zip(keys, vals))
print(D3)
print()

D4 = {k : v for (k, v) in zip(keys, vals)}
print(D4)

'''
# Generating Both Offsets and Items: enumerate
S = 'spam'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1
print()

for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
print()

E = enumerate(S)
print(E)
print(next(E))
print(next(E))
print(next(E))
print()

lc = [c * i for (i, c) in enumerate(S)]
print(lc)

path = r'.\resources\text_0426.txt'
myfile = open(path, 'w')
myfile.writelines(['aaaa\n','bbbb\n','cccc\n'])
myfile.close()

for (i, l) in enumerate(open(path,'r')):
    print('%s) %s' % (i, l.rstrip()))