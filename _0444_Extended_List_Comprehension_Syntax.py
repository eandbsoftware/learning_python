# Filter clauses: if
path = r'.\resources\script2_0433.py'
lines = [line.rstrip() for line in open(path) if line[0] == 'p']

print(lines)

# for equivalent
res = []
for line in open(path):
    if line[0] == 'p':
        res.append(line.rstrip())
print(res)

# appending/indenting
lines = [line.rstrip() for line in open(path) if line[0] == 'p' if '32' in line]
print(lines)

lines = [line.rstrip() for line in open(path) if line.rstrip()[-1].isdigit()]
print(lines)
print()

# Nested loops: for
combos = [x + y for x in 'abc' for y in 'xyz']
print(combos)

# for equivalent
res = []
for x in 'abc':
    for y in 'xyz':
        res.append(x + y)
print(res)