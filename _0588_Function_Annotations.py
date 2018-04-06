def func(a, b, c):
    return a + b + c
print(func(1, 2, 3))
print()

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
print(func(1, 2, 3))
print(func.__annotations__)
print()

def func(a: 'spam', b, c: 99):
    return a + b + c
print(func(1, 2, 3))
print(func.__annotations__)

for key in func.__annotations__:
    print(key, '=>', func.__annotations__[key])
print()

# Can use annotations and defaults
# def(name : annotation = default)
def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6 ) -> int:
    return a + b + c
print(func(1, 2, 3))
print(func())
print(func(1, c=10))
print(func.__annotations__)
print()

# Blank spaces are optional
def func(a:'spam'=4, b:(1,10)=5, c:float=6)->int:
    return a + b + c
print(func(1, 2))
print(func.__annotations__)

