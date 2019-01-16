class Spam:
    def doit(self, message):
        print(message)

# Qualify instance to get a bound method.
# A bound method object is generated along the way,
# just before the method call's parentheses
object1 = Spam()
object1.doit('hello world')
print()

# Explicitly assign a bound method
object1 = Spam()
x = object1.doit
print(type(x).__name__, x.__repr__())
x('hello bound method')
print()

# Qualify the class to get an umbound method object (function)
object1 = Spam()
t = Spam.doit
print(type(t).__name__, t.__repr__())
t(object1,'hello unbound method')
print()

# A self.method expression (within a class's method)
# is a bound method object because self is an instance object
class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        # This is a bound method object
        x = self.m1
        x(42)
Eggs().m2()