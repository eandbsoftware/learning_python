# Changing Class Attributes Can Have Side Effects
'''
class X:
    a = 1

I = X()
print(I.a)
print(X.a)
print()

X.a = 2
print(I.a)

J = X()
# Assignment to J.a would create a variable on instance J,
# but fetch of J.a just looks it up on X
print(J.a)
print()

# Get work done without ever making a single instance
class X: pass
class Y: pass

X.a = 1
X.b = 2
X.c = 3

Y.a = X.a + X.b + X.c

for X.i in range(Y.a):
    print(X.i)
print()
'''

# Changing Mutable Class Attributes Can Have Side Effects, Too
'''
class C:
    shared = []
    def __init__(self):
        self.perobj = []

x = C()
y = C()
print(y.shared, y.perobj)

x.shared.append('spam')
x.perobj.append('spam')

print(x.shared, x.perobj)
print(y.shared, y.perobj)

print(C.shared)

# Assignment to attribute name that exists on class but not instance
# creates (or reassigns) attribute on instance
x.shared.append('eggs')
x.shared = 44
print(C.shared)
print(x.shared)

# Multiple Inheritance: Order Matters
class ListTree:
    def __str__(self):
        return 'ListTree'
    def other(self):
        return 'ListTree'

class Super:
    def __str__(self):
        return 'Super'
    def other(self):
        return 'Super'

class Sub(ListTree, Super):
    other = Super.other

x = Sub()
print(x)
print(x.other())
print()

class Sub(Super, ListTree):
    __str__ = ListTree.__str__

y = Sub()
print(y)
print(y.other())

# Chapter 29 Page 875 Redux
X = 1
def nester():
    X = 2
    print(X)
    class C:
        # A class is a local scope, but does not  serve
        # as an enclosing scope to further nested code
        X = 3
        print(X)
        def method1(self):
            # Name X = 2 (not 3) is in enclosing def not class!
            print(X)
            print(self.X)
        def method2(self):
            X = 4
            print(X)
            self.X = 5
            print(self.X)

    I = C()
    I.method1()
    I.method2()

print(X)    # 1
nester()    # 2, 3, 2!, 3, 4, 5
'''

# Scopes in Methods and Classes

def generate():
    class Spam:
        count = 1
        def method(self):
            # Spam is in scope of enclosing def            
            print(Spam.count)
    return Spam()

generate().method()

# Restructure such that class is at the top level;
# now method2 and generate2 find Spam2 in the global scope
def generate():
    return Spam()

class Spam:
    count = 1
    def method(self):
        print(Spam.count)

generate().method()

# Class nesting is useful in closure contexts
def generate(label):
    class Spam:
        count = 1
        def method(self):
            print('%s=%s' % (label, Spam.count))
    # Returns a class, not an instance
    return Spam

aclass = generate('Gotchas')
print(type(aclass))
I = aclass()
print(type(I))
I.method()