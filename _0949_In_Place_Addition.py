# https://docs.python.org/2/reference/datamodel.html#object.__iadd__
#These methods should attempt to do the operation in-place (modifying self) 
# and return the result (which could be, but does not have to be, self). 
# If a specific method is not defined, the augmented assignment falls back to the normal methods.

# Takeaways:
# 1. += invokes __iadd__
# 2. __iadd__ is faster than add because it allows you to mutate an object instead of creating a new one
# 3. __add__ is a fallback to __iadd__

# += mutates in place, much faster than +
# Makes sense, since I don't have to create a new object.
# a = [1, 2, 3]
# b = a
# print(a, id(a))
# print(b, id(b))
# b += [1, 2, 3]
# print(a, id(a))
# print(b, id(b))
# print()

# # + performs addition and assigns to existing name; slower
# c = [1, 2, 3]
# d = c
# print(c, id(c))
# print(d, id(d))
# d = d + [1, 2, 3]
# print(c, id(c))
# print(d, id(d))
# print()

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        # Just mutate existing object
        self.val += other
        # Have to return something, usually, self.
        return self
    def __add__(self, other):
        # Create a new object to propagate class type
        return Number(self.val + other)

# x = Number(5)
# # calls: x.__add__(1) => 5.__add__(1) => Number.__init__(6)
# x = x + 1
# # calls: x.__iadd__(1)
# x += 1
# print(x.val)

# y = Number([1])
# y += [2]
# y += [3]
# print(y.val)

class NumberAddOnly:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return NumberAddOnly(self.val + other)

# # __add__ runs as a fallback for __iadd__
# x = NumberAddOnly(5)
# x += 1
# x += 1
# print(x.val)

# y = NumberAddOnly([1])
# y += [2]
# y += [3]
# print(y.val)

if __name__ == '__main__':
    import timeit
    print('__iadd__ with Number(int)', timeit.timeit('z+=1', setup='from _0949_In_Place_Addition import Number;z=Number(1)', number=100000))
    print('__add__ with Number(int)', timeit.timeit('z=z+1', setup='from _0949_In_Place_Addition import Number;z=Number(1)', number=100000))
    print()

    print('__iadd__ with Number(list)', timeit.timeit('z+=[2]', setup='from _0949_In_Place_Addition import Number;z=Number([1])', number=100000))
    print('__add__ with Number(list)', timeit.timeit('z=z+[1]', setup='from _0949_In_Place_Addition import Number;z=Number([1])', number=100000))
    print()

    # With __add__ as fallback, += and + take the same amount of time
    print('+= with NumberAddOnly(int)', timeit.timeit('z+=1', setup='from _0949_In_Place_Addition import NumberAddOnly;z=NumberAddOnly(1)', number=100000))
    print('+ with NumberAddOnly(int)', timeit.timeit('z=z+1', setup='from _0949_In_Place_Addition import NumberAddOnly;z=NumberAddOnly(1)', number=100000))
    
