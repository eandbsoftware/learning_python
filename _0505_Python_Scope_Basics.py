import builtins

'''
# Scope example
X = 99

def func(Y):
    Z = X + Y
    return Z

print(func(1))


# The Built-in Scope
print(dir(builtins))
print()

print(zip)
print(builtins.zip)
print(zip is builtins.zip)

# Redifining built-in names
def hider():
    open = 'spam'
    # Local variable open hides built-in
    #open('data.txt')
    #builtins.open('data.txt')

hider()

print(len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('__')]))

'''
# Intentionally hiding variables in the global scope
X = 88
def func():
    X = 99

func()
print(X)