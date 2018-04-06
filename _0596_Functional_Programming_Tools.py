# Maping Functions over Iterables: map
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)
print(updated)

def inc(x): return x + 10
print(list(map(inc, counters)))
print(list(map(lambda x: x + 10, counters)))
print()

def mymap(func, seq):
    result = []
    for x in seq:
        result.append(func(x))
    return result

print(list(map(inc, [1, 2, 3])))
print(mymap(inc, [1, 2, 3]))
print()

print(pow(3, 4))
print(list(map(pow, [1, 2, 3], [2, 3, 4])))
print()

print(list(map(inc, [1, 2, 3, 4])))
print([inc(x) for x in [1, 2, 3, 4]])
print()

# Selecting Items in Iterables: filter
print(list(range(-5, 5)))
print(list(filter(lambda x: x > 0, range(-5, 5))))

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)
print(res)

print([x for x in range(-5, 5) if x > 0])
print()

# Combining Items in Iterables: reduce
from functools import reduce
print(reduce(lambda sum, next: sum + next, [1, 2, 3, 4]))
print(reduce(lambda prod, next: prod * next, [1, 2, 3, 4]))

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res += x
print(res)
print()

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
print()

# Using optional seed (for non-commutative, non-associative functions)
# f(f(f(0, 2), 3), 4) = 2 * 2 + 3 * 3 + 4 * 4 = 29
print(reduce(lambda x, y: x + y * y, [2, 3, 4], 0))
# f(f(2, 3), 4) = 2 + 3 * 3 + 4 * 4 = 27
print(reduce(lambda x, y: x + y * y, [2, 3, 4]))
print()

import operator, functools
print(functools.reduce(operator.add, [2, 4, 6]))
print(functools.reduce(lambda x, y: x + y, [2, 4, 6]))
