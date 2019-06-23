# Problem 4
class Attrs:
    def __getattr__(self, name):
        print('get %s' % name)

    def __setattr__(self, name, value):
        print('set %s to %s' % (name, value))

x = Attrs()
x.append
x.spam = 'pork'
# Operators are intercepted by __getattr__ in 2.X, but fail because as coded here,
# __getattr__ doesn't return a callable. But operators aren't even intercepted in 3.X.
#x + 2
x.__getitem__
# Equivalent of operator fetch in 3.X: AttributeError
#type(x).__getitem__
x[1]
#x[1:5]