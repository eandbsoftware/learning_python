'''
A class method is not guaranteed to be passed the class in which it is defined; 
it may recieve a subclass instead!
'''
class Spam:
    numInstances = 0
    def count(cls):
        # Updates per-class instance counters
        cls.numInstances += 1
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    # Redefines __init__
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)
    
class Other(Spam):
    # Inherits __init__
    numInstances = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances)
print(Spam.numInstances, Sub.numInstances, Other.numInstances)