import sys
print(sys.path)
print()

'''
# Namespace packages cannot be imported in 3.2 and earlier
import ns2
print(ns2)
# Module file does not have __path__ attribute, but a package (namespace or regular) does
#print(ns2.__path__)
'''

import sub
print(sub)
print(sub.__path__)

