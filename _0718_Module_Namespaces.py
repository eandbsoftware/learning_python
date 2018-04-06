import _0719_module2 as module2

# Files Generate Namespaces
# A module file's (global) scope becomes a module object's attribute namespace
print(module2.sys)
print(module2.name)
print(module2.func)
print(module2.klass)
print()

#Namespace Dictionaries: __dict__
# Assigned names become dictionary keys
print(list(module2.__dict__.keys()))
print()

# __file__ gives the name of the file the module was loaded from
print(module2.__dict__['__file__'])
print()

# Filter out double_underscore names
print(list(name for name in module2.__dict__.keys() if not name.startswith('__')))
print()

# Attribute fetch is similar to dictionary indexing
print((module2.name, module2.__dict__['name']))
