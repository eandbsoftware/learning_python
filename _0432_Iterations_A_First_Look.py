for x in [1, 2, 3, 4]:
    print(x**2, end=' ')
print()

for x in (1, 2, 3, 4):
    print(x **3, end=' ')
print()

for x in 'spam':
    print(x * 2, end=' ')
print()

path = r'.\resources\script2_0433.py'
# f = open(path,'w')
# line = '''import sys
# print(sys.path)
# x = 2
# print(x ** 32)
# '''
# f.write(line)
# f.close()

print(open(path,'r').read())
print(repr(open(path,'r').read()))
print()

f = open(path,'r')
print(repr(f.readline()))
print(repr(f.readline()))
print(repr(f.readline()))
print(repr(f.readline()))
print(repr(f.readline()))
print()
f.close()

f = open(path,'r')
print(repr(f.__next__()))
# or use next() built in
print(repr(next(f)))
print(repr(f.__next__()))
print(repr(f.__next__()))
try: 
    print(repr(f.__next__()))
except StopIteration:
    print('caught ya!')
print()

# Preferred way
for line in open(path,'r'):
    print(line.upper().rstrip())
print()

# Reads entire file into memory:
for line in open(path,'r').readlines():
    print(line.upper().rstrip())
print()

# Read line by line with while
f = open(path,'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line.upper().rstrip())