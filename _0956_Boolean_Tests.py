'''
class Truth1:
    def __bool__(self):
        return True

X = Truth1()
if X: print('yes!')

class Truth2:
    def __bool__(self):
        return False

X = Truth2()
print(bool(X))

# A non-empty object is considered true
class Truth3:
    def __len__(self):
        return 1

X = Truth3()
if X: print('I am true; my length is not zero')

# If both methods are present Python prefers __bool__ over __len__
class Truth4:
    def __bool__(self):
        return True
    def __len__(self):
        return False

X = Truth4()
if X: print('yes!; I default to __bool__')

class Truth5:
    pass

X = Truth5()
print('I am true vacuously', bool(X))
'''

# Boolean Methods in 2.X    
class C:
    def __bool__(self):
        print('in __bool__')
        return False
X = C()
# In 3.X: prints 'in __bool__', then False 
# In 2.X prints True because a vacuous object is True by default
print(bool(X))
# In 3.X does NOT print 99
# In 2.X prints 99
if X: print(99)
print()

class D:
    def __nonzero__(self):
        print('in __nonzero__')
        return False
    
X = D()
# In 3.X prints True
# In 2.X prints 'in __nonzero__' then False
print(bool(X))
# In 3.X prints 99
# In 2.X prints 'in __nonzero__' but does NOT print 99
if X: print(99)