import math
print(math.pi,math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144),math.sqrt(2))
print(pow(2,4), 2**4, 2.0**4.0)
print(abs(-42.0), sum((1,2,3,4)))
print(min([1,2,3,4]),max(1,2,3,4))
print()

# Dropping decimal digits
print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(int(2.567), int(-2.567))
print(round(2.567), round(2.467), round(2.567, 2))
print(type(round(2.567, 1)))
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))
print(1 / 3.0, round(1 / 3.0, 2), '%.2f' % (1 / 3.0))
print()

# Square roots
print(math.sqrt(144))
print(144**0.5)
print(pow(144,0.5))

print(math.sqrt(1234567890))
print(1234567890**0.5)
print(pow(1234567890,0.5))

# Random
import random
print(random.random(), random.random())
print(random.randint(1, 10), random.randint(1, 10))
myList = ["Live of Brian", "Holy Grail", "Meaning of LIfe"]
print(random.choice(myList), random.choice(myList))
random.shuffle(myList)
print(myList)
