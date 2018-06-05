'''
# The namespace package is the virtual concatenation of its individual directory components
import sys
print(sys.path)
print()

import sub
print(sub)
print(sub.__path__)
print()

from sub import mod1
import sub.mod2
print()

print(mod1)
print(sub.mod2)


# Import directly through namespace
import sub.mod1
import sub.mod2
print()

print(sub.mod1)
print(sub.mod2)
print()

print(sub)
print(sub.__path__)
'''

# Relative imports work too
import sub.mod1
# Already imported module not rerun
import sub.mod2
print()

print(sub.mod2)