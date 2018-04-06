import sys
'''
# Don't need to print help
help(sys.getrefcount)

# Same as what's in docstring
print(sys.getrefcount.__doc__)

# For larger objects, the help display is broken down into multiple sections
help(sys)

# Can use help on built-in functions, methods and types
help(dict)

help(str.replace)
help(''.replace)

help(ord)
'''

# Works on custom modules too
import docstrings
#help(docstrings.square)
#help(docstrings.employee)
help(docstrings)