'''
# Basic usage
for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')
print()

sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item
print(prod)
print()

# Other data types
S = 'lumberjack'
T = ("and", "I'm", "okay")
for x in S:
    print(x, end=' ')
print()

for x in T:
    print(x, end=' ')
print()
print()

# Tuple assignment in for loop
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print('a =', a, ', b=', b)
print()

D = {'a' : 1, 'b' : 2, 'c' : 3}
for key in D:
    print(key, '=>', D[key])
print()

print(list(D.items()))
print()

for k,v in D.items():
    print('key = {0}, value={1}'.format(k, v))
print()

# Assign manually within the loop to unpack
for both in T:
    a, b = both
    print(a, b)
print()

# Nested sequences work too
((a, b), c) = ((1, 2), 3)
print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
print()

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)
print()

# Extended sequence assignments
a, b, c = 1, 2, 3
print(a, b, c)
print()

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
print()

a, *b, c = 1, 2, 3, 4
print(a, b, c)
print()

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
print()

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(all[0], all[1:3], all[3])

# Nested for loops
items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if key == item:
            print(key, 'was found')
            break
    else:
        print(key, 'was not found')
print()

for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'was not found')
print()

seq1 = 'spam'
seq2 = 'scam'

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)

# Classic list comprehension pattern
lc = [x for x in seq1 if x in seq2]
print(lc)
'''

# Why You Will Care: File Scanners
path = r'.\resources\test_0415.txt'
file = open(path, 'w')
text = '''
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae 
dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam 
est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non numquam [do] 
eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad 
minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea 
commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil 
molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?
'''
file.write(text)
file.close()

'''
# 1. Read entire file into memory with read()
file = open(path,'r')
print(file.read())
file.close()

# 2. Read one char at a time with read(arg)/while
file = open(path,'r')
while True:
    char = file.read(1)
    if not char:
        break
    print(char, end='$')
file.close()
print()

# 3. Read entire file, but iterate over characters with read/for
for char in open(path,'r').read():
    print(char, end='%')
print()

# 4. Read by line with readline/while
file = open(path, 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line.rstrip())
file.close()
print()

# 5. Read binary file by bytes with read(arg)/while
file = open(path,'rb')
while True:
    chunk = file.read(10)
    print(chunk)
    if not chunk:
        break
file.close()
print()
'''

# 6. Read by line with readlines()/for
for line in open(path,'r').readlines():
    print(line.rstrip())
file.close()

# 7. Read by line with for (iterator)
for line in open(path,'r'):
    print(line.rstrip())
file.close()

