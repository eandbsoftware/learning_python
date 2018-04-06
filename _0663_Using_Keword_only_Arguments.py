"""
Same usage ast timer2.py, but uses 3.X keyword-only default arguments
instead of dict pops for simpler code. No need to hoist range() out
of tests in 3.X: always a generator in 3.X, and this can't run on 2.X.
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _reps, **kargs):
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

# keyword arguments appear after * and before **
def bestoftotal(func, *pargs, _reps1=5, _reps=1000, **kargs):
    return min(total(func, *pargs, _reps=2000, **kargs) for i in range(_reps1))

#print(bestoftotal(str.upper, 'spam', _reps1=100, _reps=2000))


