# Set comprehensions
print({x**2 for x in [1, 2, 3, 4]})
print({x**2 for x in [1, 1, 1, 1]})

print({x for x in 'spam'})
print({c * 4 for c in 'spam'})
print({c * 4 for c in 'spamham'})
S = {c * 4 for c in 'spam'}
print(S | {'mmmm', 'xxxx'})
print(S & {'mmmm', 'xxxx'})
print()

# Why sets
# Filter duplicates
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
L = list(set(L))
print(L)
print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))
print()

# Isolate differences
print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
print(set('abcdefg') - set('abdghij'))
print(set('spam') - set(['h', 'a', 'm']))
print(set(dir(bytes)) - set(dir(bytearray)))
print(set(dir(bytearray)) - set(dir(bytes)))
print()

# Order-neutral equaliy
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))
print('spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp'))
print()

# Realistic use-case
engineers = { 'bob', 'sue', 'ann', 'vic'}
managers = { 'tom', 'sue'}
print('bob' in engineers)
print(engineers & managers)
print(engineers | managers)
print(engineers - managers)
print(engineers > managers)
print({ 'bob', 'sue'} < engineers)
print((managers | engineers) > managers)
print(managers ^ engineers)
print((engineers | managers) - (managers ^ engineers))