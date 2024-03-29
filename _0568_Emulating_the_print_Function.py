"""
Emulate most of the 3.X print function for use in 2.X (and 3.X)
Call signature: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""

import sys
def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print3(1, 2, 3)
print3(1, 2, 3, sep='')
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')

print3(4, 5, 6, sep='', end='')
print3(7, 8, 9)
print()
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)