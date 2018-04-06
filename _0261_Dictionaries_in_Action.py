# Basic dictionary operations
D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
print(D['spam'])
print(D)
print()

print(len(D))
print('ham' in D)
print(D.keys())
print(list(D.keys()))
print()

# Changing Dictionaries in Place
print(D)
D['ham'] = ['grill', 'bake', 'fry']
print(D)
del D['eggs']
print(D)
D['brunch'] = 'bacon'
print(D)
print()

# More dictionary methods
D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
print(D.keys())
print(list(D.keys()))
print(D.values())
print(list(D.values()))
print(D.items())
print(list(D.items()))
print()

print(D.get('spam'))
print(D.get('toast'))
print(D.get('toast', 88))
print()

D2 = {'toast' : 4, 'muffin' : 5, 'spam': 99}
D.update(D2)
print(D)
print()

print(D.pop('muffin'))
print(D)
print(D.pop('toast'))
print(D)

L = ['aa', 'bb', 'cc', 'dd']
print(L.pop())
print(L)
L.pop(1)
print(L)
print()

# Example: Movie Database
table = {'1975' : 'Holy Grail', '1979' : 'Life of Brian', '1983' : 'The Meaning of Life'}
year = '1983'
movie = table[year]
print(movie)

for year in table:
    print(year + '\t' + table[year])

# Preview: Mapping values to keys
table = {'Holy Grail' : '1975', 'Life of Brian' : '1979', 'The Meaning of Life' : '1983'}
print(table['Holy Grail'])

print(list(table.items()))
print([title for (title,year) in table.items() if year == '1975'])
print()

K = 'Holy Grail'
print(table[K])

V = '1975'
print([key for (key, value) in table.items() if value == V])
print([key for key in table.keys() if table[key] == '1975'])
print()

# Using dictionaries to simulate flexible lists: Integer keys
L = []
# list assignment index out of range
#L[99] = 'spam'

print([0]*10)

D = {}
D[99] = 'spam'
print(D[99])
print(D)
print()

table = { 1975 : 'Holy Grail', 1979 : 'Life of Brian', 1983 : 'The Meaning of Life'}
print(table[1975])
print(list(table.items()))
print()

# Using dictionaries for spase data structures: Tuble keys
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4
print(Matrix[X, Y, Z])
print(Matrix)

#print(Matrix[(2, 3, 6)])

# Avoiding missing-key errors
if (2, 3, 6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

print(Matrix.get((2, 3, 4), 0))
print(Matrix.get((2, 3, 6), 0))
print()

# Nesting in dictionaries
rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])

rec = {'name' : 'Bob', 
        'jobs' : ['developer', 'manager'],
        'web' : 'www.bons.org/~Bob',
        'home' : {'state' : 'Overworked', 'zip' : 12345}
}

print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

other = {'name' : 'Jason', 
        'jobs' : ['developer', 'manager'],
        'web' : 'www.headachehq.com',
        'home' : {'state' : 'Overworked', 'zip' : 87107}
}

db = []
db.append(rec)
db.append(other)
print(db[1]['name'])

db = {}
db[rec['name']] = rec
db[other['name']] = other
print(db['Jason'])
print()

# Other Ways to Make Dictionaries
D = {'name' : 'Bob', 'age' : 40}
print(D)

D = {}
D['name'] = 'Bob'
D['age'] = 40
print(D)

D = dict(name='Bob', age=40)
print(D)

D = dict([('name', 'Bob'), ('age', 40)])
print(D)

keylist = ['name', 'age']
valuelist = ['Bob', 40]
D = dict(zip(keylist, valuelist))
print(D)

D = dict.fromkeys(['a', 'b'], 0)
print(D)
print()

# Why You Will Care: Dictionaries Versus Lists
L = ['Bob', 40.5, ['dev', 'mgr']]
print(L[0])
print(L[1])
print(L[2][1])

D = {'name' : 'Bob', 'age' : 40.5, 'jobs' : ['dev', 'mgr']}
print(D['name'])
print(D['age'])
print(D['jobs'][1])

D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(D['name'])
print(D['age'])
print(D['jobs'][1])
print()

D = {}
D['state1'] = True
print('state1' in D)

S = set()
S.add('state1')
print('state1' in S)