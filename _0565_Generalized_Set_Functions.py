def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

s1, s2, s3 = "SPAM", "SCAM", "SLAM"
print(intersect(s1, s2))
print(union(s1, s2))
print(intersect([1, 2, 3], (1, 4)))
print(intersect(s1, s2, s3))
print(union(s1, s2, s3))
print()

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace:
            print(items)
        print(sorted(func(*items)))

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
print()
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
print()
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
print()

# Duplicates do not appear
print(intersect([1, 2, 3, 4], (1, 1, 4)))
print(union([1, 2, 3, 4], (1, 1, 4)))
print()
tester(intersect, ('ababa', 'abcdefa', 'aaaab'), False)
