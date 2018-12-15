# Slicing and Indexing in Python 2.X
class Slicer:
    def __getitem__(self, index):
        print('__getitem__', index)
    def __getslice__(self, i, j):
        print('__getslice__', i, j)
    def __setslice__(self, i, j, value):
        print('__setslice__', i, j, value)

print(Slicer()[1])
print(Slicer()[1:9])
print(Slicer()[1:9:2])
print()

class C:
    def __index__(self):
        return 255

X = C()
print(hex(X))
print(bin(X))
print(oct(X))
print(('C'*256)[255])
print(('C'*256)[X])
print(('C'*256)[X:])