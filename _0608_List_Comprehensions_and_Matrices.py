M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1])
print(M[1][2])
print()

# Column
col = [row[1] for row in M]
print(col)

col = [M[row][1] for row in (0, 1, 2)]
print(col)
print()

# Diagonal
diag = [M[i][i] for i in range(len(M))]
print(diag)

diag = [M[i][len(M) - 1 - i] for i in range(len(M))]
print(diag)
print()

# Changing in Place
L = [[1, 2, 3],
     [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] += 10
print(L)
print()

res = [e + 10 for row in M for e in row]
print(res)

res = [[e + 10 for e in row] for row in M]
print(res)
print()

res = []
for row in M:
    for e in row:
        res.append(e + 10)
print(res)

res = []
for row in M:
    tmp = []
    for e in row:
        tmp.append(e + 10)
    res.append(tmp)
print(res)
print()

# Combine values from multiple matrices
res = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(res)
res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(res)

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)
print(res)

res = []
for (rowM, rowN) in zip(M, N):
    tmp = []
    for (elemM, elemN) in zip(rowM, rowN):
        tmp.append(elemM * elemN)
    res.append(tmp)
print(res)