# State with nonlocal
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested
F = tester(0)
F('spam')
# nonlocal names are not visible outside the enclosing function
#print(F.state)
print()

# State with global
def tester(start):
    global state
    state = start
    def nested(label):
        global state
        print(state, label)
        state += 1
    return nested
F = tester(0)
F('spam')
F('eggs')
print(state)

G = tester(42)
G('toast')
G('bacon')
F('ham')
print()

# State with Classes
class tester:
    def __init__(self, start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1
F = tester(0)
F.nested('spam')
F.nested('ham')

G = tester(42)
G.nested('toast')
G.nested('bacon')
F.nested('eggs')
print(F.state)
print()

# Intercepting direct calls on instance
class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self,label):
        print(label, self.state)
        self.state += 1
H = tester(99)
H('juice')
H('pancakes')
print()

# Function Attributes
def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested
F = tester(0)
F('spam')
F('ham')
print(F.state)

G = tester(42)
G('eggs')
F('ham')
print(F.state)
print(G.state)
print(F is G)
print()

# State with mutables
def tester(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state = [start]
    return nested
F = tester(0)
F('spam')
F('ham')

G = tester(42)
G('eggs')
F('ham')