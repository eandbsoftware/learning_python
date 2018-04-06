L = [123, 'spam', 1.23]

# Sequence operations
print(len(L))
print(L[0])
print(L[:-1])

# + is overloaded to concatenate lists
print(L + [4, 5, 6])

# * is overloaded to repeat lists
print(L * 2)

# Sequence operations emit a new list
print(L)

# Type-specific operations change a list in place
L.append('NI')
print(L)

print(L.pop(2))
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

M.insert(1, 'dd')
M.remove('aa')
M.extend(['ff', 'gg'])
print(M)

# Bounds checking
# Cannot index off of the list
#print(L[99])
# Or assign off the end of the list
#L[99] = 1

# Nesting
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M)
print(M[1])
print(M[1][2])

# Comprehensions - run an expression for each item in a sequence
# Get the second column of M
col2 = [row[1] for row in M]
print(col2)

col2plus = [row[1]+1 for row in M]
print(col2plus)

# Get only even items from the second column of M
even = [row[1] for row in M if row[1] % 2 == 0]
print(even)

# Get the diagonal of M
diag = [M[i][i] for i in [0,1,2]]
print(diag)

# Repeat letters in a word
repeat = [c*2 for c in 'spam']
print(repeat)

# In 3.X, must wrap range in list to display its values
print(list(range(4)))
print(list(range(-6,7,2)))

# Squares and cubes
powers = [[x**2, x**3] for x in range(4)]
print(powers)

multiples = [[x, x/2, x*2] for x in range(-6, 7, 2) if x > 0]
print(multiples)

# Generator - deferred execution like an enumerable in C#
G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum,M)))

# Use comprehension syntax to create a set...
mySet = {sum(row) for row in M}
print(mySet)

# or a dictionary
myDict = {i: sum(M[i]) for i in range(3)}
print(myDict)

# Lists, sets, dictionaries, and generators can all be build with comprehension syntax
listComp = [ord(x) for x in 'spaam']
setComp = {ord(x) for x in 'spaam'}
dictComp = {x : ord(x) for x in 'spaam'}
genComp = (ord(x) for x in 'spaam')
print(listComp)
print(setComp)
print(dictComp)
print(genComp)
