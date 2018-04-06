# Shared references
a = 3
b = a
print(a, b)
a = 'spam'
print(a, b)
print()

# Shared references and In-Place Changes
L1 = [2, 3, 4]
L2 = L1
print(L1, L2)
L1 = 24
print(L1, L2)
print()

L1 = [2, 3, 4]
L2 = L1
print(L1, L2)
L1[0] = 24
print(L1, L2)
print()

L1 = [2, 3, 4]
L2 = L1[:]
print(L1, L2)
L1[0] = 24
print(L1, L2)
print()

# Equality
L = [1, 2, 3]
M = L
# Value equality
print(L == M)
# Reference equality (identity)
print(L is M)
print()

L = [1, 2, 3]
M = [1, 2, 3]
print(L == M)
print(L is M)
print()

X = 42
Y = 42
print(X == Y)
# True because of caching
print(X is Y)
print()

import sys
print(sys.getrefcount(42))
