class C(object):
    def act(self):
        print('spam')

# Right way
class D(C):
    def act(self):
        super(D, self).act()
        print('eggs')

# Wrong way
# class D(C):
#     def act(self):
#         super().act()
#         print('eggs')

# Traditional way
# class D(C):
#     def act(self):
#         C.act(self)
#         print('eggs')

X = D()
X.act()