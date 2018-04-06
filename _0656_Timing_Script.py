# File timeseqs.py
"Test the relative speed of iteration tool alternatives."

import sys 
import _0651_Timing_Iteration_Alternatives as timer
reps = 10000
replist = list(range(reps))

def forLoop():
    res = []
    for i in replist:
        res.append(abs(i))
    return res

def listComp():
    return [abs(i) for i in replist]

def mapCall():
    return list(map(abs,replist))

def genExpr():
    return list(abs(i) for i in replist)

def genFunc():
    def gen():
        for i in replist:
            yield abs(i)
    return list(gen())

'''
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
'''