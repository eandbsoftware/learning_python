S = 'Spam'
print(len(S))
print(S[0])
print(S[1])

# Fromally, a negative index is simply added to the string's length
print(S[-1])
print(S[len(S)-1])

# X[I:J] - give me everything in X from offset I up to but not including offset J
print(S[1:3])

# The left bound defaults to zero, and the right bound defaults to the length of the sequence
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])

# Strings are immutable and do not support item assignment
#S[0] = 'z'
S = 'z' + S[1:]
print(S)

#You can change non-string, text-based data in-place...
#...using a list of characters
S = 'shrubbery'
L = list(S)
print(L)
L[1] = 'c'
print(''.join(L))

#...or with a bytearray
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())

# string methods
S = 'spam'
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

S = 'spam'
print(S.upper())
print(S.isalpha())

line = 'aaa,bbb,ccccc,dd\n'
print(line)
print('next')
print(line.rstrip().split('x'))
print('next')

#formatting
f = '%s, eggs, and %s' % ('spam', 'SPAM')
print(f)

print('{0}, eggs, and {1}'.format('spam', 'SPAM'))
print('{}, eggs, and {}'.format('spam', 'SPAM'))

#More to come on advanced formatting
print('{:.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

# Getting help
# List all the variables in the caller's scope
print(dir())

# List all the attributes of the object passed
print(dir(str) == dir(S))

# Prints the PyDoc for the passed attribute
help(S.replace)

# Prints ALL the PyDoc for the passed type
#help(str)

# Other ways to code strings
S = 'A\nB\nC'
print(len(S))
print(ord('\a'))
S = 'A\0B\0C'
print(len(S))
print(S)

msg = """
aaaaaaaaa
bbb'''bbbbbbbbb""bbbbbbb'bbbb
ccccccccccc
"""
print(msg)
print('next')
print(r'C:\text\new')
