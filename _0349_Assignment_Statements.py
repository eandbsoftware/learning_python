# Assignment Statement Forms
'''spam = 'spam'
spam, ham = 'yum', 'YUM'
print(spam, ham)
[spam, ham] = ['jason', 'zoe']
print(spam, ham)
a, b, c, d = 'spam'
print(a, d)
a, *b = 'spam'
print(a, b)
spam = ham = 'lunch'
print(spam == ham)
spams = 0
spams += 42
print(spams)

# Sequence Assignments
nudge = 1
wink = 2
# Tuple assignment
A, B = nudge, wink  
print(A, B)
# Same as
T = (nudge, wink)
A, B = T
print(A, B)

A, B = nudge, A
print(A, B)

# List assignment
[C, D] = [nudge, wink]
print(C, D)
print()

# Swapping variables
nudge = 1
wink = 2
nudge, wink = wink, nudge
print(nudge, wink)
print()

# Assign tuple of values to list of names
[a, b, c] = (1, 2, 3)
print(a, c)
# Assign string of characters to tuple
(a, b, c) = "ABC"
print(a, c)

# Advanced sequence assignment patterns
string = "SPAM"
a, b, c, d = string
print(a, d)

# ValueError: too many values to unpack
#a, b, c = string

a, b, c = string[0], string[1], string[2:]
print(a, b, c)
a, b, c = list(string[:2]) + [string[2:]]
print(a, b, c)
a, b = string[:2]
c = string[2:]
print(a, b, c)

# Assigning nested sequences
(a, b), c = string[:2], string[2:]
print(a, b, c)

# Equivalent to
((a, b), c) = ("SP", "AM")
print(a, b, c)
print()

# Using in for loops
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

for((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
print()

# Assigning an integer series to a set of variables
red, green, blue = range(3)
print(red, green, blue)
print()

# Splitting a sequence into its front and the rest
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

# Extended Sequence Unpacking in Python 3.X
# Extended upacking in action
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
print()
# ValueError: too many values to unpack
#a, b = seq

a, *b = seq
print(a)
print(b)
print()

*a, b = seq
print(a)
print(b)
print()

a, *b, c = seq
print(a)
print(b)
print(c)
print()

a, b, *c = seq
print(a)
print(b)
print(c)
print()

a, *b = 'spam'
print(a, b)

a, *b, c = 'spam'
print(a, b, c)

a, *b, c = range(4)
print(a, b, c)
print()

S = 'spam'
print(S[0], S[1:])
print(S[0], S[1:-1], S[-1])
print()

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

# Boundary cases
seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)

a, b, c, d, *e = seq
print(a, b, c, d, e)

a, b, *e, c, d = seq
print(a, b, e, c, d)

# SyntaxError
#a, *b, c, *d = seq

# ValueError
#a, b = seq

# SyntaxError
#a* = seq

*a, = seq
print(a)
print()

# A useful convenience 
# first-rest pattern
seq = [1, 2, 3, 4]
a, *b = seq
print(a, b)

a, b = seq[0], seq[1:]
print(a, b)
print()

#rest-last pattern
*a, b = seq
print(a, b)

a, b = seq[:-1], seq[-1]
print(a, b)

'''
# Application to for loops
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
print()

for four in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = four[0], four[1:-1], four[-1] 
    print(a, b, c)

