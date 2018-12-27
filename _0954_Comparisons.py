# http://interactivepython.org/courselib/static/thinkcspy/Strings/StringComparison.html#  
# When you compare characters or strings to one another,
# Python converts the characters into their equivalent ordinal values 
# and compares the integers from left to right.

class C:
    data = 'spam'
    # called for self > other and other < self
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()
print(X > 'ham')
# str.__lt__ raises NotImplemented, then invokes reflective method: X.__gt__
print('ham' < X)
print(X < 'ham')
# Works by raising NotImplemented, then invoking reflective method: X.__lt__
print('ham' > X)
print()