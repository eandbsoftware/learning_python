line = 'aa bbb c'
# generator
res = ''.join(x for x in line.split(' ') if len(x) > 1)
print(res)
# filter
res = ''.join(filter(lambda x: len(x) > 1, line.split(' ')))
print(res)
print()

# generator
res = ''.join(x.upper() for x in line.split(' ') if len(x) > 1)
print(res)
# map and filter
res = ''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split(' '))))
print(res)
print()

# Statement-based alternative
res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)