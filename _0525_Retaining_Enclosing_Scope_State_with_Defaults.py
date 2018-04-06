'''
# Using default argument values to remember objects in the local scope
def f1():
    x = 88
    def f2(x = x):
        print(x)
    f2()
f1()

# Equivalent that avoids nesting
def f1():
    x = 88
    f2(x)

def f2(x):
    print(x)

f1()
print()

# Nested scopes, defaults, and lambdas
def func():
    x = 4
    action = (lambda n: x ** n)
    return action

x = func()
print(x(2))

# Can use default for lambda too
def func():
    x = 4
    action = (lambda n, x=x: x ** n)
    return action
x = func()
print(x(2))
print(x(2,3))
print()

# Lambda's capturing loop variable incorrectly
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions()
print(acts[0])

for i in range(5):
    print(acts[i](2))
print()

# Done correctly with default arguments
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts
acts = makeActions()
print(acts[0])

for i in range(5):
    print(acts[i](2))
print()

'''
# Doesn't work like in C#
def makeActions():
    acts = []
    for i in range(5):
        j = i
        print(dir())        
        acts.append(lambda x: j ** x)
    return acts
acts = makeActions()
print(acts[0])

for i in range(5):
    print(acts[i](2))
print()


# Arbitrary scope nesting
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()

f1()    
