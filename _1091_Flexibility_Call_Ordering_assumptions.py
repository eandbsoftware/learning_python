# Explicit calls to methods in the mro that also invoke super()
# will repeat subgraphs of the mro!
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

class D(B, C):
    def __init__(self):
        print('D.__init__')
        C.__init__(self)
        B.__init__(self)

x = D()
print(D.__mro__)