'''
# Referencing nonlocals works normally
def tester(start):
    state = start
    def nested(label):
        print(label, state)
    return nested
F = tester(0)
F('spam')
F('ham')
print()
'''
# Changing a name in an enclosing scope is not allowed by default
def tester(start):
    state = start
    def nested(label):
        # By default, all the names assigned inside a function definition are put in the local scope
       print(label, state)  
       state += 1        
    return nested
F = tester(0)
F('spam')
print()
'''
# Using nonlocal for changes
def tester(start):
    state = start
    def nested(label):
        nonlocal state                
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('spam')
F('ham')
F('eggs')
print()

# nonlocals are per-call, multiple copy data
G = tester(42)
G('spam')
G('eggs')
F('bacon')

# Function arguments are in the local scope
def dummy(me):
    print(dir())
dummy('jason')
print()

# Boundary cases
# nonlocal names must already be assigned in an enclosing def's scope
def tester(start):
    def nested(label):
        nonlocal state
        state = 0
        print(label, state)
    return nested

# globals don't have to exist when called
def tester(start):
    def nested(label):
        global state
        state = 0
        print(label, state)
    return nested
F = tester(0)
F('abc')
print(state)    
print()

# nonlocal restricts the scope lookup to just enclosing defs
spam = 99
def tester():
    def nested():
        nonlocal spam
        print('Current=', spam)
        spam += 1
    return nested
'''