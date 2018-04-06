lc = [x ** 2 for x in range(4)]
print(lc)
print()

ge = (x ** 2 for x in range(4))
print(ge)
print(list(ge))
print()

same = list(x ** 2 for x in range(4))
print(same)
print()

# Generator expressions support the iteration protocol
G = (x ** 2 for x in range(4))
print(iter(G) is G)
print(next(G))
print(G.__next__())
print(next(G))
print(next(G))
#print(next(G))
print()

print(G)
print()

# Iteration contexts automatically trigger iteration protocol
# Comprehensions\generators are iteration contexts AND can be used in an iteration context!
for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2.0))
print()

cat = ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
print(cat)

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(repr(a), repr(c))
print(a, c, sep='%')

# Extra parenthesis are not always required
s1 = sum(x ** 2 for x in range(4))
print(s1)
print()

s2 = sorted(x ** 2 for x in range(4))
print(s2)

s3 = sorted((x ** 2 for x in range(4)), reverse=True)
print(s3)
