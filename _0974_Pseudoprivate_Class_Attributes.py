'''
https://stackoverflow.com/questions/1162234/what-is-the-benefit-of-private-name-mangling-in-python
If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, 
consider naming them with double leading underscores and no trailing underscores. 
This invokes Python's name mangling algorithm, where the name of the class is mangled into the attribute name. 
This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.
'''

'''
class C1:
    def meth1(self):
        self.__X = 88
    def meth2(self):
        print(self.__X)

class C2:
    def metha(self):
        self.__X = 99
    def methb(self):
        print(self.__X)

class C3(C1, C2):
    pass

# Problem: same name used on instance by multiple superclasses
# Use case 1: Avoid collisions on instance from multiple superclasses
# Without name mangling, single attribute X is assigned by methods defined in both classes
# Thus, the value of X is dependent on which class assigned it last
# With name mangling, the variable is prefixed with _classname, so that it is (probably) unique on the instance
I = C3()
I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()
'''

def crawl(target):
    # target is class
    if hasattr(target,'__bases__'):
        print(f'class {target.__name__}')
        print('\t', list(target.__dict__.keys()))
        for base in target.__bases__:
            crawl(base)
    # target is instance
    else:
        print(f'instance of {getattr(target, "__class__", None).__name__}')
        print('\t', list(target.__dict__.keys()))
        crawl(target.__class__)

def climb(target):
    # is an instance
    if type(target) != type(type):
        print(f'instance of {getattr(target, "__class__", None).__name__}')
        print('\t', list(target.__dict__.keys()))
        climb(target.__class__)
    else:
        print(f'class {target.__name__}')
        print('\t', list(target.__dict__.keys()))
        for base in target.__bases__:
            climb(base)

class Super:
    def method(self):
        print('Super.method')

class Tool:
    def __method(self):
        print('Tool.__method')
    def other(self):
        self.__method()

class Sub1(Tool, Super):
    def actions(self):
        self.method()

# Problem: same name in two superclasses
# Use case 2: Avoid introducing new names that might 
# accidentally hide definitions elsewere in the class tree
s1 = Sub1()
s1.dummy = 1
climb(s1)
s1.actions()
print()

class Sub2(Tool):
    def __init__(self):
        self.method = 99

# Problem: same name in instance/subclass and superclass
# Use case 3: Avoid introducing new names that might 
# accidentally hide definitions HIGHER in the class tree
# If I didn't rely on name mangling and wanted to call a
# hidden superclass method, I would have to use the fully
# qualified attribute fetch class.method(instance) form.
s2 = Sub2()
climb(s2)
print(s2.method)

# Can still access mangled/hidden attribute, but must know mangled name
s2._Tool__method()
    