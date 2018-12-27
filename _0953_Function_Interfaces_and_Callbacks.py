import tkinter

class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)
    def changeColor(self):
        print('turn', self.color)

def closure(color):
    def oncall():
        print('turn', color)
    return oncall

cb1 = Callback('red')
cb2 = Callback('blue')
cb3 = closure('yellow')
cb4 = (lambda color='green': print('turn', color))

# The form
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

# Pass a callable object, not a function, to command
button1 = tkinter.Button(frame, text="Button 1", fg='red', command=cb1)
button1.pack(side=tkinter.LEFT)

# Pass a bound method; no need for instance
button2 = tkinter.Button(frame, text='Button 2', fg='blue', command=cb2.changeColor)
button2.pack(side=tkinter.LEFT)

# Pass a closure function
button3 = tkinter.Button(frame, text='Button 3', fg='yellow', command=cb3)
button3.pack(side=tkinter.LEFT)

# Pass a lambda with default
button4 = tkinter.Button(frame, text='Button 4', fg='green', command=cb4)
button4.pack(side=tkinter.LEFT)

root.mainloop()

