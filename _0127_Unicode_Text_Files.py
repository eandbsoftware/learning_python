S = 'sp\xc4m'
print(S)
print(S[2])
print(ord(S[2]))
print()

# Write text encoded as utf-8
file = open(r'.\resources\unidata.txt','w',encoding='utf-8')
print(file.write(S))
file.close()


# Read text encoded as utf-8
text = open(r'.\resources\unidata.txt', 'r', encoding='utf-8').read()
print(text)
print(len(text))
print()

# Read raw bytes
raw = open(r'.\resources\unidata.txt','rb').read()
print(raw)
print(len(raw))
print()

# Encode and decode manually
print('encoded=', text.encode('utf-8'))
print('decoded=', raw.decode('utf-8'))
print()

# Use different encodings on same text
print(text.encode('latin-1'))
print(text.encode('utf-8'))
print(text.encode('utf-16'))
print()

print((len(text.encode('latin-1')), len(text.encode('utf-16'))))
print()

#Decode bytes
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))

print(ord('Ā'))

# hx = '0123456789abcedf'
# for l in hx:
#     for r in hx:
#         s = r'\x' + l + r
#         print(s)
