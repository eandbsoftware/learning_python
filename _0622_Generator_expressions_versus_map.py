# Apply built-in function
print(list(map(abs, (-1, -2, 3, 4))))
print(list(abs(x) for x in (-1, -2, 3, 4)))
print()

# Apply lambda expression
print(list(map(lambda x: x * 2, (1, 2, 3, 4))))
print(list(x * 2 for x in (1, 2, 3, 4)))
print()

line = 'aaa,bbb,ccc'
# Throw-away list
print(''.join([x.upper() for x in line.split(',')]))

# Apply built-in function
print(''.join(x.upper() for x in line.split(',')))
print(''.join(map(str.upper, line.split(','))))
print()

# Apply lambda expression
print(''.join(x * 2 for x in line.split(',')))
print(''.join(map(lambda x: x * 2, line.split(','))))
print()

# Both can be nested
# Unnecessarily creates two lists
print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))
print(list(x * 2 for x in (abs(y) for y in (-1, -2, 3, 4))))
print()

import math
print(list(map(math.sqrt, (x **2 for x in range(4)))))
print()

# Arbitrarily deep nesting
print(list(map(abs,map(abs, map(abs, (-1, 0, 1))))))
print(list(abs(x) for x in (abs(y) for y in (abs(z) for z in (-1, 0, 1)))))
print()

# Flatter is better than nested
print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))
print(list(math.sqrt(x ** 2) for x in range(4)))
print(list(abs(x) for x in (-1, 0, 1)))