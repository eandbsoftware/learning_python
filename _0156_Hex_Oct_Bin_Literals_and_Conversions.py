# Octal literals
print(0o1,0o20,0o377)

# Hex literals
print(0x01, 0x10, 0xFF)

# Binary literals
print(0b1, 0b10000, 0b11111111)

# Converting to base-10
print(0xFF, 15*(16**1) + 15*(16**0))
print(0x2F, 2*(16**1) + 15*(16**0))
print(0xF, 15*(16**0))
print()

# Convert from base-10 int to string of another base (int -> string)
print(oct(64), hex(64), bin(64))
print(int(oct(64), 8), int(hex(64), 16), int(bin(64), 2))
print()

# Converting from other base string to base-10 int (string -> int)
print(64, 0o100, 0x40, 0b1000000)
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('64'), int('0o100', 8), int('0x40', 16), int('0b1000000', 2))
print()

# Using eval to convert from string to int
print(type(eval('64')))
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
print()

# Using string formatting
S1 = '{0:o},{1:x},{2:b}'.format(64,64,64)
print(S1)
S2 = '%o, %x, %x, %X' % (64,64,255,255)
print(S2)
print()

X = 0xFFFFFFFFFFFFFFFFFFFFFF
print(X)
print(oct(X))
print(bin(X))