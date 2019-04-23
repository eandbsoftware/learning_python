class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
# Works in 3.X, fails in 2.X
Spam.printNumInstances()
# Fails in both
a.printNumInstances()