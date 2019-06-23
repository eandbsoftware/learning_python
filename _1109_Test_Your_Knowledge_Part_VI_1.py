# Part 1
'''
class Adder:
    def add(self, x, y):
        print('Not Implemented')

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        composite = dict(x)
        composite.update(y)
        return composite

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']

adder = Adder()
adder.add(L1, L2)

listAdder = ListAdder()
print(listAdder.add(L1, L2))

D1 = dict(zip(L1, L2))
D2 = dict(zip(L2, L1))
print(D1)

dictAdder = DictAdder()
print(dictAdder.add(D1, D2))

'''
# Part 2
class Adder:
    def __init__(self, data):
        self.data = data
    def __add__(self, other_data):
        # Z is a list or dict, not another Adder
        return self.add(self.data, other_data)
    def __radd__(self, other_data):
        return self.add(self.data, other_data)
    def add(self, my_data, other_data):
        print('Not Implemented')

class ListAdder(Adder):
    def add(self, my_data, other_data):
        return my_data + other_data

class DictAdder(Adder):
    def add(self, my_data, other_data):
        composite = dict(my_data)
        composite.update(other_data)
        return composite

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']

adder = Adder(L1)
adder + L2

listAdder = ListAdder(L1)
print(listAdder + L2)

D1 = dict(zip(L1, L2))
D2 = dict(zip(L2, L1))

dictAdder = DictAdder(D1)
print(dictAdder + D2)

x = Adder([1])
x + [2]

x = ListAdder([1])
x + [2]
[2] + x

'''
# Part 3
class Adder:
    def __init__(self, data):
        self.data = data
    def __add__(self, other_data):
        # Z is a list or dict, not another Adder
        return self.add(other_data)
    def add(self, y):
        print('Not Implemented')

class ListAdder(Adder):
    def add(self, other_data):
        return self.data + other_data

class DictAdder(Adder):
    def add(self, other_data):
        composite = dict(self.data)
        composite.update(other_data)
        return composite

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']

adder = Adder(L1)
adder + L2

listAdder = ListAdder(L1)
print(listAdder + L2)

D1 = dict(zip(L1, L2))
D2 = dict(zip(L2, L1))

dictAdder = DictAdder(D1)
print(dictAdder + D2)
'''