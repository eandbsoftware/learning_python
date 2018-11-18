class SharedData:
    spam = 42

# Shared data
x = SharedData()
y = SharedData()
print(x.spam, y.spam)

# Change it by going through class name
SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)

# Assign name through instance
x.spam = 88
print(x.spam, y.spam, SharedData.spam)
print()

class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)

x = MixedNames(1)
y = MixedNames(2)
x.display(); y.display()