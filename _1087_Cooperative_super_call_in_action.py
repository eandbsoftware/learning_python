'''
# Traditionally coded python classes
# (i.e., non-diamond)

class B:
    def __init__(self):
        print('B.__init__')

class C:
    def __init__(self):
        print('C.__init__')

# No constructor on D
# class D(B, C): pass

# Yes constructor on D
class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

x = D()

# Explicit-name calls may trigger the top-level class's 
# method more than once in diamond class tree patterns
class A:
    def __init__(self):
        print('A.__init__')
    
class B(A):
    def __init__(self):
        print('B.__init__')
        A.__init__(self)

class C(A):
    def __init__(self):
        print('C.__init__')
        A.__init__(self)

x = B(); print()
x = C(); print()

class D(B, C):
    pass

x = D(); print()

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

x = D()
'''

class A:
    def __init__(self):
        print('A.__init__')
    
class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C(A):
    def __init__(self):
        print('C.__init__')
        super().__init__()

x = B(); print()
x = C(); print()

class D(B, C):
    pass
    # Don't actually need this constructor, but it works
    # def __init__(self):
    #     super().__init__()

x = D(); print()

print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
