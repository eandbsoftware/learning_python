S = 'ace'
for x in S:
    for y in S:
        print(x + y, end=' ')
print()

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator():
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    print()
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print()

    # Classes versus slices
    S = 'abcdef'
    for x in S[::2]:
        for y in S[::2]:
            print(x + y, end=' ')
    print()

    S = 'abcdef'
    S = S[::2]
    print(S)
    for x in S:
        for y in S:
            print(x + y, end=' ')    