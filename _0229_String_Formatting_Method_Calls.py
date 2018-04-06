# Formatting Method Basics
# By position
template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))

# By keyword
template = '{motto}, {pork} and {food}'
print(template.format(motto='spam', pork='ham', food='eggs'))

# By both
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

# By relative position
template = '{}, {} and {}'
print(template.format('spam', 'ham', 'eggs'))

# Same via expression
template = '%s, %s and %s'
print(template % ('spam', 'ham', 'eggs'))

# Expression with dictionary
template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))
print()

# More...
print('{motto}, {0} and {food}'.format(42, motto='3.14', food=[1,2]))
X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)
print(X.split(' and '))
Y = X.replace('and', 'but under no circumstances')
print(Y)
print()

# Adding Keys, Attributes, and Offsets
import sys
print('My {1[kind]} runs {0.platform}'.format(sys, dict(kind='laptop')))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map=dict(kind='laptop')))
print()

# Indexing (offsets)
somelist = list('SPAM')
print(somelist)
print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)
print('first={0}, last={1}, middle={2}'.format(*parts))