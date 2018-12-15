class StepperIndex:
    # __getitem__ provides support for ALL iteration contexts
    def __getitem__(self,i):
        return self.data[i]

X = StepperIndex()
X.data = 'Spam'

# Indexing
print(X[1])

# for loop iteration
for i in X:
    print(i, end=' ')

# in membership test
print('p' in X)

# list comprehension
print([c for c in X])

# map builtin
print(list(map(str.upper, X)))

# Sequence assignments
a, b, c, d = X
print(a, c, d)

# Sequence constructors
print(list(X), tuple(X), ''.join(X))