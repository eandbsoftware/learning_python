# 1.  Method name sets are disjoint - super skips ahead in mro until it finds a class with the requested name
'''
class A:
    def other(self):
        print('A.other')
    
class Mixin(A):
    def other(self):
        print('Mixin.other')
        super().other()

class B:
    def method(self):
        print('B.method')

# class C(Mixin, B):
#     def method(self):
#         print('C.method')
#         super().other()
#         # call to method is passed on, even though Mixin, the next class in the MRO,
#         # doesn't define that method's name
#         super().method()

# C().method()
# # C.method, Mixin.other, A.other, B.method
# print(C.__mro__)

# Mixing the other way
class C(B, Mixin):
    def method(self):
        print('C.method')
        # B doesn't define other, but classes later in the MRO do.
        super().other()
        super().method()

C().method()
# C.method, Mixin.other, A.other, B.method
print(C.__mro__)
'''

# 2. super() skips ahead in diamonds too
'''
class A:
    def other(self):
        print('A.other')

class Mixin(A):
    def other(self):
        print('Mixin.other')
        super().other()

class B(A):
    def method(self):
        print('B.method')

# class C(Mixin, B):
#     def method(self):
#         print('C.method')
#         super().other()
#         super().method()

# C().method()
# # C.method, Mixin.other, A.other, B.method
# print(C.__mro__)

# # Other mix-in orderings work too
# class C(B, Mixin):
#     def method(self):
#         print('C.method')
#         super().other()
#         super().method()

# C().method()
# # C.method, Mixin.other, A.other, B.method
# print(C.__mro__)

# Direct calls are more explicit
class C(Mixin, B):
    def method(self):
        print('C.method')
        Mixin.other(self)
        B.method(self)

C().method()
'''

# 3. Dispatch order for same-named methods can cause unexpected results
'''
class A:
    def method(self):
        print('A.method')

class Mixin(A):
    def method(self):
        print('Mixin.method')
        super().method()

Mixin().method(); print()

class B(A):
    def method(self):
        print('B.method')
        # super() here would invoke A after B

class C(Mixin, B):
    def method(self):
        print('C.method')
        super().method()

C().method()

# Direct calls give much more control, and allow mix-in classes
# to be much more independent of usage contexts
'''

class A:
    def method(self):
        print('A.method')

class Mixin(A):
    def method(self):
        print('Mixin.method')
        # Direct call renders mro moot
        A.method(self)

class B(A):
    def method(self):
        print('B.method')

class C(Mixin, B):
    def method(self):
        print('C.method')
        Mixin.method(self)

C().method()