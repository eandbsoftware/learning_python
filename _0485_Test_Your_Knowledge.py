'''
# PROBLEM 1
# a.
S = 'jason'
for c in S:
    print(ord(c))
print()

# b.
total = 0
for c in S:
    total += ord(c)
print('total=', total)
print()

# c.
codepoints = []
for c in S:
    codepoints.append(ord(c))
print(codepoints)

print(list(map(ord,S)))
print([ord(c) for c in S])


# PROBLEM 2
for i in range(50):
    print('hello %d\n\a' % i)


# PROBLEM 3
ages = dict(jason=38, zoe=32, holden=0, hayden=3)
# Could use sorted(D) also because dict iterator yields keys
for k in sorted(ages.keys()):
    print(k, ages[k])

'''
# PROBLEM 4
L = [1, 2, 4, 8, 16, 32, 64]
X = 15

found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
         i = i + 1
if found:
    print('at index', i)
else:
    print(X, 'not found')         

# a.
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
# The normal (i.e., non-breaking) way out of the loop
else:
    print(X, 'not found')

# b.
for x in L:
    if 2 ** X == x:
        print('at index', L.index(x))
        break
else:
    print(X, 'not found')

# c.
if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')

# d.
powers = []
for x in range(7):
    powers.append(2 ** x)
print(powers)

# e.
target = 2 ** X
for x in L:
    if target == x:
        print('at index', L.index(x))
        break
else:
    print(X, 'not found')

# f.
powers = map(lambda x: 2 ** x, range(7))
print(list(powers))

