# https://stackoverflow.com/questions/35518986/whats-the-difference-between-yield-from-and-yield-in-python-3-3-2
def both(N):
    for i in range(N):
        yield i
    for i in (x ** 2 for x in range(N)):
        yield i

print(list(both(5)))

def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(list(both(5)))
print(' : '.join(str(i) for i in both(5)))