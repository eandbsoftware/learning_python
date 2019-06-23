class B:
    def __init__(self):
        print('B.__init__')
        #super().__init__()

class C:
    def __init__(self):
        print('C.__init__')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D.__init__')
        super().__init__()

x = D()
print(D.__mro__)