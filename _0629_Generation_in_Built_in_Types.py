# Iteration contexts accept any iterable, user-defined or built-in
D = {'a' : 1, 'b' : 2, 'c' : 3}
x = iter(D)
print(next(x))
print(next(x))
print()

for key in D:
    print(key, D[key])
print()


path = r'.\resources\temp_0629.txt'

'''
f = open(path,'w')
f.writelines(['Tis but\n', 'a flesh wound\n'])
f.close()
'''

for line in open(path,'r'):
    print(line, end='')
print()

# Generators and library tools: directory walkers
import os
for (root, subs, files) in os.walk('.'):
    for name in files:
        print('root=', root, 'name=', name)
print()

G = os.walk(r'C:\_Gastelum\Development')
print(iter(G) is G)
I = iter(G)
print(next(I))
print()
print(next(I))
print()

# Geneartors and function application
def f(a, b, c):
    print("%s, %s, and %s" % (a, b, c))

f(0, 1, 2)
f(*range(3))
f(*(i for i in range(3)))
print()

D = dict(a='Bob', b='dev', c=40.5)
f(a='Bob', b='dev', c=40.5)
# Unpack dict: key=value
f(**D)
# Unpack keys iterator
f(*D)
f(*D.values())
print()

for x in 'spam':
    print(x.upper(), end=' ')
print()
list(print(x.upper(), end=' ') for x in 'spam')
print()
print(*(x.upper() for x in 'spam'))