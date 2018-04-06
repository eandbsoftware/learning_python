'''
# Prob 1
print('Prob 1')
def func(x):
    print(x)

for i in ['string', 5, [1, 2, 3], {'a':1, 'b':2, 'c':3} ]:
    func(i)
#func()
#func(1, 3)
print()

# Prob 2
print('Prob 2')
def adder(a, b):
    return a + b

for i in [('jason', 'zoe'), ([1, 2, 3], [4, 5, 6]), (3.0, 7.0)]:
    print(adder(*i))
print()

# Prob 3
print('Prob 3')
def adder(*args):
    return sum(args)

def adder(*args):
    aggregate = args[0]
    for e in args[1:]:
        aggregate += e
    return  aggregate
    
print(adder(1))
print(adder(1, 2))
print(adder(1, 2, 3))
print(adder('j', 'a', 'g'))
#print(adder(1, 'jason'))
#print(adder({'a':1, 'b':2, 'c':3}, {'a':1, 'b':2, 'c':3}))
print()

# Prob 4
print('Prob 4')
def adder(good=0, bad=0, ugly=0):
    return good + bad + ugly

print(adder(1))
print(adder(1, 2))
print(adder(1, 2, 3))
#print(adder(1, 2 ,3, 4))
print(adder(ugly=1, good=2))
print()

def adder(**kwargs):
    keys = list(kwargs.keys())
    aggregate = kwargs[keys[0]]
    for key in keys[1:]:
        aggregate += kwargs[key]
    return aggregate
print(adder(a=1, b=2 ,c=3, d=4))
print(adder(a=[1, 2], b=[3, 4]))
print()

# Prob 5
print('Prob 5')
def copyDict(copyme):
    return dict(copyme)
def copyDict(copyme):
    d = {}
    for key in copyme:
        d[key] = copyme[key]
    return d

d = {'a':1, 'b':2, 'c':3}
e = copyDict(d)
e['b'] = '?'
print(d)
print(e)
print()

# Prob 6
print('Prob 6')
def addDict(dict1, dict2):
    composite = dict(dict2)
    for key in dict1:
        composite[key] = dict1[key]
    return composite

x = {1:1}
y = {2:2, 1:99}
z = addDict(x, y)
print(z)
print()

# Prob 7
print('Prob 7')
def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)
def f3(a, **b): print(a, b)
def f4(a, *b, **c): print(a, b, c)
def f5(a, b=2, c=3): print(a, b, c)
def f6(a, b=2, *c): print(a, b, c)

f1(1, 2)                # 1 2
f1(b=2, a=1)            # 1 2
f2(1, 2, 3)             # 1 (2, 3)
f3(1, x=2, y=3)         # 1 {'x':2, 'y':3}
f4(1, 2, 3, x=2, y=3)   # 1 (2, 3) {'x':2, 'y':3}
f5(1)                   # 1 2 3
f5(1, 4)                # 1 4 3
f6(1)                   # 1 2 ()
f6(1, 3, 4)             # 1 3 (4,)
print()

# Prob 8
print('Prob 8')
def primes(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')

primes(13)
primes(13.0)
primes(15)
primes(15.0)
print()

# Prob 9
print('Prob 9')
import math
nums = [2, 4, 9, 16, 25]

roots = []
for i in nums:
    roots.append(math.sqrt(i))
print(roots)

roots = list(map(math.sqrt, nums))
print(roots)

roots = [math.sqrt(x) for x in nums]
print(roots)

roots = list(math.sqrt(x) for x in nums)
print(roots)
print()

# Prob 10
print('Prob 10')
import sys, math
import _0661_Timing_Module_Alternatives as alt_timer
reps = 10000
repslist = range(reps)

def mathMod():
    for i in repslist:
        res = math.sqrt(i)
    return res

def powCall():
    for i in repslist:
        res = pow(i, 0.5)
    return res

def powExpr():
    for i in repslist:
        res = i ** 0.5
    return res

print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = alt_timer.bestoftotal(test, _reps1 = 3, _reps=1000)
    print('%s: %.5f => %s' % (test.__name__, elapsed, result))

import _0663_Using_Keword_only_Arguments as kw_timer
def dictcomp(I):
    return {i: i for i in range(I)}

def dictloop(I):
    new = {}
    for i in range(I):
        new[i] = i
    return new

print(dictcomp(10))
print(dictloop(10))

print(kw_timer.bestof(dictcomp, 10000)[0])
print(kw_timer.bestof(dictloop, 10000)[0])
print()

print(kw_timer.bestof(dictcomp, 100000)[0])
print(kw_timer.bestof(dictloop, 100000)[0])
print()

print(kw_timer.bestof(dictcomp, 1000000)[0])
print(kw_timer.bestof(dictloop, 1000000)[0])
print()

print(kw_timer.total(dictcomp, 1000000, _reps=50)[0])
print(kw_timer.total(dictloop, 1000000, _reps=50)[0])
'''
# Prob 11
print('Prob 11')

def countdown(N):
    if N == 0:
        print('stop')
    else:
        print(N, end=' ')
        countdown(N - 1)
countdown(5)
countdown(20)
print()

# Nonrecursive options
print(list(range(5, 0, -1)))
[print(i, end=' ') for i in range(5, 0, -1)]
print()
list(map(lambda x: print(x, end=' '), range(5, 0, -1)))
print()

# Generator options
def countdown2(N):
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N - 1):
            yield x
print(list(countdown2(5)))

def countdown3(N):
    yield from range(N, 0, -1)
print(list(countdown3(5)))

g = (x for x in range(5, 0, -1))
print(list(g))

print(list(range(5, 0, -1)))

'''
# Prob 12
print('Prob 12')
import math, functools, timeit
def fact1(I):
    if I == 1:
        return 1
    else:
        return I * fact1(I - 1)

def fact2(I):
    return functools.reduce(lambda x, y: x * y, range(1, I + 1))

def fact3(I):
    prod = 1
    for i in range(1, I + 1):
        prod *= i
    return prod

def fact4(I):
    return math.factorial(I)

# Tests
print(fact1(6), fact2(6), fact3(6), fact4(6))
print(fact1(500) == fact2(500) == fact3(500) == fact4(500))
for test in (fact1, fact2, fact3, fact4):
    print(test.__name__, min(timeit.repeat(stmt=lambda: test(500), number=20, repeat=3)))
print()


def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1])

def rev2(S):
    return ''.join(reversed(S))

def rev3(S):
    return S[::-1]

print(rev1('jason'), rev2('jason'), rev3('jason'))
for test in (rev1, rev2, rev3):
    print(test.__name__, min(timeit.repeat(stmt=lambda: test('jason'), number=10000, repeat=3)))
'''
    

