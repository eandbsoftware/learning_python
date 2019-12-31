def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

def g(x):
    if __debug__:
        if not (x < 0):
            raise AssertionError('x must be negative')
    return x ** 2

if __name__ == '__main__':
    print(f'{__debug__=}')
    print(f(1))
    #print(g(1))