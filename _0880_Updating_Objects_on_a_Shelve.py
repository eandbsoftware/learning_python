import shelve
# Reopen shelve
db = shelve.open(r'.\resources\persondb_0878')

for key in sorted(db):
    print(key, '=>', db[key])

# Create object in memory from db
sue = db['Sue Jones']
sue.giveRaise(0.10)
# Assign to key to update in shelve
db['Sue Jones'] = sue
db.close()