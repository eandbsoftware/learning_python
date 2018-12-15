class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[2])

for i in range(5):
    print(X[i], end=' ')
print()

# Intercepting Slices
L = [5, 6, 7, 8, 9]
print(L[2:4])
print(L[1:])
print(L[:-1])
print(L[::2])
print()

print(L[slice(2, 4)])
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)])
print()

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer()
print(X[0])
print(X[1])
print(X[-1])
print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])
print()

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

X = Indexer()
print(X[99])
print(X[1:99:2])
print(X[1:])
print()

class IndexSetter:
    data = [5, 6, 7, 8, 9]
    def __setitem__(self, index, value):
        print('setting', index)
        self.data[index] = value

Y = IndexSetter()
Y[1] = 99
print(Y.data)
Y[2:3] = ['fast', 'neat', 'average']
print(Y.data)
print()