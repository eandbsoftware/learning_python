# Variables and Basic Expressions
a = 3
b = 4
print((a + 1, a-1))
print((b * 3, b / 2))
print((a % 2, b ** 2))
print((2 + 4.0, 2.0 ** b))
print(b / 2 + a)
print(b / (2.0 + a))

# Numeric Display Formats
num = 1 / 3.0
print(num)

print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))
print()

# Comparisons
print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)
print()

# Chained comparisons
X = 2
Y = 4
Z = 6
print(X < Y < Z)
print(X < Y and Y < Z)
print()
print(X < Y > Z)
print(X < Y and Y > Z)
print()
print(1 < 2 < 3.0 < 4)
print(1 < 2 and 2 < 3.0 and 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print()

print(1 == 2 < 3)
print()

print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))

# Division  
print(10 / 4)       # 2.5
print(10 / 4.0)     # 2.5
print(10 // 4)      # 2
print(10 // 4.0)    # 2.0
print()

# Floor vs truncation
import math
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print()
print(5 / 2, 5 / -2)        # 2.5, -2.5
print(5 // 2, 5 // -2)      # 2, -3
print(5 / 2.0, 5 / -2.0)    # 2.5, -2.5
print(5 // 2.0, 5 // -2.0)  # 2.0, -3.0
print()

print(5 / -2)               # 2.5
print(5 // -2)              # -3
print(math.trunc(5 / -2))   # -2    
print()

# Always get a float in 3.X (true division)
print(9/3)