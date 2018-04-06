X = 1
print(X<<2)     # 4
print(X|2)      # 3 0b11
print(X&1)      # 1
print()

# every bit-shift is a power of 2
# for i in range(10):
#     print(X,bin(X))
#     X = X << 1

X = 0b0001
print(X<<2)
print(bin(X<<2))
print()

print(bin(X | 0b010))
print(bin(X & 0b1))
print()

X = 0xFF
print(bin(X))
print(X ^ 0b10101010)
print(bin(X ^ 0b10101010))
print(int('1010101',2))
print(hex(85))
print()

X = 99
print(bin(X), X.bit_length(), len(bin(X))-2)
print(bin(256),(256).bit_length(),len(bin(256))-2)