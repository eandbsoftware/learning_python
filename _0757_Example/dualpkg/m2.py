import sys
print(sys.path)

# Relative import statement works when the file is used as a package,
# but is not allowed in nonpackage mode by either 2.X or 3.X
#from . import m1

# A simple import statement works in nonpackage mode in both 2.X and 3.X,
# but fails in package mode in 3.X only
#import m1

# Using full package paths works in both usage modes and Pythons,
# as long as the package's root is on the module search path
# Recall that multiple dirs in PYTHONPATH should NOT be separated by a space!
import dualpkg.m1 as m1

def somefunc():
    m1.somefunc()
    print('m2.somefunc')

# Self-test or top-level script usage mode code
if __name__ == '__main__':
    somefunc()