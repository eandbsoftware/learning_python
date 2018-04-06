# Write a file
# f = open(r'.\resources\data.txt', 'w')
# print(f.write('hello\n'))
# print(f.write('world\n'))
# f.close()
"""
# Read a file
f = open(r'.\resources\data.txt', 'r')
text = f.read()
print(text)

# Files are iterable
words = [w for w in open(r'.\resources\data.txt')]
print(words)

#print(dir(f))
#print(help(f.seek))
"""
# Binary Bytes Files
import struct
# packed = struct.pack('>i4sh', 7, b'spam', 8)
# print(packed)
# g = open(r'.\resources\data.bin', 'wb')
# print(g.write(packed))
# g.close()

data = open(r'.\resources\data.bin','rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh',data))

#print(help(struct))

