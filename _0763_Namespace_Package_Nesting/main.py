import sys
[print(p) for p in sys.path]
print()

'''
# Namespace pkg nested in a namespace pkg
import sub.lower.mod3

# Same effect if accessed incrementally
import sub
print(sub)
[print(s) for s in sub.__path__]
print()

import sub.mod2
import sub.lower.mod3
print()

print(sub.lower)
[print(s) for s in sub.lower.__path__]
'''

# Nesting behavior holds whether the lower component is a module, regualr package or another namespace package
# Nested module
import sub.mod2
# Nested regular package
import sub.pkg
# Nested namespace package
import sub.lower.mod3
print()

# Namespace package
print(sub)
# Nested module
print(sub.mod2)
# Nested regular package
print(sub.pkg)
# Nested namespace package
print(sub.lower)
# Double nested module
print(sub.lower.mod3)