#from _0825_A_First_Example import FirstClass
from _0829_A_Second_Example import SecondClass

# Inherits from SecondClass
class ThirdClass(SecondClass):
    # On "ThirdClass(value)"
    def __init__(self, value):
        self.data = value
    
    # On "self + other"
    def __add__(self, other):
        return ThirdClass(self.data + other)

    # On "print(self)", "str()"
    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    # In place change
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
# Inherited method called
a.display()
print(a)
print()

b = a + 'xyz'
b.display()
print(b)
print()

a.mul(3)
print(a)