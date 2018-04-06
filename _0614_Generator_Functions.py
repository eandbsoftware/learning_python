# Generator functions in action
def gensquares(N):
    for i in range(N):
        yield i ** 2

def just_a_function(N):
    pass

for i in gensquares(5):
    print(i, end=" : ")
print()
print()

x = gensquares(4)
print(x)

f = just_a_function
print(f)
print()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
#print(next(x))
print()

y = gensquares(5)
print(iter(y) == y)
print(next(y))
print()

# Why generator functions
def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
    return res

for x in buildsquares(5):
    print(x, end =" : ")
print()

for x in [n ** 2 for n in range(5)]:
    print(x, end=" : ")
print()

for x in map(lambda x: x ** 2, range(5)):
    print(x, end=" : ")
print()
print()

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print(tuple(ups('aaa,bbb,ccc')))
print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})
