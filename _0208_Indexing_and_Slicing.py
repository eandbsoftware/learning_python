# Basic operations
print(len('abc'))
print('abc' + 'def')
print('Ni!' * 4)
print('-' * 80)
print()

myjob = 'hacker'
for c in myjob:
    print(c, end=' ')
print()
print("k" in myjob)
print("z" in myjob)
print("spam" in 'abcspamdef')
print()

# Indexing and slicing
S = 'Spam'
print(S[0])     # S
print(S[-2])    # a
print(S[1:3])   # pa
print(S[1:])    # pam
print(S[:-1])   # spa
print()

# Extended slicing
import string
S = string.ascii_lowercase
print(S)
print(S[1:10:2])
print(S[::2])
print()

H = 'hello'
print(H[::-1])

# Reversing a string
S = 'abcdefg'
print(S[5:1:-1])
print()

# Slicing is equivalent to indexing with a slice object
S = 'spam'
print(S[1:3])
print(S[slice(1, 3)])
print(S[::-1])
print(S[slice(None,None,-1)])