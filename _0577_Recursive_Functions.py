# Summation with Recursion

def mySum(L, debug=False):
    if debug: print(L)
    if not L:
        return 0
    else:
        return L[0] + mySum(L[1:], True)

print(mySum([1, 2, 3, 4, 5], True))
print()

# Coding Alternatives
def mySum2(L):
    return 0 if not L else L[0] + mySum2(L[1:])
print(mySum2([1, 2, 3, 4, 5]))

def mySum3(L):
    return L[0] if len(L) == 1 else L[0] + mySum3(L[1:])
print(mySum3([1, 2, 3, 4, 5]))

def mySum4(L):
    first, *rest = L
    return first if not rest else first + mySum4(rest)
print(mySum4([1, 2, 3, 4, 5]))
print()

print(mySum2([]))
print(mySum4([1]))
print(mySum4([1, 2, 3, 4, 5]))
print(mySum4(['s', 'p', 'a', 'm']))
print(mySum4('spam'))
print(mySum4(['spam', 'ham', 'eggs']))
print()

# Indirect Recursion
def mySum5(L):
    if not L:
        return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + mySum5(L[1:])

print(mySum5([1, 2, 3, 4, 5]))
print()

# Loop Statements Versus Recursion
L = [1, 2, 3, 4, 5]
def sumWhile(L):
    sum = 0
    while L:
        sum += L[0]
        L = L[1:]
    return sum
print(sumWhile(L))

def sumFor(L):
    sum = 0
    for x in L:
        sum += x
    return sum
print(sumFor(L))

print(sum(L))