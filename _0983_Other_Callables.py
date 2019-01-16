# Callables: functions (def or lambda), instances with __call__, and bound instance methods
def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):
        self.val = val
    def method(self, val):
        return self.val * val

sum_obj = Sum(2)
prod_obj = Product(3)

# function, instance, bound method; all take 1 parameter
actions = [square, sum_obj, prod_obj.method]
for act in actions:
    print(act(5))
print()

# Treat callables generically
print(actions[-1](5))
print([act(5) for act in actions])
print(list(map(lambda act:act(5), actions)))
print()

# Classes are callable too!
class Negate:
    def __init__(self, val):
        self.val = -val
    def __repr__(self):
        return str(self.val)
    # def __str__(self):
    #     return str(self.val)
    def __format__(self, spec):
        return self.val.__format__(spec)

actions = [square, Sum(2), Product(3).method, Negate]
for act in actions:
    print(act(5))
print()

# Use __repr__ above so that contained items print as desired
print([act(5) for act in actions])
print()

table = {act(5): act for act in actions}
for (key, value) in table.items():
    # Cannot use width format option...
    print('{0:2} => {1}'.format(key, value))