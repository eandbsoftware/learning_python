import glob

# Examine the files
path = r'.\resources\person*'
# Use glob.glob to return a lists of paths matching a pattern
matches = glob.glob(path)
print(matches)
print()

print('contents of .dir\n', open(matches[2]).read())
print()

print('contents of .dat\n', open(matches[1],'rb').read()[:100])
print()

# Examine the files as a client
import shelve
db = shelve.open(r'.\resources\persondb_0878')
print(len(db))
print(list(db.keys()))
# Don't have to import Person class here to recreate class instance!
bob = db['Bob Smith']
print(bob)
print(bob.lastName())

for key in db:
    print(key, '=>', db[key])
print()

for key in sorted(db):
    print(key, '=>', db[key])