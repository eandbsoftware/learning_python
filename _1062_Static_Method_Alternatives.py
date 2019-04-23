'''
def printNumInstances():
    print('Number of instances created: %s' % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numberInstances += 1

a = Spam()
b = Spam()
c = Spam()
printNumInstances()
print(Spam.numInstances)
'''

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(self):
        print('Number of instances created: %s' % Spam.numInstances)

a, b, c = Spam(), Spam(), Spam()
a.printNumInstances()
Spam.printNumInstances(a)
Spam().printNumInstances()