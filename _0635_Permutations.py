def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            # Remove target node
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                # Add target node to front
                res.append(seq[i:i+1] + x)
        return res

def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x
'''
scramble = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print(permute1('ab'))
print()

print(list(scramble('abc')))
print(permute1('abc'))
print(list(permute2('abc')))
print()

G = permute2('abc')
print(next(G))
print(next(G))
print()

for x in permute2('abc'):
    print(x)
print()

print(permute1('spam') == list(permute2('spam')))
print((len(list(permute2('spam'))), len(list(scramble('spam')))))
print()

print(list(scramble('spam')))
print(list(permute2('spam')))
'''