class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()

    x.setdata('King Arthur')
    x.display()

    y.setdata(3.1415)
    y.display()
    print()

    # Change instance attribute from the class itself
    x.setdata('Zoe')
    x.display()
    # Or from outside the class by assigning to an explicit instance
    x.data = 'Jason'
    x.display()

    # Generate na entirely new attribute
    x.anothername = 'spam'
    print(x.__dict__)