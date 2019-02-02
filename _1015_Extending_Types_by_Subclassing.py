# Map 1...N to 0...N-1; call back to build-in version.
class MyList(list):
    def __getitem__(self, index):
        print('(indexing %s at %s' % (self, index))
        return list.__getitem__(self, index - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)

    # Uses MyList.__getitem__ to customize list superclass method
    print(x[1])
    print(x[3])

    # Inherits attributes from list superclass
    x.append('spam'); print(x)
    x.reverse(); print(x)

class MySet(list):
    def __init__(self, value=[]):
        # value must be iterable else concat with raise an exception
        # default value for value is necessary to construct an empty MySet without passing an empty list
        list.__init__(self)
        self.concat(value)

    def intersect(self, other):
        # Returns a new MySet instance.
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return MySet(res)

    def union(self, other):
        # Returns a new MySet instance.
        # self argument here is value parameter in constructor (not the implicit self parameter).
        res = MySet(value=self)
        res.concat(other)
        return res

    def concat(self, value):
        # Mutates self instance (and its only ever mutated here, not in constructor)
        # Does not add duplicates to self (necessary in case source iterable contains duplicates)
        for x in value:
            if x not in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'MySet:' + list.__repr__(self)

if __name__ == '__main__':
    x = MySet([1, 3, 5, 7])
    y = MySet([2, 1, 4, 5, 6])
    z = MySet([0, 1, 1, 1])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    print(y & x, y | x)
    x.reverse(); print(x)