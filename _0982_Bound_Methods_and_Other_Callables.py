class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3
    
x = Number(2)
y = Number(3)
z = Number(4)
print(x.double()); print()

# Bound methods can be processed as generic objects
acts = [x.double, y.double, y.triple, z.double]
for act in acts:
    print(act())
print()

# Bound methods have introspection tools: __self__ and __func__
bound = x.double
print('self:', bound.__self__, 'func:', bound.__func__)
print(bound.__self__.base)
print(bound())
print(bound.__self__.double())
print(bound.__func__(bound.__self__))
