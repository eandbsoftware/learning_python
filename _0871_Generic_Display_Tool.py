"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':
    import _0846_person as person
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
        # def gatherAttrs(self):
        #     return 'spam'
    
    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
    print()

    # Instance vs Class Attributes
    bob = person.Person('Bob Smith')
    dir_call = dir(bob)
    print('dir call:', len(dir_call), sorted(dir_call))
    instance_attrs = bob.__dict__.keys()
    print('instance keys:', len(instance_attrs), sorted(instance_attrs))
    class_attrs = bob.__class__.__dict__.keys()
    print('class attribs:', len(class_attrs), sorted(class_attrs))
    print('class bases:', bob.__class__.__bases__)
    obj_attrs = bob.__class__.__bases__[0].__dict__.keys()
    print('object attrs:', len(obj_attrs), sorted(obj_attrs))
    all_attrs = instance_attrs | class_attrs | obj_attrs
    print(all_attrs == set(dir_call))
    print(class_attrs & obj_attrs)
