class Methods:
    def imethod(self, x):
        print([self, x])
    def smeth(x):
        print([x])
    def cmeth(cls, x):
        print([cls, cls.__name__, x])
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

# Instance methods - must be passed an instance object
obj = Methods()
obj.imethod(1)
Methods.imethod(obj, 2)

# Static methods - called without passing an instance argument (even when called from an instance!)
Methods.smeth(3)
obj.smeth(4)

# Class methods - passed the class (not an instance)
Methods.cmeth(5)
obj.cmeth(6)