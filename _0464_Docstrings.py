import docstrings
'''
# User-defined docstrings
print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.employee.__doc__)
'''
# Built-in docstrings
import sys
# Built-in modules have docstrings
#print(sys.__doc__)

print(sys.version)

# Functions, classes, and methods have descriptions in their __doc__ attributes as well
print(sys.getrefcount.__doc__)

# built-in functions have docstrings
print(int.__doc__)
print(map.__doc__)