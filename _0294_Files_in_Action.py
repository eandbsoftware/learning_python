path = r'.\resources\'myfile.txt'

'''
myfile = open(path,'w')
print(type(myfile))
print(myfile.write('hello text file\n'))
print(myfile.write('goodbye text file\n'))
myfile.close()

myfile = open(path,'r')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())


print(open(path,'r').read())

for line in open(path,'r'):
    print(line, end='')
'''

'''
# Text and Binary Files
myfile = open(r'.\resources\data287.bin','wb')
print(myfile.write(b'\x00\x00\x00\x07spam\x00\x08'))
myfile.close()

data = open(r'.\resources\data287.bin','rb').read()
print(data)
print(data[4:8])
print(data[4:8][0])
print(bin(data[4:8][0]))
'''

# Storing Python Objects in Files
path = r'.\resources\datafile.txt'
"""
X, Y, Z = (43, 44, 45)
S = 'Spam'
D = {'a' : 1, 'b' : 2}
L = [1, 2, 3]

F = open(path, 'w')
F.write(S + '\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '%' + str(D) + '\n')
F.close()

chars = open(path, 'r').read()
print(chars)

F = open(path, 'r')
line = F.readline()
print(line)
line = line.rstrip()
print(line)
print()

line = F.readline()
print(line)
parts = line.split(',')
print(parts)
print(int(parts[1]))
numbers = [int(n) for n in parts]
print(numbers)
print()

line = F.readline()
print(line)
parts = line.split('%')
print(parts)
print(eval(parts[0]))
objects = [eval(p) for p in parts]
print(objects)
print(objects[1]['b'])
"""

# Storing Native Python Objects: pickle
pickle_path = r'.\resources\datafile.pkl'
"""
D = {'a' : 1, 'b' : 2}
F = open(pickle_path, 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open(pickle_path, 'rb')
E = pickle.load(F)
print(E)
print(E['b'])

print(open(pickle_path, 'rb').read())
"""

# Storing Python Objects in JSON Format
import json
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
path = r'.\resources\testjson.txt'
'''
print(rec)

print(json.dumps(rec))
S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)
print(O == rec)
print(O['name']['first'])
print()
'''

json.dump(rec, fp=open(path,'w'), indent=4)
print(open(path, 'r').read())

p = json.load(open(path,'r'))
print(p)
print(p['name']['first'])