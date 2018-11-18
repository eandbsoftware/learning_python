# Example 0
'''
class klass:
    x = 1
    print(x)
    def m(self):
        x is an undefined variable
        print(x)

k = klass()
k.m()
'''

# Example 1
'''
X = 1
def nester():
    print(X)
    class C:
        print(X)
        def method1(self):
            print(X)
        def method2(self):
            X = 3
            print(X)
    I = C()
    I.method1()
    I.method2()

print(X)
nester()
'''

# Example 2
'''
X = 1
def nester():
    X = 2
    print(X)
    class C:
        print(X)
        def method1(self):
            print(X)
        def method2(self):
            X = 3
            print(X)
    I = C()
    I.method1()
    I.method2()

print(X)
nester()
'''

# Example 3
X = 1
def nester():
    X = 2
    print(X)
    class C:
        X = 3
        print(X)
        def method1(self):
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

print(X)
nester()