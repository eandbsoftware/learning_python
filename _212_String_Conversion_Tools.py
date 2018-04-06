#S = '42' + 1
print(type(int("42")), type(str(42)), type(repr(42)))
print((int("42"), str(42), repr(42)))
print(len(repr(42)))
print()

S = "42"
I = 1
#print(S + I)
print(int(S) + I)
print(S + str(I))
print()

print((str(3.1415), float('1.5')))
text = '1.234E-10'
print(float(text))
print()

# Character code conversions
print(ord('s'))
print(chr(115))
myAscii = [chr(x) for x in range(128,256)]
#print(myAscii)
print()

S = '5'
print(ord(S))
S =chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)
print()

delta = ord('5') - ord('0')
print(delta, ord('5'), ord('0'))

# Binary string to int algo
B = '1101'
I = 0
while B != '':
    I = I * 2 + ord(B[0]) - ord('0')
    B = B[1:]
print(I)
print()

print(int('1101',2))
print(bin(13))
print()

# Changing Strings I
S = 'spam'
#S[0] = x
S = S + 'SPAM!'
print(S)
S = S[:4] + "Burger" + S[-1]
print(S)
print()

# Replace demo
S = 'splot'
S = S.replace('pl','pamal')
print(S)

# Format demo
S = 'That is %d %s bird' % (1, 'dead')
print(S)
S = 'That is {0} {1} bird'.format(1,'dead')
print(S)