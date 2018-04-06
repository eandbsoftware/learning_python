# Basic list operations
print(len([1, 2, 3]))           # Length
print([1, 2, 3] + [4, 5, 6])    # Concatenation
print(['Ni!'] * 4)              # Repitition

print(str([1, 2]) + '34')
print([1, 2] + list('34'))
print(list('jason'))
print()

# List iterations and comprehensions
print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x, end=' ')
print()

res = [c * 4 for c in 'SPAM']
print(res)

res = []
for c in 'SPAM':
    res.append(c * 4)
print(res)

print(list(map(abs,[-1, -2, 0, 1, 2])))
print()

# Indexing, Slicing, and Matrices
L = ['spam', 'Spam', 'SPAM']
print(L[2])
print(L[-2])
print(L[1:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][1])
print()

# Changing lists in place
L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'
print(L)
L[0:2] = ['eat', 'more']
print(L)

L = [31, 38]     
print(L[1:2])   # Exceeding the upper bound of the iterable does not throw an exception
L[1:2] = [4, 5]
print(L)
print()

L = [1, 2, 3]
L[1:2] = [4, 5]     # Replacement/insertion
print(L)
L[1:1] = [6, 7]     # Insertion (replace nothing)
print(L)
L[1:2] = []         # Deletion (insert nothing)
print(L)

print()
L = [1]
L[:0] = [2, 3, 4]
print(L)
L[len(L):] = [5, 6, 7]
print(L)
L.extend([8, 9, 10])
print(L)