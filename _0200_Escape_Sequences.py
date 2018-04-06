s = 'a\nb\tc'
print(repr(s),str(s))
print(len(s))
print()

# Fun with unicode
print(repr('\a'),str('\a'))
print('\u00A3')
print(repr('\u0ED6'),str('\u0ED6'))
print('\xc6')
print('\777')
print('\u0D94')
print(repr('\u0D17'),str('\u0D17'))
print('\U0001028C')
print()

s = 'a\0b\0c'
print(repr(s),str(s))
print(len(s))
print()

s = '\001\002\x03'
print(repr(s),str(s), s)
print(len(s))
print()

s = 's\tp\na\x00m'
print(repr(s),str(s), s)
print(len(s))
print()

# bell, backspace, tab
print('\x07', '\x08', '\x09')
print(repr('\x07'), repr('\x08'), repr('\x09'))
print()

x = "C:\py\code"
print(repr(x),x)
print(len(x))
print()

print(repr('\x00'),'\x00')
print(repr('\x01'),'\x01')
print(repr('\x02'),'\x02')
print(repr('\x03'),'\x03')
print(repr('\x04'),'\x04')
print(repr('\x05'),'\x05')
print(repr('\x06'),'\x06')
print(repr('\x07'),'\x07')
print(repr('\x08'),'\x08')
print(repr('\x09'),'\x09')
print(repr('\x0A'),'\x0A')
print(repr('\x0B'),'\x0B')
print(repr('\x0C'),'\x0C')
print(repr('\x0D'),'\x0D')
print(repr('\x0E'),'\x0E')
print(repr('\x0F'),'\x0F')

print(repr('\x10'),'\x10')
print(repr('\x11'),'\x11')
print(repr('\x12'),'\x12')
print(repr('\x13'),'\x13')
print(repr('\x14'),'\x14')
print(repr('\x15'),'\x15')
print(repr('\x16'),'\x16')
print(repr('\x17'),'\x17')
print(repr('\x18'),'\x18')
print(repr('\x19'),'\x19')
print(repr('\x1A'),'\x1A')
print(repr('\x1B'),'\x1B')
print(repr('\x1C'),'\x1C')
print(repr('\x1D'),'\x1D')
print(repr('\x1E'),'\x1E')
print(repr('\x1F'),'\x1F')

print(repr('\x20'),'\x20')
print(repr('\x21'),'\x21')
print(repr('\x22'),'\x22')
