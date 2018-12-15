class PrivacyExc(Exception):
    pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivacyExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

t1 = Test1()
t2 = Test2()

t1.name = 'Bob'
#t2.name = 'Sue'

t2.age = 30
t1.age = 40