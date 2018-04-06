# In Python 2.X, it's possible to automatically unpack tuples in arguments passed to a function
def f((a, (b, c))):
    print('a =', a, ' b=', b,'c =', c)

f((1, ('a', 'b')))
# Can also be called with a tuple object created before the call

# Arbitrary sequences in the call successfully match tuples in the header
f((2, ['x', 'y']))

# Python 2.X supports only the tuple form of sequence assignment;
# more general sequence assignments fail
def g((a, [b, c])):
    print('a =', a, ' b=', b,'c =', c)

# The def syntax below is no longer supported in Python 3.X
#def f((a, (b, c))):
#    print(a, b, c)

# Use an explicit assignment statement instead
T = (1, (2, 3))
def f(T):
    (a, (b, c)) = T
    print('a =', a, ' b=', b,'c =', c)
f(T)
