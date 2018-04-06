# Generator expression
G = (c * 4 for c in 'SPAM')
print(G)
print(list(G))

# Generator function
def timesfour(S):
    for c in S:
        yield c * 4
G = timesfour('spam')
print(G)
print(list(G))
print()

# Iterate generator expression manually
G = (c * 4 for c in 'SPAM')
I = iter(G)
print(next(I))
print(next(I))

G = timesfour('spam')
I = iter(G)
print(next(I))
print(next(I))
print()

line = 'aa bbb c'
S = ''.join(x.upper() for x in line.split() if len(x) > 1)
print(S)

def gensub(line):
    for c in line.split():
        if len(c) > 1:
            yield c.upper()

S = ''.join(gensub(line))
print(S)