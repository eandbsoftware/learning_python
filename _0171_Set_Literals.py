X = set([1, 2, 3, 4])
Y = {1, 2, 3, 4}
print(X == Y)
print()

# Using built-in constructor
print(set([1, 2, 3, 4]))
print(set('spam'))
print()

# New set literals
print({1, 2, 3, 4})
S = {'s', 'p', 'a', 'm'}
print(S)
S.add('alot')
print(S)
print()

# Set expressions work the same
S1 = {1, 2, 3, 4}
print(S1 & {1, 3})
print({1, 5, 3, 6} | S1)
print(S1 - {1, 3, 4})
print(S1 > {1, 3})
print()

# Empty sets must be defined with constructor
print(S1 - {1, 2, 3, 4})
print(type({}))
S = set()
S.add(1.23)
print(S)
print()

# Sets created with literals support the same methods (which allow iterable operands)
print({1, 2, 3} | {3, 4})
#print({1, 2, 3} | [3, 4])
print({1, 2, 3}.union({3, 4}))
print({1, 2, 3}.union(set([3, 4])))
print({1, 2, 3}.union([3, 4]))
print({1, 2, 3}.intersection([1, 3, 5]))
print({1, 2, 3}.issubset(range(-5, 5)))
print()

# Immutable constraints and frozen sets
print(S)
#S.add([1, 2, 3])
#S.add({'a' : 1})
S.add((1, 2, 3))
print(S)
print(S | {(1, 2, 3), (4, 5, 6)})
print((1, 2, 3) in S)
print((1, 4, 3)  in S)

S3 = {'jason'}
#S3.add(S)
frozen = frozenset([1, 2, 3])
print(frozen)
S3.add(frozen)
print(S3)
