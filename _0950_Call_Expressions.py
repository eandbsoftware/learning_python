class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)

C = Callee()
# Call an instance!
C(1, 2, 3)
C(1, 2, 3, x=4, y=5)
print()

class C1:
    # positional parameters with default
    def __call__(self, a, b, c=5, d=6):
        print(f'{self.__class__.__name__} called')

class C2:
    # collect arbitrary positional and keyword arguments
    def __call__(self, *pargs, **kargs):
        print(f'{self.__class__.__name__} called')

class C3:
    # 3.X keyword-only argument with default (which means its optional)
    def __call__(self, *pargs, d=6, **kargs):
        print(f'{self.__class__.__name__} called')

for klass in (C1, C2, C3):
    # All of these calls match the method signatures
    k = klass()
    k(1, 2)
    k(1, 2, 3, 4)
    k(a=1, b=2, d=4)
    k(*[1, 2], **dict(c=3, d=4))
    k(1, *(2,), c=3, **dict(d=4))
print()

class Prod1:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value * other

x = Prod1(2)
print(x(3))
print(x(4))
print()

class Prod2:
    def __init__(self, value):
        self.value = value
    def comp(self, other):
        return self.value * other

x = Prod2(3)
print(x.comp(3))
print(x.comp(4))