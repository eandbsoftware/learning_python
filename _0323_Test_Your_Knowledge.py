# PROBLEM 1
'''
print(2**16)

# In Python 3.X you always get true division
print(2 / 5, 2 / 5.0)

print("spam" + "eggs")
S = "ham"
print("eggs " + S)   # eggsham
print(S * 5)        # hamhamhamhamham
# Returns an empty of same type as sliced
print(S[:0])
print(type(S[:0]))       
print("green %s and %s" % ("eggs", S))  # green eggs and ham
print('green {0} and {1}'.format('eggs', S))
print()

print(('x',)[0])        # x
print(('x', 'y')[1])    # y
L = [1, 2, 3] + [4, 5, 6]
print((L, L[:], L[:0], L[-2], L[-2:]))  # ([1..6], [1..6], ,[] ,5,[5, 6])
# No trailing comma, so not a tuple
print(([1, 2, 3] + [4, 5, 6])[2:4])     #[3, 4]
print([L[2], L[3]])     # [3, 4]
L.reverse(); print(L)
L.sort(); print(L)
print(L.index(4))       # 3
print()

print({'a' : 1, 'b' : 2}['b'])  # 2
D = {'x' : 1, 'y' : 2, 'z' : 3}
D['w'] = 0
print(D['x'] + D['w'])      # 1
D[(1, 2, 3)] = 4
print((list(D.keys()), list(D.values()), (1, 2, 3) in D))
print(([[]],["", [], (), {}, None]))

# PROBLEM 2
L = [0, 1, 2, 3]
# Indexing out of bounds throws an exception
#print(L[4])

# Slicing out of bounds does not throw an exception
# Effectively reassignes your slice arguemnts (to zero or length of the sequence)
print(L[-1000:100])
print(L[10:100])
print(L[1:100])

# Trying to extract in reverse with lb > ub doesn't work. (Must use thrid, negative argument.)
# In this case, Python scales the upper slice limit to ensure that the lb <= ub, thus L[3:1] is scaled to L[3:3]
print(L[3:1])
L[3:1] = ['?']
print(L)

# PROBLEM 3
L = [0, 1, [], 3]
print(L)

# Assigning to a slice deletes the slice and repalces it with the contents of the sequence, not the sequence itself
L[2:3] = []
print(L)

del L[0]
print(L)

# Cannot delete a slice
del L[1:2]
print(L)

# Cannot assign a scalar to a slice
#L[1:2] = 1

L = [0, 1, 2, 3]
L[2:2] = [98]
L[2:3] = [99]
print(L)

# PROBLEM 4
X = 'spam'
Y = 'eggs'
T = Y, X
X, Y = T
# Tuple assignment
#X, Y = Y, X
print(X)
print(Y)

# PROBLEM 5
# Integers used as keys, not accessing by offset
D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)

# PROBLEM 6
D = dict(a=1, b=2, c=3)
#print(D['d'])
D['d'] = 'spam'
print(D)

# PROBLEM 7
# a: Exceptions. Cannot concatenate mixed types
#'string' + [1, 2]
#[1, 2] + (1, 2)
# b: + does not work on dictionaries because they are not sequences
#{} + {}
# c: append is a method on lists, not strings; keys is a method on dictionaries, not lists
[].append(9)
#"".append('s')
# d: slicing and concatenation yields the type that was operated on

# PROBLEM 8
S = 'spam'
print(S[0][0][0][0][0])
L = list(S)
print(L)
# Generally doesn't work for lists (lists can hold arbitrary objects) unless the list contains strings
print(S[0][0][0][0][0])

# PROBLEM 9
# Slicing and concatenation
S = "spam"
S = S[0:1] + 'l' + S[2:]
print(S)
# Indexing and concatenation
S = "spam"
S = S[0] + 'l' + S[2] + S[3]
print(S)
# Index assignment
# Can't do it with index assignment because strings are immutable

# PROBLEM 10
Record = {}
Name = dict(first='Jason', middle='Adam', last='Gastelum')
Record['name'] = Name
Record['age'] = 38
Record['job'] = 'Data Scientist'
Address = dict(number=1335, street='Valle', city='Albuquerque', state='NM')
Record['address'] = Address
Record['phone'] = 8991452
print(Record['name']['last'])
print(Record['age'])
print(Record['address']['city'])

# PROBLEM 11
path = r''
path = 'problem11.txt'
myfile = open(path, 'w')
myfile.write('hello world')
myfile.close()

myfile = open(path)
print(myfile.read())
'''

