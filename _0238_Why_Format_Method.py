# Extra features
print('{0:b}'.format((2**16) - 1))
#print('%b' % ((2**16) - 1))
print(bin((2**16) - 1))
print('%s' % bin((2**16) - 1))
print('{}'.format(bin((2**16) - 1)))
print('%s' % bin((2**16) - 1)[2:])

print('{:,d}'.format(999999999))
print()

# Flexible reference syntax
print('{name} {job} {name}'.format(name='Jason', job='Data Scientist'))
print('%(name)s %(job)s %(name)s' % dict(name='Jason', job='Data Scientist'))

D = dict(name='Jason', job='Data Scientist')
print('{0[name]} {0[job]} {0[name]}'.format(D))
print('{name} {job} {name}'.format(**D))
print('%(name)s %(job)s %(name)s' % D)
print()

# Explicit value references
print('The {0} side {1} {2}'.format('bright', 'of', 'life'))
print('The {} side {} {}'.format('bright', 'of', 'life'))
print('The %s side %s %s' % ('bright', 'of', 'life'))

print('{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))
print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
print()

# Named method and context-neutral arguments
print('%.2f' % 1.2345)
print('%.2f %s' % (1.2345, 99))
print('%s' % 1.23)
print('%s' % (1.23,))
print('%s' % ((1.23,),))

print('{0:.2f}'.format(1.2345))
print('{0:.2f} {1}'.format(1.2345, 99))
print('{0}'.format(1.23))
print('{0}'.format((1.23,)))
print()

# Functions vs expressions
def myformat(fmt, args): return fmt % args
print(myformat('%s - %s', (88,99)))
print()

# Plus one more
print('%(num)i = %(title)s' % dict(num=7, title='Strings'))
print('{num:d} = {title:s}'.format(num=7, title='Strings'))
print('{num} = {title}'.format(**dict(num=7, title='Strings')))

import string
t = string.Template('$num = $title')
print(t.substitute({'num':7, 'title':'Strings'}))
print(t.substitute(dict(num=7,title='Strings')))
print(t.substitute(num=7,title='Strings'))