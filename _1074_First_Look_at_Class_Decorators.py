# Automatically augment class with attribute
def addCount(aClass):
    aClass.numInstances = 0
    return aClass

@addCount
class Spam:
    def __init__(self):
        self.count()
    @classmethod
    def count(cls):
        cls.numInstances += 1

@addCount
class Sub(Spam):
    def __init__(self):
        Spam.__init__(self)

@addCount
class Other(Spam):
    pass

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances)
print(Spam.numInstances, Sub.numInstances, Other.numInstances)
print()

# As defined, can be applied to class or function
@addCount
def func(): pass
@addCount
class klass: pass

print(hasattr(func,'numInstances'), hasattr(klass, 'numInstances'))
print()

# Use a decorator to manage an object's interface by intercepting construction calls
def decorator(cls):
    class Proxy:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Proxy

@decorator
class C: 
    def __init__(self, name):
        self.name = name
x = C('jason')
print(type(x))
print(x.name)
