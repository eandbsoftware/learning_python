import os

'''
# Read line by line
F = os.popen('dir')
print(F.readline().rstrip())
F.close()
print()

# Read by sized blocks
F = os.popen('dir')
print(F.read(50))
F.close()
print()

# Read all lines and index
print(os.popen('dir').readlines()[0].rstrip())
print()

# Read all at once and slice
print(os.popen('dir').read()[:50])
print()

# File line iterator loop
print('---for---')
for line in os.popen('dir'):
    print(line.rstrip())

# Doesn't do anything in VS Code
os.system('systeminfo')

for line in os.popen('systeminfo'):
    print(line.rstrip())

for (i, line) in enumerate(os.popen('systeminfo')):
    if i == 4:
        break
    print('%05d) %s' % (i, line.rstrip()))
print()

for line in os.popen('systeminfo'):
    parts = line.split(':')
    if parts and parts[0].lower() == 'system type':
        print(parts[1].strip())

# awk emulation: extract column 7 from whitespace-delimited file
path = r'.\resources\input_428.txt'
for val in [line.split()[6] for line in open(path)]:
    print(val)

# Retain result
col7 = []
for line in open(path):
    cols = line.split()
    col7.append(cols[6])
for item in col7:
    print(item)

# Reuseable
def awker(file, col):
    return [line.rstrip().split()[col - 1] for line in open(file)]
print(awker(path, 7))
print(','.join(awker(path,7)))

'''
from urllib.request import urlopen
for line in urlopen('http://learning-python.com/books'):
    print(line)