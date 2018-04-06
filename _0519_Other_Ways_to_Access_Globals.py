var = 99

def local():
    var = 0

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import _0519_Other_Ways_to_Access_Globals
    _0519_Other_Ways_to_Access_Globals.var += 1

def glob3():
    var = 0
    import sys
    glob = sys.modules['_0519_Other_Ways_to_Access_Globals']
    glob.var += 1

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)

# Use the following lines in a separate module to call
#import _0519_Other_Ways_to_Access_Globals
#_0519_Other_Ways_to_Access_Globals.test()