# Dictionary comprehensions
Z = list(zip(['a', 'b', 'c'],[1, 2, 3]))
print(Z)
D = dict(Z)
print(D)

D = {k : v for (k,v) in zip(['a', 'b', 'c'],[1, 2, 3])}
print(D)
print()

D = {x: x**2 for x in [1, 2, 3, 4]}
print(D)
D = {c:c*4 for c in 'SPAM'}
print(D)
D = {c.lower() : c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
print()

D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)
D = {k : 0 for k in ['a', 'b', 'c']}
print(D)
print()

D = dict.fromkeys('spam')
print(D)
D = {k : None for k in 'spam'}
print(D)
print()

# Dictionary views in 3.X
D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()
print(K)
print(list(K))

V = D.values()
print(V)
print(list(V))

I = D.items()
print(I)
print(list(I))

#print(K[0])
print(list(K)[0])
print()

for k in D.keys():
    print(k, end='')
print()

for k in D:
    print(k,end='')
print()

D = {'a' : 1, 'b' : 2, 'c' : 3}
K = D.keys()
V = D.values()
print(list(K))
print(list(V))
del D['b']
print(list(K))
print(list(V))
print()

# Dictionary views and sets
print(K, V)
print(K | {'x' : 4})
#print(V & {'x' : 4})
print()

D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D.keys() & D.keys())
print(D.keys() & {'b'})
print(D.keys() & {'b' : 1})
print(D.keys() | {'b', 'c', 'd'})
print()

D = {'a' : 1}
print(list(D.items()))
print(D.items() | D.keys())
print(D.items() | D)
print(D.items() | {('c', 3), ('d', 4)})
print(dict(D.items() | {('c', 3), ('d', 4)}))
print()

# Sorting ditionary keys in 3.X
D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D)
Ks = D.keys()
#Ks.sort()
print()

# Convert to list manually
Ks = list(D.keys())
Ks.sort()
for k in Ks:
    print(k, D[k], end=', ')
print()
# Use sorted call. Views (and dictionaries) are iterable but not sequences
Ks = D.keys()
for k in sorted(Ks):
    print(k, D[k], end=', ')
print()

# Use dictionary's keys iterator. Dictionary's iterator returns keys.
for k in sorted(D):
    print(k, D[k], end=', ')
print(); print()

# Membership - us in keyword
print(D)
#print(D.has_key())

print('c' in D)
print('x' in D)
if 'c' in D:
    print('present', D['c'])
print()

print(D.get('c'))
print(D.get('x'))
print(D.get('x', 0))
if D.get('c') != None:
    print('present', D['c'])
print()

# Why you will care
import dbm
file = dbm.open(r'.\resources\mydbmdb','n')
file['key'] = 'data'
data = file['key']
print(data)
