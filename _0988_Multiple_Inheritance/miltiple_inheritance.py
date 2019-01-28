# Difference between __str__ and __repr__
sentence = "\tHolden's ball"
print(sentence)
print(repr(sentence))
print()

# Pg 989 - default print is pretty much useless
class Spam:
    def __init__(self):
        self.data1 = 'food'
x = Spam()
print(x)

# Pg 992 - using listinstance we can print instance attributes
from listinstance import ListInstance
class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'
y = Spam()
print(y)

# str also calls ListInstance.__str__
display = str(y)
print(display)
# Calling repr on str - returns as-code object, with escaped characters and quotes
print(repr(display))
# Calling repr on Spam object itself - returns default repr
print(repr(y))
print()

# Pg 995 - listinstance also works on a class when it's attributes are assigned outside the class
class C(ListInstance):
    pass
z = C()
z.a, z.b, z.c = 1, 2, 3
print(z)
print()

try:
    class C: pass
    class B(C): pass
    C.__bases__= (B,)
except Exception as ex:
    print(ex)
print()

# Pg 1006 Usage variation: Running on larger modules
from listtree import ListTree
from tkinter import Button

class MyButton(ListTree, Button): pass
B = MyButton(text='spam')
chars_written = open(r'_0988_Multiple_Inheritance\savetree.txt', 'w').write(str(B))
print(chars_written)
print(len(open(r'_0988_Multiple_Inheritance\savetree.txt','r').readlines()))

S = str(B)
print(S[:1000])
print()

# Pg 1006 Collector Module
# import lister
# print(lister.ListInstance)
# print(lister.Lister)

# from lister import Lister
# print(Lister)

from lister import ListInstance as Lister
print(Lister)