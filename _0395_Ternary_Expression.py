'''
if X:
    A = Y
else:
    A = Z

A = X ? Y : Z

'''

# Ternary operator
# A = Y if X else Z
A = 't' if 'spam' else 'f'
print(A)
A = 't' if '' else 'f'
print(A)
print()

# Using and/or operators
# A = ((X and Y) or Z)
# Y must evaluate to Boolean true (necessary for first case)
A = (('spam' and 't') or 'f' )
print(A)
A = (('' and 't') or 'f')
print(A)
print()

# Using bool and indexing
# A = [Z, Y][bool(X)]
# Does not short-circut
A = ['f', 't'][bool('spam')]
print(A)
A = ['f', 't'][bool('')]
print(A)
print()

# Why You Will Care: Booleans

# Assign X to the first non-empty object
# X = A or B or C or None
X = 0 or {} or 69 or None
print(X)

Y = []
Default = 5
X = Y or Default
print(X)
print()

# Similar to or chains
L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))
print([x for x in L if x])
print(any(L), all(L))