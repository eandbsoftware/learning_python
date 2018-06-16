'''
from unders import *

print(a, c)
# Variables prefixed by underscore do not get imported in from * statements
#print(_b)

# But they can still be accessed by other imports
import unders
print(unders._b)
'''

# __all__ lists variables that should be imported in from * statements, 
# and has precedence over leading underscores
from alls import *
print(a, _c)
print(b)