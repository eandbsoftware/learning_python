class A:
    def method(self):
        print('A.method')
        # Note that linter thinks that "Super of 'A' has no 'method' member.
        super().method()

class B(A):
    def method(self):
        print('B.method')
        # What if a class needs to replace a super's default entirely?
        #super().method()

class C:
    def method(self):
        print('C.method')

'''
class D(B, C):
    def method(self):
        print('D.method')
        super().method()
'''

# Back to explicit calls
class D(B, C):
    def method(self):
        print('D.method')
        B.method(self)
        C.method(self)

x = D()
x.method()

