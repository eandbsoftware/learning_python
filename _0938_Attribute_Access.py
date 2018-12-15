# Attribute Reference
class Empty:
    def __init__(self):
        self.defined = 'defined'
    # Called on self.undefined!
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

X = Empty()
# Defined attribute, NOT routed through self.__getattr__
print(X.defined)
# Undefined attributes, routed through self.__getattr__
print(X.age)
#print(X.name)
print()

# Attribute Assignment
class Accesscontrol:
    def __setattr__(self, attr, value):
        # This pattern may stop an infinite recursion with malformed assignments
        if attr == 'age':
            # Assignment forms that cause infinite recursion, 
            # regardless of whether assignment occurs inside or outside of class
            # Not really natural to hardcode attribute unless using this pattern.
            #self.age = value + 10
            #setattr(self,'age', value + 10)

            # Forms that avoid infinite recursion
            self.__dict__[attr] = value + 10
            # Invoke base object's __setattr__ method, which has NOT been overridden
            # then find attributes via inheritance
            #object.__setattr__(self, attr, value + 10)
        else:
            raise AttributeError(attr + ' not allowed')
    def assignment(self):
        # Assignments within the class are no different from assignments outside 
        # with regard to getting caught by self.__setattr__
        self.__dict__['endrun'] = True
        self.other = 99


X = Accesscontrol()
X.age = 40
print(X.age)
#X.name = 'Bob'
#X.assignment()
print()

class DeleteControl:
    def __delattr__(self, attribute):
        if attribute == 'name':
            # Avoids infinite recursion
            del self.__dict__[attribute]
            # Causes infinite recursion
            #del self.name
        else:
            raise AttributeError("%s is not an existing attribute" % attribute)
        
d = DeleteControl()
d.name = 'Jason'
d.age = 39
del d.name
print(d.__dict__)