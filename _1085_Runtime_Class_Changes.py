class X:
    def m(self):
        print('X.m')

class Y:
    def m(self):
        print('Y.m')

class C(X):
    def m(self):
        # Alternative 1: using super()
        #super().m()
        # Alternative 2: calling through the current 
        # superclass tuple's value indirectly
        C.__bases__[0].m(self)
i = C()
i.m()

# Change the superclass at runtime
C.__bases__ = (Y,)
i.m()