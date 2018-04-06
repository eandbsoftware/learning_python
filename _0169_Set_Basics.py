x = set('abcde')
y = set('bdxyz')
print(x)

# Set expression operators
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)
print(x > y, y > x)
print('e' in x)
print('e' in 'Camelot', 22 in [11, 22, 33])
print()

# Set method calls
z = x.intersection(y)
print(z)
z.add('spam')
print(z)
z.update(set(['X', 'Y']))
print(z)
z.remove('b')
print(z)
print()

# Sets are iterable but not sequences
for item in set('abc'):
    print(item * 3)
print()

# Expression operators require both arguments to be sets
S = set([1, 2, 3])
print(S | set([3, 4]))
# print(S | [3, 4])
# But methods work with set and iterable
print(S.union([3, 4]))
print(S.intersection([1, 3, 5]))
print(S.issubset(range(-5, 5)))
