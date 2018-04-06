L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print((L1 == L2, L1 is L2))
print()

S1 = 'spam'
S2 = 'spam'
print((S1 == S2, S1 is S2))
S1 = 'a much much much much much much much much much much much much longer string'
S2 = 'a much much much much much much much much much much much much longer string'
# Different result than in the book!!!
print((S1 == S2, S1 is S2))
print()

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print((L1 < L2, L1 == L2, L1 > L2))
print()

# Python 3.X mixed-type comparisons
print(11 == '11')
# Mixed-type comparisons throws an exception in 3.X
#print(11 >= '11')
print(11 > 9.123)
print((str(11) >= '11', 11 >= int('11')))
print()

# Python 3.X dictionary comparisons
D1 = {'a' : 1, 'b' : 2}
D2 = {'a' : 1, 'b' : 3}
print(D1 == D2)
# Dictionary magnatude comparisons throw and exception is 3.X
#print(D1 < D2)
print()

print(D1.items())
print(list(D1.items()))
print(sorted(D1.items()))
print(sorted(D1.items()) < sorted(D2.items()))
print(sorted(D1.items()) > sorted(D2.items()))
print()

# The Meaning of True and False
print(0 == False)
print(1 == True)
print()

if 'spam':
    print('it works like this...')
print()

if 'spam' == True:
    print('not like this')

print(bool('spam'))
print(bool(''))

print(bool([1, 2]))
print(bool([]))

print(bool({'a' : 1}))
print(bool({}))

print(bool(1))
print(bool(0.0))
print(bool(None))
print()

# The None object
L = [None] * 10
print(L)
print()

# The bool type
print(bool(1))
print(bool('spam'))
print(bool({}))
print()

if 5:
    print('non zero value')
if [1, 2]:
    print('stuff in the list')
if {}:
    print('empty dict')