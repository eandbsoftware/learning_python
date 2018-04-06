# Sets
X = set('spam')
print(X)
Y = {'h', 'a', 'm'}
print(Y)
S = set('spamh')

# Intersection
print(X & Y)
# Union
print(X | Y)
# In X but not in Y
print(X - Y)
# X is a superset of Y
print(X > Y)
print(S > Y)

# Set comprehension
print({n**2 for n in [1,2,3,4,4]})

# Filter out duplicates
print(list(set([1,2,1,3,1])))
# Differences
print(set('spam') - set('ham'))
# Order-neutral equality
print(set('spam') == set('asmp'))

t = 'p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']
print(t)

# Floating points
print(1/3)
print(2/3 + 1/2)

# Decimals
import decimal
d = decimal.Decimal('3.141')
print(d + 1)
print(3.141 + 1)

decimal.getcontext().prec = 5
print('precision', decimal.getcontext().prec)
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction
f = Fraction(2,3)
print(f, f + 1)
print(f + Fraction(1,2))

# Booleans
b = 1 > 2, 1 < 2
print(b)
print(bool('spam'))
print(bool(''))

# None
X = None
print(X)
L = [None] * 10
print(L)

# Types
print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print('samesame')

if type(L) == list:
    print('samesame')

if isinstance(L,list):
    print('samesame')

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)

jason = Worker("Jason Gastelum", 57000)
zoe = Worker("Zoe Gastelum", 114000)
print(jason.lastname())
zoe.giveRaise(0.1)
print(zoe.pay)
Worker.giveRaise(jason,0.05)
print(jason.pay)
