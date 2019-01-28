class ListInherited:
    '''
    Use dir() to collect both instance attrs and names inherited from
    its classes; Python 3.X shows more names than 2.X because of the
    implied object superclass in the new-style class module; getattr()
    fetches inherited names not in self.__dict__; user __str__ not
    __repr__, or else this loops when printing bound methods!
    '''

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s\n' % attr
            else:
                # An implicit call to self.__repr__ here for methods 
                # because methods display their class by calling their __repr__
                # value of method = <bound method {assigning class.method_name} of <{fully qualified object name} at {hex(id(obj))}>>
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __attrnames2(self, indent=' '*4):
        # Escaped % allows string to be formatted twice!
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, hex(id(self)), self.__attrnames())

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)