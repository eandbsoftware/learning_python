# tuple-based record
rec = ('Bob', 40.5, ['dev', 'mgr'])
print(rec)
print(rec[0])
print()

# dict-based record
rec2 = {}
rec2['name'] = 'Bob'
rec2['age'] = 40.5
rec2['jobs'] = ['dev', 'mgr']
print(rec2)
print(rec2['name'])
print()

# Emulate with a class
class rec3: pass
rec3.name = 'Bob'
rec3.age = 40.5
rec3.jobs = ['dev', 'mgr']
print(rec3)
print(rec3.name)
print()

# Attach attributes to instances instead
class rec4: pass
pers1 = rec4()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec4()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)
print()

# Full blown class
class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
print(rec1.jobs)
rec2 = Person('Sue', ['dev', 'cto'])
print(rec2.info())
print()

# class construction calls closely resemble dictionaries
rec = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(rec)
rec = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
print(rec)

# Using a namedtuple...