class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Chef1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

class Server1(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

bob = Chef1('bob')
sue = Server1('sue')
print(bob.salary, sue.salary); print()

class Chef2(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)

class Server2(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

bob = Chef2('bob')
sue = Server2('sue')
print(bob.salary, sue.salary); print()


# Employee is a member of both categories;
# superclasses use super() to call their superclass constructor
class TwoJobs(Chef2, Server2):
    pass

# Throws the following exception: __init__() takes 2 positional arguments but 3 were given
# because the next class on the mro is not Employee as implied by the args in Chef2's call 
# to super().__init__, but Server2 which has a different argument list!
#tom = TwoJobs('tom')

print(TwoJobs.__mro__); print()
print(Chef2.__mro__); print()

# Employee is a member of both categories;
# superclasses use direct calls to call their superclass constructor
class TwoJobs(Chef1, Server1):
    pass

# Works, but only the constructor for the leftmost superclass is run
tom = TwoJobs('tom')
print(tom.salary); print()


# 1. Alternative way to route to the top-level class: all direct calls
class TwoJobs(Chef1, Server1):
    def __init__(self, name):
        Employee.__init__(self, name, 70000)

direct = TwoJobs('direct')
print(direct.salary); print()

# 2. Alternative way to route to the top-level class: composite calls
# This is the example that the author refers to but doesn't articulate;
# using two dispatch techniques: direct calls and super() 
class TwoJobs(Chef2, Server2):
    def __init__(self, name):
        Employee.__init__(self, name, 70000)

composite = TwoJobs('composite')
print(composite.salary); print()

# 3. Alternative way to route to the top-level class: all super, doesn't work
class TwoJobs(Chef2, Server2):
    def __init__(self, name):
        super().__init__(name, 70000)

# Same problem with number of arguments, but happens on call to Chef2 (instead of Server2)
all_super = TwoJobs('all_super')
print(all_super.salary)