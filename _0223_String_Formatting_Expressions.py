print('That is %d %s bird' % (1,'dead'))
exclamation = 'Ni'
print('The knights who say %s!' % exclamation)
print('%d %s %g you' % (1, 'spam', 4.0))
print('%s -- %s -- %s' % (42, 3.1415, [1, 2, 3]))
print()

# Advanced Formatting Expression Examples
x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)

x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
print('%E | %F | %G' % (x, x, x))
print()

print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print( '%s' % x, str(x))
print()

print('%f, %.2f, %.*f' % (1 / 3.0, 1 / 3.0, 3, 1 / 3.0))
print()

# Dictionary-Based Formatting Expressions
print('%(qty)d more %(food)s' % {'qty' : 1, 'food' : 'spam'})

reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name' : 'jason', 'age' : 38 }
print(reply % values)
print()

food = 'spam'
qty = 10
#print(vars())
print('%(qty)d more %(food)s' % vars())