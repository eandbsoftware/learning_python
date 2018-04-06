import timeit

'''
# Interactive usage and API calls
print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)))
print()

# Timing multiline statements
print(min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1")))
print(min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")))
print(min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]")))
print()

# Other usage modes: Setup, totals, and objects
print(min(timeit.repeat(number=1000, repeat=3,
    setup='from _0562_The_min_Wakeup_Call import min1, min2, min3\n'
    'vals=list(range(1000))', 
    stmt='min3(*vals)')))
print(min(timeit.repeat(number=1000, repeat=3,
    setup='from _0562_The_min_Wakeup_Call import min1, min2, min3\n'
    'import random\nvals=[random.random() for i in range(1000)]',
    stmt='min3(*vals)')))
print()
'''

# Total time
number = 1000
total_time = timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=number)
# This is a convenience function that calls the timeit() repeatedly, returning a list of results.
repeat_time = timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=number, repeat=5)
print('total_time = {0}, repeat_times = {1}'.format(total_time, repeat_time))
print()

# Class API
timer = timeit.Timer(stmt='[x ** 2 for x in range(1000)]')
# Create a Timer instance with the given statement...
print(timer.timeit(1000))
print()

# The static way
print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=3))
print()

# Passing callable object instead
def testcase():
    y = [x ** 2 for x in range(1000)]
print(timeit.repeat(testcase, number=1000, repeat=3))