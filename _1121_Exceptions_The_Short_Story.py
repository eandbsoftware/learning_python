# 1. Python raises an exception on an error
# 2. An exception is an event that can modify the flow of control of the program
# 3. The default exception handler is to stop the program and print an error message

# Default Exception Handler
def fetcher(obj, index):
    return obj[index]

x = 'spam'
print(fetcher(x, 3))
# Raises IndexError
# print(fetcher(x, 4))
print()

# Catching Exceptions
try:
    fetcher(x, 4)
except IndexError:
    print('got exception')
print()

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
    print('continuing')
catcher()
print()

# Raising Exceptions
try:
    raise IndexError
except IndexError:
    print('got exception')

# Uncaught exceptions are propagated to the top-level default handler
#raise IndexError

# assert can be used to trigger (conditional) exceptions too
#assert False, 'Nobody expects the Spanish Inquisition!'
print()

# User-Defined Exceptions
class AlreadyGotOne(Exception):
    pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('got an exception')
print()

class Career(Exception):
    def __str__(self):
        return 'So I became a waiter...'

#raise Career()

# Termination Actions
try:
    fetcher(x, 3)
finally:
    print('after fetch')
print()

def after():
    try:
        fetcher(x, 3)
    finally:
        print('after fetch')
    print('after try?')
after()

with open('resources/lumberjack.txt', 'w') as f:
    f.write('The larch!\n')
print('file written')