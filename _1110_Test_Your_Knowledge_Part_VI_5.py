# Problem 5
class Set(list):
    def __init__(self, value=[]):
        list.__init__(self)
        self.concat(value)

    def intersect(self, other):
        both = []
        for x in self:
            if x in other:
                both.append(x)
                continue
        return Set(both)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):
        for x in value:
            if x not in self:
                self.append(x)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + list.__repr__(self)

'''
s1 = Set([1, 2, 3, 5, 8])
s2 = Set([2, 3, 4, 5, 7, 8])

# a.
intersection = s1 & s2
print(intersection)
union = s1 | s2
print(union)
print()

# b. list.__getitem__
str_set = Set('jason')
a = str_set[1]
print(a)
print()

# c. list.__iter__
cat = '-'.join(c for c in str_set)
print(cat)
print()

# d. Yes
print(str_set & 'son')
print(str_set | 'gastelum')
'''

class MultiSet(Set):
    def intersect(self, *others):
        for other in others:
            self = Set.intersect(self, other)
        return self

    # def multi_intersect(self, *others):
    #     res = []
    #     for x in self:
    #         for other in others:
    #             if x not in other:
    #                 break
    #         else:
    #             res.append(x)
    #     return MultiSet(res)
        
    def union(self, *others):
        for other in others:
            self = Set.union(self, other)
        return self

    # def multi_union(*args):
    #     res = [x for arg in args for x in arg]
    #     return MultiSet(res)

x = MultiSet([1, 2, 3, 4])
y = MultiSet([3, 4, 5])
z = MultiSet([0, 1, 2])

print(x & y, x | y)
print(x.union(y))

print(x.intersect(y,z))
print(x.union(y, z))
print(x.intersect([1, 2, 3], [2, 3, 4], [1, 2, 3]))
print(x.union(range(10)))

w = MultiSet('spam')
print(w)
print(''.join(w | 'super'))
print((w | 'super') & MultiSet('slots'))