# Nested scope example 1
'''
X = 99

def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()
'''

# Nested scope example 2
def f1():
    X = 88
    def f2():
        print(X)
    return f2

action = f1()
action()