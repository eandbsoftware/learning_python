# Empty class
class rec:
    pass

# Assign attributes to the class
rec.name = 'bob'
rec.age = 40

# Retrieve attributes from class
print(rec.name)
print()

# Create instances
x = rec()
y = rec()

# Instances fetch the name attribute from their parent class object
print(x.name, y.name)
print()

# Assign attribute to an instance
x.name = 'Sue'
print(rec.name, x.name, y.name)
print()

# The __dict__ attribute is the namespace dictionary for most class-based objects
print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith('__')))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))
print()

# Fetching an attribute
print(x.name, x.__dict__['name'])
print(x.age)
# This will raise a MissingKeyException
#print(x.__dict__['age'])
print()

# Inspect instance.__class__ and class.__bases__ objects
print(x.__class__)
print(rec.__bases__)
print()

# Even methods can be created independent of a class object
def uppername(obj):
    return obj.name.upper()

print(uppername(x))
print()

# Assign this function to an attribute of the class
rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))