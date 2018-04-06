'''
# Basic Examples
if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')
print()

# Multiway Branching
x = 'killer rabbit'
if x == 'roger':
    print('shave and a haircut')
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away!')

# Equivalent to
if x == 'roger':
    print('shave and a haircut')
else:
    if x == 'bugs':
        print("what's up doc?")
    else:
        print('Run away!')
print()

choice = 'ham'
print({'spam' : 1.25,
        'ham': 1.99,
        'eggs' : 0.99,
        'bacon' : 1.10}[choice])

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')
print()
'''

# Handling switch defaults
# dict.get
branch = {'spam' : 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))

# in test
choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

# try/except
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')
