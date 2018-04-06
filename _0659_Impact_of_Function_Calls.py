import sys
import _0651_Timing_Iteration_Alternatives as timer

reps = 10000
repslist = list(range(reps))

def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map(lambda x: x + 10, repslist))

def genExpr():
    return list(x + 10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
print()

# Calling a user-defined function
# Unlike what book says, map is NOT fastest, even when calling a function!
def F(x): 
    return x

def forLoop2():
    res = []
    for x in repslist:
        res.append(F(x))
    return res

def listComp2():
    return [F(x) for x in repslist]

def mapCall2():
    return list(map(lambda x: F(x), repslist))

def genExpr2():
    return list(F(x) for x in repslist)

def genFunc2():
    def gen():
        for x in repslist:
            yield F(x)
    return list(gen())

print(sys.version)
for test in (forLoop2, listComp2, mapCall2, genExpr2, genFunc2):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
