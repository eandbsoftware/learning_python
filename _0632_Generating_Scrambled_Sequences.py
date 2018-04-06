# Scrambling sequences
L, S = [1, 2, 3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')
print()

for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=' ')
print()

for i in range(len(S)):
    S = S[i:] + S[:i]
    print(S, end=' ')
print()
print()

# Simple functions
def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res
print(scramble('spam'))

def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]
print(scramble('spam'))

for x in scramble((1, 2, 3)):
    print(x, end=' ')
print()
print()

# Generator functions
def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq

def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

print(list(scramble('spam')))
print(list(scramble((1, 2, 3))))
for x in scramble((1, 2, 3)):
    print(x, end=' ')
print()
print()

# Generator expressions
S = 'spam'
G = (S[i:] + S[:i] for i in range(len(S)))
print(list(G))
print()

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F)
print(list(F(S)))
print(list(F((1, 2, 3))))

for x in F((1, 2, 3)):
    print(x, end=' ')
print()
print()

# Tester client
def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

def tester(func, items, trace=True):
    for args in scramble(items):
        if trace:
            print(args)
        print(sorted(func(*args)))

tester(intersect, ('aab', 'abcde', 'ababab'))
print()
tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False)
            