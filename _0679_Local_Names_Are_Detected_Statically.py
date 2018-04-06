X = 99

# X references variable in global scope
'''
def selector():
    print(X)    
'''

# Assigned names are treated as locals everywhere in a function,
# not just after the statements where they are assigned
'''
def selector():
    print(X)
    X = 88
'''

# Specify that the X referred to is global
# This means the assignment also changes the global
'''
def selector():
    global X
    print(X)
    X = 88
    print(X)
'''

# Import the enclosing module and use module attrobute notation
# to get to the global version
def selector():
    import __main__
    print(__main__.X)
    X = 88
    print(X)

selector()
