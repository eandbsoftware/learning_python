def gen(x):
    for i in range(x):
        yield i**2

# Generator has __iter__ and __next__
G = gen(5)
# gen.__iter__ returns itself
print(G.__iter__() == G)
I = iter(G)
# Can call next on gen or iter(gen)
print(next(G), next(I), next(I))
print(list(gen(5)))
print()

class SquaresYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for i in range(self.start, self.stop + 1):
            yield i**2

for i in SquaresYield(1, 5):
    print(i, end=' ')
print()

S = SquaresYield(1, 5)
print(S)
I = iter(S)
print(I)
print(I == iter(I))
#print(next(I)); print(next(I));print(next(I));print(next(I));print(next(I));print(next(I))
print()

class ManualSquares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def gen(self):
        for i in range(self.start, self.stop + 1):
            yield i**2

# I can only iterate over an object that has an __iter__ method!
for i in ManualSquares(1,5).gen():
    print(i, end=' ')
print()

S = ManualSquares(1, 5)
I = iter(S.gen())
print(next(I))
print(S.gen().__next__())
print()

# Multiple iterators with yield
S = SquaresYield(1, 5)
I = iter(S)
print(next(I), next(I))
J = iter(S)
print(next(J))
print(next(I))
print()

S = SquaresYield(1, 3)
for i in S:
    for j in S:
        print('%s:%s' % (i, j), end=' ')
print(); print()

# Do the same without yield (takes a lot more code)
class SquaresNonYield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value**2

for i in SquaresNonYield(1, 5):
    print(i, end=' ')
print()

S = SquaresNonYield(1, 5)
I = iter(S)
print(next(I), next(I))
J = iter(S)
print(next(J))
print(next(I))
print()

S = SquaresNonYield(1, 3)
for i in S:
    for j in S:
        print('%s:%s' % (i, j), end= ' ')
print(); print()

class SkipperYield:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        offset = 0
        while offset <= len(self.wrapped):
            yield self.wrapped[offset]
            offset += 2
    
    # This won't work because the body is only passed through once
    # def __iter__(self):
    #     offset = 0
    #     if offset <= len(self.wrapped):
    #         yield self.wrapped[offset]
    #         offset += 2

skipper = SkipperYield('abcde')
I = iter(skipper)
print(next(I), next(I), next(I))

for x in skipper:
    for y in skipper:
        print(x + y, end = ' ')
print()