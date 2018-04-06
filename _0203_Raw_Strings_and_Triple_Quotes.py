path = r'C:\new\text.dat'
print(repr(path), path, len(path))
print()

f = open(r'C:\_Gastelum\Development\Python\resources\readme.txt','r')
print(f.read())
print()

f = open('C:/_Gastelum/Development/Python/resources/readme.txt','r')
print(f.read())
print()

# not a valid string
#s = r'jason\'

mantra = """Always look
 on the bright
side of life."""
print(repr(mantra))
print(mantra)
print()

# Watch out for comments
menu = """spam      # comments here added to string!
eggs                # ditto
"""
print(repr(menu))

# Alternative way for multi-line strings
menu = (
    "spam\n"        # comments here added to string!
    "eggs\n"        # ditto
)
print(repr(menu))
print()

# Also used to disable code
X = 1
print(X)
"""
import os
print(os.getcwd())
"""
Y = 2
print(Y)
