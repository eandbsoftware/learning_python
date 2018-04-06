# A First Detailed Look
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)

# Comprehension
L = [x + 10 for x in L]
print(L)

# Equivalent
res = []
for x in L:
    res.append(x + 10)
print(res)
print()

# Using List Comprehensions on Files
path = r'.\resources\script2_0433.py'
f = open(path)
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

lines = [line.rstrip() for line in open(path)]
print(lines)
print()

print([line.upper() for line in open(path)])
print([line.rstrip().upper() for line in open(path)])
print([line.split() for line in open(path)])
print([line.replace(' ','!') for line in open(path)])
print([('sys' in line, line[:5]) for line in open(path)])