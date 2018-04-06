import math
from _0635_Permutations import permute1, permute2
'''
print(math.factorial(10))
print()

# Using normal evaluation
seq = list(range(10))
print(seq)
p1 =permute1(seq)
print((len(p1), p1[0], p1[1]))
print()

# Using lazy evaluation
p2 = permute2(seq)
print(next(p2))
print(next(p2))
p2 = list(permute2(seq))
print(p1 == p2)
print()
'''

# Generators can produce results from large solution sets
print(math.factorial(50))
p3 = permute2(list(range(50)))
print(next(p3))
print()

# Shuffling sequence first
import random
print(math.factorial(20))
seq = list(range(20))
print(seq)
random.shuffle(seq)
print(seq)
p = permute2(seq)
print(next(p))
print(next(p))
print()

random.shuffle(seq)
print(seq)
p = permute2(seq)
print(next(p))
print(next(p))