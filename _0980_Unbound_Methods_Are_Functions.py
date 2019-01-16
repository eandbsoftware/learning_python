class Dummy:
    def meth(self):
        pass
    def func():
        pass

d = Dummy()
print(type(d.meth).__name__, d.meth)
print(type(d.func).__name__, d.func)
print(type(Dummy.meth).__name__, Dummy.meth)
print(type(Dummy.func).__name__, Dummy.func)
print()

class Selfless:
    def __init__(self, data):
        self.data = data
    # A simple function in 3.X
    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2
    def selfless(arg1, arg2):
        return arg1 + arg2
    
X = Selfless(2)
# Invoked through instance so instance is passed automatically as self argument
print(X.normal(3, 4))
# self expected by method: pass instance manually
print(Selfless.normal(X, 3, 4))

# No instance: works in 3.X, fails in 2.X!
print(Selfless.selfless(3, 4))
print()

# Calling 'static' function through an instance Fails! 
# takes 2 positional arguments but 3 were given (first of which is the implicitly passed instance)
#print(X.selfless(3, 4))

# Calling a 'method' through the class without explicitly passing the instance Fails!
#  missing 1 required positional argument: 'arg2'
print(Selfless.normal(3, 4))