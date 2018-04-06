# Tuples in action
print((1, 2) + (3, 4))
print((1, 2) * 4)
T = (1, 2, 3, 4)
print(T[0], T[1:3])
print()

# Tuple syntax pecularities
x = (40)
print(x)
y = (40,)
print(y)
print() 

# Conversions, methods, and mutability
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
print(tmp)
T = tuple(tmp)
print(T)

print(sorted(T))
print()

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
print(L)
print()

T = (1, 2, 3, 2, 4, 2)
print(T)
print(T.index(2))
print(T.index(2,2))
#print(dir(tuple))
#print(help(tuple.index))
print(T.count(2))
print()

T = (1, [2, 3], 4)
#T[1] = 'spam'
T[1][0] = 'spam'
print(T)
print()

# Records Revisited: Named Tuples
# As a list
bob = ('Bob', 40.5, ['dev', 'mgr'])
print(bob)
print(bob[0], bob[2])
print()

# As a dict
bob = dict(name='Bob', age=40.5, jobs=['dev','mgr'])
print(bob)
print(bob['name'], bob['jobs'])
print()

# To tuples
print(bob.values())
print(tuple(bob.values()))

print(bob.items())
print(tuple(bob.items()))
print()

# namedtuple
from collections import namedtuple
# Emits a subclass with name equal to first argument
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age='40.5', jobs=['dev', 'mgr'])
print(type(bob))
print(bob)
print(bob[0], bob[2])
print(bob.name,bob.jobs)
print()

O = bob._asdict()
print(O['name'], O['jobs'])
print(O)
print()

# Unpacking tuples
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
a, b, c = bob
print(a, ',', c)

for x in bob: print(x)
print()

bob = {'name' : 'Bob', 'age' : 40.5, 'jobs' : ['dev', 'mgr']}
print(type(bob.values()))
name, age, jobs = bob.values()
print(name, jobs)

for k in bob: print(bob[k])
for v in bob.values(): print(v)