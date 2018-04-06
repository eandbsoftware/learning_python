print(type(1))
# The type of an object is an object of type type
print(type(int))
print(type(type(1)))
# The type of a type object is type
print(type(type(int)))
print()

print(type([1]) == type([]))
print(type([1]) == list)
print(isinstance([1], list))
print()

import types
def f(): pass
print(type(f) == types.FunctionType)