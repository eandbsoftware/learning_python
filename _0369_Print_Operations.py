import sys
# Use stdout as a file
sys.stdout.write("hello world!")

# The 3.X print function in action
print()

x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)

# Send an alternative separator
print(x, y, z, sep='')
print(x, y, z, sep=', ')
print()

# Pass a different terminator
print(x, y, z, end='')
print(x, y, z)
print(x, y, z, end='...\n')
print()

# Both
print(x, y, z, sep='...', end='!\n')
# keyword order doesn't matter
print(x, y, z, end='!\n', sep='...')
print()

# file keyword
path = r'.\resources\data_0372.txt'
print(x, y, z, sep='...', file=open(path, 'w'))
print(x, y, z)
print(open(path, 'r').read())
print()

# Display more specific formatting
text = "%s: %-.4f, %05d" % ('Result', 3.14159, 42)
print(text)
print("%s: %-.4f, %05d" % ('Result', 3.14159, 42))