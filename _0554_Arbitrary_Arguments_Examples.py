'''
# Headers: Collecting arguments
def f(*args):
    print(args)
f()
f(1)
f(1, 2, 3, 4)
print()

def f(**args):
    print(args)
f()
#f(1)
f(a=1, b=2)
print()

def f(a, *pargs, **kargs):
    print(a, pargs, kargs)
f(1, 2, 3, x=1, y=2)
f(1)
f(1,1,x=1)
print()

# Calls: Unpacking arguments
def func(a, b, c, d):
    print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func(*args)
#func(args)

args = {'a' : 1, 'b' : 2, 'c' : 3}
args['d'] = 4
func(**args)
print()

func(*(1, 2), **{'d' : 4, 'c' : 3})
func(1, *(2, 3), **{'d' : 4})
func(1, c=3, *(2,), **{'d' : 4})
#func(1, c=3, 2, d=4)
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{'d' : 4})

# *pargs in a call is an iteration context
path = r'./resources/args_0557.txt'
f = open(path,'w')
f.write('1\n')
f.write('b\n')
f.write('69\n')
f.close()

def func(*pargs):
    for a in pargs:
        print(a.strip())

func(*open(path))

# Applying functions generically
def func1(x): print(x)
def func2(x, y, z): print(x, y, z)

if False:
    action, args = func1, (1,)
else:
    action, args = func2, (1, 2, 3)
action(*args)
print()

def tracer(func, *pargs, **kargs):
    print('calling:', func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))
'''

# The defunct apply built-in
# Run this in 2.X
def echo(*pargs, **kargs):
    print(pargs, kargs)

echo(1, 2, a=3, b=4)
print()

pargs = (1, 2)
kargs = {'a' : 3, 'b' : 4}

echo(*pargs, **kargs)
apply(echo, pargs, kargs)
print

print apply(pow,(2, 100))
print(pow(*(2, 100)))
print

echo(0, c=5, *pargs, **kargs)

