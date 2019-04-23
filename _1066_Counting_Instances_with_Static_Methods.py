class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print('Number of instances: %s' % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

'''
a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()
'''

class Sub(Spam):
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

a = Sub()
b = Sub()
a.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()

class Other(Spam):
    pass

c = Other()
c.printNumInstances()