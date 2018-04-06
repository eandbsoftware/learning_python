def sumTree(L):
    tot = 0
    for x in L:
        print(x)
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumTree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumTree(L))
print()

M = [1, [2, [3, [4, 5]]]]
print(sumTree(M))
print()

N = [[[[[1], 2], 3], 4], 5]
print(sumTree(N))
print()

def sumTreeBreadth(L):
    tot = 0
    items = list(L)
    while items:
        first = items.pop(0)
        if not isinstance(first, list):
            print(first, end=', ')        
            tot += first
        else:
            items.extend(first)
    return tot

print(sumTreeBreadth(L))
print(sumTreeBreadth(M))
print(sumTreeBreadth(N))
print()

def sumTreeDepth(L):
    tot = 0
    items = list(L)
    while items:
        first = items.pop(0)
        if not isinstance(first, list):

            print(first, end=', ')
            tot += first
        else:
            items[:0] = first
    return tot

print(sumTreeDepth(L))
print(sumTreeDepth(M))
print(sumTreeDepth(N))
print()

# Recursion Limits
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(9999)
print(sys.getrecursionlimit())
help(sys.setrecursionlimit)