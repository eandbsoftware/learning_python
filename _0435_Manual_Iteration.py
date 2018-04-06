# next(X) and X.__next__() 
path = r'.\resources\script2_0433.py'

f = open(path,'r')
print(repr(f.__next__()))
print(repr(f.__next__()))
f.close()
print()

f = open(path,'r')
print(repr(next(f)))
print(repr(next(f)))
f.close()
print()

L = [1, 2, 3]
#I = iter(L)
I = L.__iter__()
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
#print(I.__next__())
print()

# A file object is its own iterator
f = open(path,'r')
print(iter(f) is f)
print(iter(f) is f.__iter__())
print(repr(f.__next__()))
f.close()
print()

# Lists are NOT their own iterators
L = [1, 2, 3]
print(iter(L) is L)
#print(L.__next__())
I = iter(L)
print(I.__next__())
print(next(I))
print()

# Manual iteration
L = [1, 2, 3]
for X in L:
    print(X ** 2, end=' ')
print()

I = L.__iter__()
while True:
    try:
        X = I.__next__()
    except StopIteration:
        break
    print(X ** 2, end=' ')    
