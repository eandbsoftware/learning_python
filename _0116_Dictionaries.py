# Assign dictionary literal
D = { 'food' : 'spam', 'quantity' : 4, 'color' : 'pink' }
print(D)
print(D['food'])
D['quantity'] += 1
print(D)

# Start with empty dictionary
D = {}
D['name'] = 'Holden'
D['age'] = 0
D['color'] = 'orange'
print(D)
print(D['name'])

# Other ways to instantiate dictionaries
D1 = dict(name='Hayden', age=3, color='bronze')
print(D1)

D2 = dict(zip(['name', 'age', 'color'],['Jason',38,'olive']))
print(D2)

# Nesting
rec = {'name' : {'first': 'Jason', 'last' :'Gastelum'},
        'jobs': ['officer', 'analyst'],
        'age': 38 }
print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])
rec['jobs'].append('dad')
print(rec)

# Missing Keys
D ={'a' : 1, 'b' : 2, 'c' : 3}
print(D)
D['e'] = 99
print(D)
# Fetching a non-existent key is an error
#print(D['f'])

print('f' in D)
print('a' in D)

# if test
if not 'f' in D:
    print('missing')
    print('no, really...')

# dict.get()
present = D.get('a',0)
print(present)
missing = D.get('x',0)
print(missing)

# ternary operator
value = D['x'] if 'x' in D else 0
print(value)

# Sorting Keys: for Loops
D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D)

print(D.keys())
keys = list(D.keys())
print(keys)

keys.sort()
for key in keys:
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

# for loop works on iterables (like strings)
for c in 'spam':
    print(c)

# while loop
x = 4
while x > 0:
    print('spam!' * x)
    x-= 1

# Iteration and Optimization
squares = [x**2 for x in [1,2,3,4,5]]
print(squares)

sqIter = (x**2 for x in range(6))
print(sqIter)
for s in sqIter:
    print(s)

# Every list comprehension can be rewritten as a loop
squares = []
for x in [1,2,3,4,5]:
    squares.append(x**2)
print(squares)
