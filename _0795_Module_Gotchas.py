# Statement Order Matters in Top-Lvel Code
'''
# Error, foward reference. func1 not yet assigned.
#func1()

# Ok, 'func2' looked up later
def func1():
    print(func2())

# Error, func2 not yet assigned
#func1()

def func2():
    return 'Hello'

func1()
'''

# from Copies Names but Doesn't Link