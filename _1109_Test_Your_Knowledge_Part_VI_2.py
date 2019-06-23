#Question 2
class MyList:
    def __init__(self, start):
        # That's heavy!
        # This constructor can take either a list or another MyList 
        # (or anything iterable for that matter) as an argument!!!
        self.wrapped = list(start)
        
        # slicing a string returns a new string, not a list
        # so delegating to methods expected on a list fails.
        # But using list() will make a new list, even from
        # a string
        #self.wrapped = start[:]

    def __add__(self, other):
        return MyList(self.wrapped.__add__(other))

    def __mul__(self, time):
        return MyList(self.wrapped.__mul__(time))

    def __getitem__(self, index):
        return self.wrapped.__getitem__(index)

    def __len__(self):
        return self.wrapped.__len__()
    
    def __iter__(self):
        return self.wrapped.__iter__()

    def append(self, obj):
        # Assuming that self.wrapped is a list
        self.wrapped.append(obj)
    
    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

    def __repr__(self):
        return repr(self.wrapped)

x = MyList('spam')
print(x)
print(x[2])
print(x[1:])
# Can add a MyList and regular list
print(x + ['eggs'])
print(x * 3)
x.append('a')
x.sort()
func = x.count
print(func('a'))
print(x)
print(' '.join(c for c in x))
print()

for i in x:
    print(i)
# Can make a MyList from a MyList
y = MyList(x)
# CANNOT add a regular list and MyList
print([1, 2, 3] + x)

'''
# Question 3
def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print(f'{oncall.calls} total calls')
        return func(*args)
    oncall.calls = 0
    return oncall
    
class MyListSub(MyList):
    def __init__(self, start):
        self.calls = 0
        MyList.__init__(self, start)
    # Method is a class member shared by everyone, thus it counts all invocations
    # Decorator is invoked once, at class definition time
    #__add__ = tracer(__add__)
    @tracer
    def __add__(self, other):
        self.calls += 1
        print(f'{self.calls} instance calls')        
        return MyList.__add__(self, other)    
    
x = MyListSub([1, 2, 3])
x + ['hayden']
x + [40]
x + ['jason']
print(x)
print()

y = MyListSub(['a', 'b', 'c'])
y + [1]
'''