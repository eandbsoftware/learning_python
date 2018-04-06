def gen():
    for i in range(10):
        x = yield i
        print("You passed {} to the generator!".format(x))

g = gen()

'''
print(g.send(None))
print(g.send(99))
'''
print(next(g))
print(g.send(88))
print(g.send(77))
print(next(g))
