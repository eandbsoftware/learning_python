class Super:
    def delegate(self):
        self.action()
    def action(self):
        #assert False, 'action must be defined in subclass'
        raise NotImplementedError('action must be defined in subclass')
#X = Super()
#X.delegate()

class Sub(Super):
    pass
# For instances of subclasses, we still get the exception unless the subclass provides the expected method.
#X = Sub()
#X.delegate()

class Sub(Super):
    def action(self):
        print('spam')
X = Sub()
X.delegate()