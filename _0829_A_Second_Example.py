from _0825_A_First_Example import FirstClass

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

if __name__ == '__main__':
    z = SecondClass()
    z.setdata(42)
    z.display()

    x = FirstClass()
    x.setdata('New value')
    x.display()