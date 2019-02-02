class MySet:
    def __init__(self, value=[]):
        # value must be iterable
        # default value a convenience for creating empty MySet
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return MySet(res)

    def union(self, other):
        # Make a copy of self.data
        # res = self.data[:]
        # for x in other:
        #     if x not in res:
        #         res.append(x)
        # return MySet(res)

        #Why not implement as in setsubclass?
        # res = MySet(self.data[:])
        # res.concat(other)
        # return res

        # Or just be lazy and let MySet.concat deal with duplicates
        return MySet(self.data[:] + other.data[:])

    def concat(self, value):
        # Does not add duplicates to self.data
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'MySet:' + repr(self.data)
    def __iter__(self): return iter(self.data)

x = MySet([1, 3, 5, 7])
print(x.union(MySet([1, 4, 7])))
print(x | MySet([1, 4, 7]))