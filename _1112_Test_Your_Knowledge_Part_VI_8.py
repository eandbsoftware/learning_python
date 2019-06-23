# Problem 8
'''
class Animal:
    def speak(self):
        print("I'm alive!")
    def reply(self):
        self.speak()

class Mammal(Animal):
    def speak(self):
        print("I'm warm blooded!")

class Cat(Mammal):
    def speak(self):
        print('Meow')

class Dog(Mammal):
    def speak(self):
        print('Ruff')

class Primate(Mammal):
    def speak(self):
        print('I have opposable thumbs!')

class Hacker(Primate):
    pass
    # def speak(self):
    #     print('Hello world!')

spot = Cat()
spot.reply()

data = Hacker()
data.reply()
'''
# Problem 9
class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line("that's one ex-bird")
        self.clerk.line("no it isn't...")
        self.parrot.line(None)

class Actor:
    def line(self, text):
        print(f'{self.__class__.__name__}: {text}')

class Customer(Actor):
    pass

class Clerk(Actor):
    pass

class Parrot(Actor):
    pass

Scene().action()