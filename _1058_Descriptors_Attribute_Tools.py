class AgeDesc(object):
    def __get__(self, instance, owner):
        return 40
    def __set__(self, instance, value):
        instance._age = value

class descriptors(object):
    age = AgeDesc()

x = descriptors()
# Routed through AgeDesc.__get__
print(x.age)
# Routed through AgeDesc.__set__
x.age = 42
# Normal fetch
print(x._age)