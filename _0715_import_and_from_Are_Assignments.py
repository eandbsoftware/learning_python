'''
# Changing mutables in modules
# Copy two names out
from _0715_small import x, y
print('Original values in main module: x={}, y={}'.format(x, y))

# Reassign name to new object
x = 42

# Mutate shared mutable object
y[0] = 42
print('After reassignment/mutation: x={}, y={}'.format(x, y))

import _0715_small
print("small's values: x={}, y={}".format(_0715_small.x, _0715_small.y))
'''

# Cross-file name changes
from _0715_small import x, y
print(f'Values: {x, y}')

# Reassign name x to a new object
x = 42
print(f'Values: {x, y}')

# Examine name in imported namespace
import _0715_small
print(f'Values: {_0715_small.x, _0715_small.y}')

