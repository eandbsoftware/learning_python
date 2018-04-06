# Generator is its own iterator
G = (c * 4 for c in 'SPAM')
print(iter(G) is G)
print()

# All iterators point to the same position
I1 = iter(G)
print(next(I1))
print(next(I1))
I2 = iter(G)
print(next(I2))
print()

# Once any iterator runs to completion, all are exhausted
print(list(I1))
#print(next(I2))

I3 = iter(G)
#print(next(I3))

I3 = (c * 4 for c in 'SPAM')
print(next(I3))
print()

# Same for generator functions
def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('spam')
print(iter(G) is G)

I1, I2 = iter(G), iter(G)
print(next(I1))
print(next(I1))
print(next(I2))
print()

# Different than some built-in types
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print(next(I1))
print(next(I1))
print(next(I2))
del(L[2:])
print(next(I2))
print(next(I1))