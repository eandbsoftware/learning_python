T = (1,2,3,4)
print(len(T))
print(T + (5,6))
print(T[0])
print(T[:2])
print(T.index(4))
print(T.count(4))
# Tuples are immutable
#T[0] = 2
T = (2,) + T[1:]
print(T)
T = 'spam', 3.0, [11,22,33]
print(T[1])
print(T[2][1])
