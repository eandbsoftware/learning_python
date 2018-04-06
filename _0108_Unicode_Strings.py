# 3.X: normal strings are unicode text
print('sp\xc4m')

# bytes strings are byte-based data
print(b'a\x01c')

# The 2.X Unicode literal works in 3.3+: just str
print(u'sp\u00c4m')

print('spam'.encode('utf8'))
print('spam'.encode('utf16'))

print('sp\xc4\u00c4\U000000c4m')

print('\u00A3')
print('\u00A3'.encode('latin1'))
print(b'\xA3'.decode('latin1'))

# Python 3.X never allows normal strings and bytes to mix
# Fails in 3.X
#print(u'x' + b'y')
print(u'x' + 'y')

# Decode bytes to str
print('x' + b'y'.decode())

# Encode str to bytes
print('x'.encode() + b'y')