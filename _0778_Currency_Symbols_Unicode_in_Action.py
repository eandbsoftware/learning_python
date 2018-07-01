from _0775_Example_Dual_Mode_Code.formats import commas, money

X = 54321.987

print(money(X), money(X, 0, ''))

# Specify a unicode string (just a regular str in 3.X) with a hex or unicode escape
print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))

# Decode (to a unicode string) an encoded byte string using a particular encoding
print(money(X, currency=b'\xA3'.decode('latin-1')))

# A unicode string specyfing a code point using a unicode escape (decimal 8364), a byte string with the character encoded using iso8859-15
print(money(X, currency=u'\u20AC'), money(X, 0, b'\xA4'.decode('iso8859-15')))

# \xA4 is different in latin-1 and iso8859-15 encodings
print(money(X, currency=b'\xA4'.decode('latin-1')))

