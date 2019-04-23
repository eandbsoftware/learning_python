'''
class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

x = operators()
# Routed through __getattr__
print(x.age)
# Routed through __getattr__
#print(x.name)

class properties(object):
    def getage(self):
        return 40
    age = property(getage, None, None, None)

x = properties()
# Routed through getage
print(x.age)
# Normal fetch
#print(x.name)

class properties(object):
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)

x = properties()
# Routed through getage
print(x.age)
# Routed through setage
x.age = 42
# Normal fetch
print(x._age)
# Routhed through getage
print(x.age)
# Normal fetch, assign
x.job = 'trainer'
print(x.job)
'''

class operators(object):
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value

x = operators()
# Routed through __getattr__
print(x.age)
# Routed through __setattr__
x.age = 41
# Defined: no __getattr__ call
print(x._age)
# Routed through __getattr__
print(x.age)
# Routed through __setattr__
x.job = 'trainer'
# Defined: no __getattr__ call
print(x.job)
