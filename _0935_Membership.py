class Iters:
    def __init__(self, value):
        self.data = value
    
    # Preferred for index, slice
    # Fallback for iteration
    def __getitem__(self, i):
        print('get[%s]:' % i)
        return self.data[i]

    # Preferred for iteration
    # Allows only one active iterator
    # def __iter__(self):
    #     print('iter=> next:')
    #     for x in self.data:
    #         yield x
    #         print('next:')
            
    # def __iter__(self):
    #     print('iter=> ')
    #     self.ix = 0
    #     return self

    # def __next__(self):
    #     print('next:')
    #     if self.ix == len(self.data): raise StopIteration
    #     item = self.data[self.ix]
    #     self.ix += 1
    #     return item

    # Preferred for 'in'
    # def __contains__(self, x):
    #     print('contains: ')
    #     return x in self.data

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    print()

    for i in X:
        print(i)
    print()

    print([i**2 for i in X])
    print()

    print(list(map(bin, X)))
    print()

    I = iter(X)
    while True:
        try:
            print(next(I))
        except StopIteration:
            break
    print()

    X = Iters('spam')
    print(X[0])

    print('spam'[1:])
    print('spam'[slice(1, None)])

    print(X[1:])
    print(X[:-1])
    print(list(X))