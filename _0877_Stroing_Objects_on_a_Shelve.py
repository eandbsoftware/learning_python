import _0846_person as person

bob = person.Person('Bob Smith')
sue = person.Person('Sue Jones', job='dev', pay=1000000)
tom = person.Manager('Tom Jones', 50000)

import shelve
db = shelve.open(r'.\resources\persondb_0878')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()