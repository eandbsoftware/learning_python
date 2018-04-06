import sys

'''
# Called without an argement to list variables in scope
print(dir())
name = 'jason'
# Called with an object to list all of the attributes
print(dir(name))
# Called with the name of a data type to list all of the attributes
print(dir(str))

print(dir(sys))
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith("__")]))
print(len([x for x in dir(sys) if x[0] != "_"]))
print()

print(dir([]) == dir(list))
print(dir(list))

print(dir("") == dir(str))
print(dir(str))

print(len(dir([])), len([x for x in dir([]) if not x.startswith("__")]))
print(len(dir(str)), len([x for x in dir(str) if not x.startswith("_")]))

print([x for x in dir([]) if not x.startswith("__")])
print([x for x in dir({}) if not x.startswith("__")])

'''
def dir1(x):
    return [a for a in dir(x) if not a.startswith("__")]
print(dir1(tuple))
print()

name = 'zoe'
print(dir("") == dir(str))
print(dir(name) == dir(""))
print(dir(list) == dir([]))
