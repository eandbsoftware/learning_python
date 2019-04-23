class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances: %s, class name: %s' % (cls.numInstances, cls.__name__))
    printNumInstances = classmethod(printNumInstances)

'''
a, b = Spam(), Spam()
a.printNumInstances()
Spam.printNumInstances()
print()
'''

class Sub(Spam):
    def printNumInstances(cls):
        print('Extra stuff...', cls.__name__)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam):
    pass

x = Sub()
y = Spam()
x.printNumInstances(); print()
Sub.printNumInstances(); print()
y.printNumInstances(); print()

z = Other()
z.printNumInstances()