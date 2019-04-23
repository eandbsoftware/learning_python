'''
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()
'''

class Methods(object):
    def imeth(self, x):
        print([self, x])

    @staticmethod
    def smeth(x):
        print([x])

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__
    
obj = Methods()
obj.imeth(1)
obj.smeth(2)
obj.cmeth(3)
print(obj.name)
