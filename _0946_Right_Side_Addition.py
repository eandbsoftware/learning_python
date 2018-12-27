class Adder:
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return self.data + other

x = Adder(5)
print(x + 2)
# Throws exception because int does not know how to add to an Adder!
#print(2 + x)
print()

# Python will first call left.__add__(right). If that returns NotImplemented Python'
# will check if right implements __radd__ and if it does it will call right.__radd__(left).

class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, right):
        print('add', self.val, right)
        return self.val + right
    def __radd__(self, left):
        print('radd', left, self.val)
        return left + self.val

# calling __add__ directly
class Commuter2:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self.__add__(other)

# swapping order and re-adding to trigger __add__indirectly
class Commuter3:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self + other

# 1.__add__(y) => y.__radd__(1) => y.__add__(1)
#print(1 + y)
# x.__add__(y) => 88.__add__(y) => y.__radd__(88) => y.__add__(88)
#print(x + y)

# assigning __radd__ to be an alias for __add__
class Commuter4:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__

if __name__=='__main__':
    for klass in (Commuter1, Commuter2, Commuter3, Commuter3):
        print('-'*20, klass.__name__, '-'*20 )
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
        
