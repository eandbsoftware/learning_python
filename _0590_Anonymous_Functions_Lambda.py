# lambda basics
def func(x, y, z):
    return x + y + z
print(func(2, 3, 4))

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

x = lambda a='fee', b='fie', c='ffoe': a + b + c
print(x('wee'))

def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x
    return action
act = knights()
msg = act('robin')
print(msg)
print()

# Why Use lambda
L = [lambda x: x **2,
    lambda x: x ** 3,
    lambda x: x ** 4    
]

for f in L:
    print(f(2))
print(L[0](3))
print()

def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4
L = [f1, f2, f3]
for f in L:
    print(f(2))
print(L[0](3))
print()

# Multiway branch switches
key = 'got'
result = {
    'already' : (lambda: 2 + 2),
    'got' : (lambda: 2 * 4),
    'one' : (lambda: 2 ** 6)
}[key]()
print(result)

def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6
key = 'one'
result = {
    'already': f1,
    'got': f2,
    'one' : f3
}[key]()
print(result)
print()

# How not to Obfuscate Your Python Code
# Printing in lambda
printMe = lambda x: print(x)
printMe('jason')
import sys
printMe = lambda x: sys.stdout.write(x + '\n')
printMe('zoe')
print()

# Selection logic in lambda
lower = lambda x, y: x if x < y else y
print(lower('bb', 'aa'))
print(lower('aa', 'bb'))
print()

# Loops in lambda
showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
print(type(t))
print()

bsof = ('bright\n', 'side\n', 'of\n', 'life\n')

showall = lambda z: [sys.stdout.write(line) for line in z]
t = showall(bsof)
print()

showall = lambda y: [print(line, end='') for line in y]
t = showall(bsof)
print()

showall = lambda m: print(*m, sep='', end='')
t = showall(bsof)
print()

# Scopes: lambdas Can Be Nested Too
def action(x):
    return lambda y: x + y
act = action(99)
print(act)
print(act(2))
print()

action = lambda x: lambda y: x + y
act = action(99)
print(act(3))

print(((lambda x: lambda y: x + y)(99))(4))
