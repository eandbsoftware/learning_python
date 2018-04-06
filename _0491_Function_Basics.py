'''
# A First Example: Definitions and Calls
def times(x, y):
    return x * y

print(times(2, 4))
x = times(3.14, 4)
print(x)
print(times('Ni', 4))
'''

# A Second Example: Intersecting Sequences
def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = 'SPAM'
s2 = 'SCAM'
print(intersect(s1,s2))
print([x for x in s1 if x in s2])

# Function is polymorphic, i.e., it works on arbitrary types, as long as they support the expected interface
x = intersect([1, 2, 3], (3, 4))
print(x)