import sys 
import _0651_Timing_Iteration_Alternatives as timer
reps = 1000
replist = list(range(reps))

def forLoop():
    res = []
    for i in replist:
        res.append(i ** 2)
    return res

def listComp():
    return [i ** 2 for i in replist]

def mapCall():
    return list(map(lambda i: i ** 2,replist))

def genExpr():
    return list(i ** 2 for i in replist)

print(sys.version)
print('Homegrown timer:')
for test in (forLoop, listComp, mapCall, genExpr):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))


