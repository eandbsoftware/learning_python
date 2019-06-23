class A:
    def act(self):
        print('A')

class B:
    def act(self):
        print('B')

class C(A):
    def act(self):
        super().act()

X = C()
X.act() # A

class D(A, B):
    def act(self):
        super().act()

X = D()
X.act() # A

class E(B, A):
    def act(self):
        super().act()

X = E()
X.act() # B

class F(A, B):
    def act(self):
        A.act(self)
        B.act(self)

X = F()
X.act()