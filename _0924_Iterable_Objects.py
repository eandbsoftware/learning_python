# User-Defined Iterables
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i, end=' ')
print()

X = Squares(1, 5)
I = iter(X)
print(next(I))
print(next(I))
# Since iterator is self this works too!
print(next(X))
print(next(I))
print(next(I))
# Must catch StopIteration exception
#print(next(I))
print()

X = Squares(1, 5)
# Implementing __iter__ only supports iteration, not indexing
#print(X[1])
print(list(X)[1])
print()

class GetItemSquare:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __getitem__(self, i):
        # Not natural, but it works for iteration AND random indexing.
        if i + self.start > self.stop:
            raise StopIteration
        return (i + self.start) ** 2

Y = GetItemSquare(1, 5)
for y in Y:
    print(y, end=' ')
print()

Y = GetItemSquare(1, 5)
print(Y[1])
print()

# Single versus multiple scans
X = Squares(1, 5)
print([n for n in X])
print([n for n in X])
# Need a new iterator once exhausted!
print([n for n in Squares(1, 5)])
print(list(Squares(1, 5)))
print(36 in Squares(1, 10))
a, b, c = Squares(1, 3)
print(a, b, c)
print(':'.join(map(str, Squares(1,5))))
print()

# Converting to a list supports multiple scans
X = Squares(1, 5)
print(tuple(X), tuple(X))
X = list(Squares(1, 5))
print(tuple(X), tuple(X))
print()

# Classes versus generators
def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i**2

for i in gsquares(1, 5):
    print(i, end=' ')
print()

for i in (x**2 for x in range(1, 6)):
    print(i, end=' ')
print()

print([x**2 for x in range(1, 6)])

