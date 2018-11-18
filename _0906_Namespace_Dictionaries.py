import _0897_Abstract_Superclasses as mod
print(mod.__name__)
print(mod.Super)

print(mod.__name__, )
class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

X = Sub()
print(X.__dict__)
print(X.__class__)
print(Sub.__bases__)
print(Super.__bases__)
print()

Y = Sub()
X.hello()
print(X.__dict__)
X.hola()
print(X.__dict__)

print(list(Sub.__dict__.keys()))
print(list(Super.__dict__.keys()))
print(Y.__dict__)
print()

print(X.data1, X.__dict__['data1'])
X.data3 = 'toast'
print(X.__dict__)
X.__dict__['data3'] = 'ham'
print(X.data3)