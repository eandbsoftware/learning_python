# List method calls
L = ['eat', 'more', 'SPAM!']
L.append('please')
print(L)
L.sort()
print(L)
print()

# More on sorting lists
L = ['abc', 'ABD', 'aBe']
L.sort()
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)
print(L)
L = ['seven', 'one', 'four']
L.sort(key=lambda x: len(x))
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)
print(L)
print()

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))
L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], key=str.lower, reverse=True))
print()

# Other common list methods
L = [1, 2]
L.extend([3, 4, 5])
print(L)
print(L.pop())
print(L)
L.reverse()
print(L)
print(list(reversed(L)))
print()

L = []
L.append(1)
L.append(2)
print(L)
print(L.pop())
print(L)
print()

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))
L.insert(1, 'toast')
print(L)
L.remove('eggs')
print(L)
print(L.pop(1))
print(L)
print(L.count('spam'))
print()

# Other common list operations
L = ['spam', 'eggs', 'ham', 'toast']
del L[0]
print(L)
del L[1:]
print(L)

L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)
