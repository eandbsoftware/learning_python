# Function objects can be reassigned to other names
def echo(message):
    print(message)
echo('Direct call!')
x = echo('Indirect call!')
print()

# Pass functions to other functions
def indirect(func, arg):
    func(arg)
indirect(echo, 'Argument call!')
print()

# Stuff functions into data structures
schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg)
print()

# Functions can be created and returned elsewhere
def make(label):
    def echo(message):
        print(label + ' : ' + message)
    return echo
F = make("Makers' Mark")
F('Ham!')
F('Eggs!')
print()

# Function Introspection
def func(a):
    b = 'spam'
    return b * a
print(func(8))
print(func.__name__)
print(func.__code__)
print(dir(func.__code__))
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print()

# Function Attributes
print(func)
func.count = 0
func.count +=1
print(func.count)

func.handles = 'Button-Press'
print(func.handles)
print(dir(func))
print()

# In 3.X, all python internals have leading and trailing underscores
def f(): pass
print(len(dir(f)))
print([x for x in dir(f) if not x.startswith('__')])