'''
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        # self.func is a function (not a bound method on klass); 
        # it expects 4 arguments but is only passed 3
        print(self.func.__code.co_varnames)
        return self.func(*args)

@tracer
def spam(a, b, c):
    return a + b + c

print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
print()

# Cannot use tracer class to decorate class-level method function!
# Method name on target class reassigned to instance of tracer and
# since tracer does not have a reference to the instance on which
# the method is defined, it cannot pass self argument and ends 
# up being one parameter short.
class klass:
    # bound method
    def eggs(self):
        pass
    # tracer object!!!
    @tracer
    def spam(self, a, b, c):
        return a + b + c

k = klass()
print(k.eggs, k.spam)
k.spam(1, 2, 3)

'''
def tracer(func):
    # oncall becomes a bound method to C!!!
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    # Replace original spam method with nested function returned from tracer.
    # Original spam method is captured in closure, but as a function.
    # That is the difference!! In the first implementation of tracer we
    # replaced a method with a callable instance of tracer, rather than
    # another method (or function that could serve as a method)
    def spam(self, a, b, c):
        return a + b + c

x = C()
print(x.spam)
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))