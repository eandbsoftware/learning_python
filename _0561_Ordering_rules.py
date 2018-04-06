# call :    positional arguments, 
#           keyword arguments or *iterable form, 
#           **dict form

# header:   normal arguments, default arguments, 
#           *name form, 
#           normal or default keyword-only arguments, 
#           **name form

#def kwonly(a, **pargs, b, c):
#    pass

#def kwonly(a, **, b, c):
#    pass

#def f(a, *b, **d, c=6):
#    pass

# Header ordering
def f(a, *b, c=6, **d):
    print(a, b, c, d)

f(1, 2, 3, x=4, y=5)
# 1, (2, 3), 6, {x : 4, y : 5}

f(1, 2, 3, x=4, y=5, c=7)
# 1, (2, 3), 7, {x : 4, y : 5}

f(1, 2, 3, c=7, x=4, y=5)
# 1, (2, 3), 7, {x : 4, y : 5}

def f(a, c=6, *b, **d):
    print(a, b, c, d)

f(1, 2, 3, x=4)
# 1, (3,), 2, {x : 4}
print()

# Call ordering
def f(a, *b, c=6, **d):
    print(a, b, c, d)

f(1, *(2, 3), **dict(x=4, y=5))
# 1, (2, 3), 6, {x : 4, y : 5}

# Different from book!
f(1, *(2, 3), **dict(x=4, y=5), c=7)
# 1 (2, 3), 7, {x : 4, y : 5}

f(1, *(2, 3), c=7, **dict(x=4, y=5))
# 1, (2, 3), 7, {x : 4, y : 5}

f(1, c=7, *(2, 3), **dict(x=4, y=5))
# 1, (2, 3), 7, {x : 4, y : 5} 

f(1, *(2, 3), **dict(x=4, y=5, c=7))
# f(1, 2, 3, x=4, y=5, c=7)
# 1, (2, 3), 7, {x : 4, y : 5} 