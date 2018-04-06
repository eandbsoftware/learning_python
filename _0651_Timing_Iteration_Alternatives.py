"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-total time.
"""
# Timing Module: Homegrown
import time
def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start
'''
print(timer(pow, 2, 1000))
print(timer(str.upper, 'spam'))
print()
'''
import sys
timer = time.clock if sys.platform[:3] == 'win' else time.time
def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    replist = list(range(reps))
    start = timer()
    for i in replist:
        ret =func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
'''
# total
# Take first element only because result is really big
print(total(1000, pow, 2, 1000)[0])
print(total(1000,str.upper, 'spam'))
print()

# bestof
# Result in book ommits exponent?
print(bestof(1000, pow, 2, 1000)[0])
print(bestof(1000, str.upper, 'spam'))
print()

# bestoftotal
# (A, (B, C)) Ok that B > A, because B is just the last iteration
print(bestof(50, total, 1000, str.upper, 'spam'))
print(bestoftotal(50, 1000, str.upper, 'spam'))
print()

# min
print(min(total(1000, str.upper, 'spam') for i in range(50)))
print()

# New timer calls in 3.3
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.version[:3] == 'win' else time.time

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.clock if sys.version[:3] == 'win' else time.time

print(timer is time.perf_counter)
'''