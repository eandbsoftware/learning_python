'''
# object serves as implicit anchoring superclass,
# which must be present to use super()
class B:
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C:
    def __init__(self):
        print('C.__init__')
        super().__init__()

x = B(); print()
x = C(); print()

class D(B, C):
    pass

x = D()

# Explicit (extra) anchoring superclass instead of object
class A:
    def m(self):
        print('A.m')

class B(A):
    def m(self):
        print('B.m')
        super().m()

class C(A):
    def m(self):
        print('C.m')
        super().m()

class D(B, C):
    def m(self):
        print('D.m')
        super().m()

x = D()
x.m()
'''

# Direct call alternative
class B:
    def __init__(self):
        print('B.__init__')

class C:
    def __init__(self):
        print('C.__init__')

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

x = D()