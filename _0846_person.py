'''
Record and process information about people.
Run this file directly to test its classes.
'''
from _0871_Generic_Display_Tool import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    # fallback for print and str
    # suffices to give a single display in all cases -- prints, nested appearances, and interactive echos
    # ...now inherited from AttrDisplay
    # def __repr__(self):
    #     return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    '''
    A customized person with special requirements.
    '''
    def __init__(self, name, pay):
        # Intellisense skips self argument
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)

class ManagerWrapper:
    # Embed a person object
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    # Strictly speaking this method does not need to be overridden;
    # calls to it it would be caught by the __getattr__ opertor and return Person.getRaise.
    # However, since we want special behavior for managers, we override it and pass it 
    # the sum of percent+bonus as an argument. 
    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)

    # Intercept and delegate attribute fetches. Recall attributes can be properties or methods.
    # Note that operators are not intercepted in 3.X!!!
    # __getattribute__ gets called on attribute fetches regardless of whether it exists or not
    # __getattr__ only gets called for fetches of attributes that don't actually exist.
    # attr is a runtime string
    def __getattr__(self, attr):
        return getattr(self.person, attr)

    # Must overload __repr__ again in 3.X because opertor attribute fetches are not routed through __getattr__.
    def __repr__(self):
        #return str(self.person)
        # Same as...
        return self.person.__repr__()
class Department:
    # *args packs arguments into tuple
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def show_all(self):
        for person in self.members:
            print(person)            

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=1000000)
    print(bob)
    print(sue)
    print()

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
    print()

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)    
    print()

    tom_c = ManagerWrapper('Tommy California', 50000)
    #tom_c.giveRaise(0.10)
    # The following two lines below are equivalent to the one above
    # Just get the function (from Person)
    tom_c_raise_fx = tom_c.giveRaise
    # Invoke it
    tom_c_raise_fx(0.10)
    
    print(tom_c.lastName())
    # print() is an implicit call to (attributes) __str__ or __repr__
    print(tom_c)
    print()

    # Polymorphism in action
    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(0.10)
        print(obj)
    print()

    jas = Person('Jason Gastelum')
    hayden = Person('Hayden Gastelum', job='dev', pay=1000000)
    zoe = Manager('Zoe Gastelum', pay=50000)

    development = Department(jas, hayden)
    development.addMember(zoe)
    development.giveRaises(0.10)
    development.show_all()