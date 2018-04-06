'''
# Multiple-Target Assignments
a = b = c = 'spam'
print(a, b, c)

# Equivalent to:
c = 'spam'
b = c
a = b
print(a, b, c)

# Initializing a non-mutable counter:
a = b = 0
b = b + 1
print(a, b)

# Initializing a mutable list
a = b = []
b.append(42)
print(a, b)

# Initialize mutable objects in seperate statements instead
a = []
b = []
b.append(42)
print(a, b)

# Or use a tuple assignment
a, b = [], []
b.append(42)
print(a, b)
'''

# Augmented Assignments
x = 1
x = x + 1
print(x)
x += 1
print(x)

S = 'spam'
S += 'Spam'
print(S)
print()

L = [1, 2]
L = L + [3]
print(L)
L.append(4)
print(L)

L = L + [5, 6]
print(L)
L.extend([7, 8])
print(L)

# For lists, += mapped to extend
L += [9, 10]
print(L)
print()

L = []
L += 'spam'
print(L)

# For lists += allows arbitrary sequences, but concatenation normally does not
#L = L + 'spam'
print()

# For lists += is an in-place change 
L = [1, 2]
M = L
L = L + [3, 4]
print(L, M)

L = [1, 2]
M = L
L += [3, 4]
print(L, M)