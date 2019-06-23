# Odd semantics
class C:
    def act(self):
        print('spam')

class D(C):
    def act(self):
        super().act()
        print('eggs')

X = D()
X.act()
print()

print(super)
# Raises an exception
#super()
print()

class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()

E().method()