D = {'a' : 1, 'b' : 2, 'c' : 3}
for key in D.keys():
    print(key, D[key])
print()

# Dictionaries are iterable (i.e., return an iterator with iter())
I = iter(D)
print(next(I))
print(next(I))
print(next(I))
#print(next(I))
print()

# Use a for loop with a dict
for k in D:
    print(k, D[k])
print()

# os.popen is iterable
import os
P = os.popen('dir')
print(repr(P.__next__()))
print(repr(P.__next__()))
# Must employ the full iteration protocol 
# (i.e., by calling iter(P)) for next(P) to work
#print(next(P))
print()

P = os.popen('dir')
I = iter(P)
print(repr(next(I)))
print(repr(next(I)))
print()

# range returns an iterable
R = range(5)
print(R)
I = iter(R)
print(next(I))
print(next(I))
print(list(R))
print()

# enumerate returns an iterable
E = enumerate('spam')
print(E)
I = iter(E)
print(next(I))
print(I.__next__())
print(list(E))
