'''
# Examples
while True:
    print('Type Ctrl-C to stop me!')

x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
print()

a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1
print()

# Pass ane ellipses
while True: pass
while True: ...
print('Never gets here!')

def func1(): pass
def func1(): ...
print('done')

# continue
x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x, end=' ')
print()

# break
while True:
    name = input('Enter name: ')
    if name == 'stop':
        break
    age = input('Enter age: ')
    print(' Hello', name, '=>', int(age)**2)
'''

# Loop else
y = 27
x = y // 2
while x > 1:
    print('trying factor', x)
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')
