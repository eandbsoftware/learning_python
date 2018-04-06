# Assignment Creates References, Not Copies
L = [1, 2, 3]
M = ['X', L, 'Y']
print(M)
L[1] = 0
print(M)
print()

L = [1, 2, 3]
M = ['X', L[:], 'Y']
print(M)
L[1] = 0
print(L)
print(M)
print()

# Repetition Adds One Level Deep
L = [4, 5, 6]
X = L * 4
print(X)
Y = [L] * 4
print(Y)
print()

L[1] = 0
print(X)
print(Y)
print()

# Embed a shared copy of L
L = [4, 5, 6]
Y = [list(L)] * 4
print(Y)

L[1] = 0
print(Y)

Y[0][1] = 99
print(Y)
print()

# Ensure all copies are unique
L = [4, 5, 6]
Y = [list(L) for i in range(4)]
Y[0][1] = 99
print(Y)
print()

# Beware of Cyclic Data Structures
L = ['grail']
L.append(L)
print(L)
print()

# Immutable Types Can't Be Changed in Place
T = (1, 2, 3)
#T[2] = 4
T = T[:2] + (4,)
print(T)