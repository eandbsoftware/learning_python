# Arguments and shared references
def f(a):
    a = 99
b = 88
f(b)
print(b)
print()

def changer(a, b):
    a = 2
    b[0] = 'spam'
X = 1
L = [1, 2]
changer(X, L)
print(X, L)
print()

X = 1
a = X
a = 2
print(X)
print()

L = [1, 2]
b = L
b[0] = 'spam'
print(L)
print()

# Avoiding Mutable Argument Changes
# Don't impact the caller 
L = [1, 2]
changer(X, L[:])
print(L)
print()

# Don't allow object to be changed at all
# Throws a TypeError because 'tuple' object does not support item assignment
#changer(X, tuple(L))

# Simulating Output Parameters and Multiple Results
def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y

X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X, L)
print()