import struct
path = r'.\resources\packed_data.bin'

'''
F = open(path,'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
F.write(data)
F.close()

F = open(path, 'rb')
data = F.read()
print(data)
values = struct.unpack('>i4sh', data)
print(values)
print()
'''

# File Context Managers
with open(r'.\resources\myfile.txt','r') as myfile:
    for line in myfile:
        print(line)
